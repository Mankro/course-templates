import copy
import os.path

from django.shortcuts import render

from access.types.auth import get_uid
from access.types.stdasync import _acceptSubmission
from util.files import create_submission_dir, save_submitted_file, \
    write_submission_file
from util.http import not_modified_since, not_modified_response, cache_headers
from util.templates import _exercise_context


# Copied from mooc-grader/access/types/stdasync.py, function acceptGeneralForm,
# and slightly modified in order to save the uid parameter into the submission
# directory.
def acceptGeneralFormAndSaveUidToSdir(request, course, exercise, post_url):
    '''
    Presents a template and accepts form containing any input types
    (text, file, etc) for grading queue.

    Save the user id (uid) parameter from the request into the submission
    directory that is accessible to the grading container.
    '''
    if not_modified_since(request, exercise):
        return not_modified_response(request, exercise)

    fields = copy.deepcopy(exercise.get("fields", []))
    result = None
    miss = False

    if request.method == "POST":
        # Parse submitted values.
        for entry in fields:
            entry["value"] = request.POST.get(entry["name"], "").strip()
            if "required" in entry and entry["required"] and not entry["value"]:
                entry["missing"] = True
                miss = True

        files_submitted = []
        if "files" in exercise:
            # Confirm that all required files were submitted.
            #files_submitted = [] # exercise["files"] entries for the files that were really submitted
            for entry in exercise["files"]:
                # by default, all fields are required
                required = ("required" not in entry or entry["required"])
                if entry["field"] not in request.FILES:
                    if required:
                        result = { "rejected": True, "missing_files": True }
                        break
                else:
                    files_submitted.append(entry)

        if miss:
            result = { "fields": fields, "rejected": True }
        elif result is None:
            # Store submitted values.
            sdir = create_submission_dir(course, exercise)
            for entry in fields:
                write_submission_file(sdir, entry["name"], entry["value"])

            if "files" in exercise:
                if "required_number_of_files" in exercise and \
                        exercise["required_number_of_files"] > len(files_submitted):
                    result = { "rejected": True, "missing_files": True }
                else:
                    # Store submitted files.
                    for entry in files_submitted:
                        save_submitted_file(sdir, entry["name"], request.FILES[entry["field"]])
            # Store the user's personal identifier to the submission directory
            # that is accessible in the grading container.
            uids = get_uid(request) # string like "123" or "123-567" for group submissions
            with open(os.path.join(sdir, 'uid'), 'w') as f:
                f.write(uids)
            return _acceptSubmission(request, course, exercise, post_url, sdir)

    return cache_headers(
        render_configured_template_with_uid(
            request, course, exercise, post_url,
            "access/accept_general_default.html", result
        ),
        request,
        exercise
    )


# Copied from mooc-grader/util/templates.py, function render_configured_template
def render_configured_template_with_uid(request, course, exercise, post_url, default=None, result=None):
    '''
    Renders a configured or optional default template.

    @type request: C{django.http.request.HttpRequest}
    @param request: a request to handle
    @type course: C{dict}
    @param course: a course configuration
    @type exercise: C{dict}
    @param exercise: an exercise configuration
    @type post_url: C{str}
    @param post_url: the post URL for the exercise
    @type default: C{str}
    @param default: a default template name to use if not configured
    @type result: C{dict}
    @param result: results from grading
    @rtype: C{django.http.response.HttpResponse}
    @return: a response
    '''
    template = None
    if "template" in exercise:
        template = exercise["template"]
    elif default is not None:
        template = default
    else:
        raise ConfigError("Missing \"template\" in exercise configuration.")

    return render_template_with_uid(request, course, exercise, post_url, template, result)


# Copied from mooc-grader/util/templates.py, function render_template
def render_template_with_uid(request, course, exercise, post_url, template, result=None):
    '''
    Renders a template.

    @type request: C{django.http.request.HttpRequest}
    @param request: a request to handle
    @type course: C{dict}
    @param course: a course configuration
    @type exercise: C{dict}
    @param exercise: an exercise configuration
    @type post_url: C{str}
    @param post_url: the post URL for the exercise
    @type template: C{str}
    @param template: a template name to use
    @type result: C{dict}
    @param result: results from grading: may include error=True, accepted=True, points=%d
    @rtype: C{django.http.response.HttpResponse}
    @return: a response
    '''
    if template.startswith('./'):
        template = course['key'] + template[1:]
    return render(request, template,
        _exercise_context_with_uid(course, exercise, post_url, result, request))


def _exercise_context_with_uid(course, exercise, post_url, result=None, request=None):
    ctx = _exercise_context(course, exercise, post_url, result, request)
    ctx['uid'] = get_uid(request)
    return ctx
