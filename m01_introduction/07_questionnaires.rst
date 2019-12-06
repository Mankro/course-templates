Creating questionnaire exercises
================================

One can easily create simple questionnaire exercises for an A+ course, such as
one-line text answers and multiple choice exercises. This page shows many
examples on these.

*Technical remark.* The most recent and complete documentation on this can
be found at `the source code of the A+ RST tools package
<https://github.com/Aalto-LeTech/a-plus-rst-tools>`_. Technically A+ RST tools
provide specific Sphinx directives for writing course HTML and configuration
files, and then A+ and mooc-grader implement the actual functionality.

General description of the options
----------------------------------

The ``questionnaire`` directive implements a questionnaire exercise. Its
arguments define the exercise key (exercise identifier for A+) and max points
with the optional difficulty (``A``, ``B``, ``C``, etc.). For example,
``.. questionnaire:: easyexercise A50`` sets key to ``easyexercise``,
maximum points to ``50`` and difficulty ``A``. The difficulty parameter
does not affect any scorekeeping, but only works as an indicator for the
student. (The A+ REST API can group earned points by the difficulty so that
the teacher may use the difficulties for computing final course grades.)

The questionnaire directive accepts the following options:

* ``submissions``: max submissions
* ``points-to-pass``: points to pass
* ``feedback``: If set, assumes the defaults for a feedback questionnaire
* ``no-override``: If set, the conf.py override setting is ignored
* ``pick_randomly``: integer. Set the pick_randomly setting for the quiz
  (select N questions randomly on each load)
* ``category``: exercise category

The contents of the questionnaire directive define the questions and possible
instructions to students.

The **question directives** ``pick-one``, ``pick-any``, and ``freetext`` take
the points of the question as the first argument. The sum of the question points
should be equal to the questionnaire max points. The question directives accept
the following options:

* ``class``: `CSS class <03_css>`_
* ``required``: If set, the question is required and empty answers are rejected
* ``key``: a manually set key for the question. This affects the HTML **input**
  element and the key in the submission data. If no key is set, note that
  automatically added keys change when the order and amount of questions is
  modified.

The ``freetext`` directive also accepts the following options in addition to
the common question options:

* ``length``: (horizontal) length for the HTML text input in characters
* ``height``: vertical height of the text input in rows. If this is greater than
  1, the **textarea** HTML element is used. Otherwise, a text input is used.
* Also other options are defined in the `questionnaire code of A+ RST tools
  <https://github.com/Aalto-LeTech/a-plus-rst-tools/blob/master/directives/questionnaire.py>`_,
  but they mainly affect the CSS classes and they were implemented for very
  narrow usecases.

The ``freetext`` directive accepts a second positional argument after the points.
It defines the compare method for the model solution. A textual input can be
compared with the model solution as ``int``, ``float``, ``string``,
or ``unsortedchars`` (unsorted character set). Another option is ``regexp``
which takes the correct answer as a regular expression and tries to match the
submission with it using the `Python re library <https://docs.python.org/3/library/re.html>`_.

Strings have comparison modifiers that are separated with a hyphen (``-``).
For example, to create a freetext question which compares the answer to the
correct answer as string, and ignores whitespace characters and quotes, write
``.. freetext:: 30 string-ignorews-ignorequotes``.

* ``ignorews``: ignore whitespace (all space characters, applies to regexp too)
* ``ignorequotes``: iqnore quotes ``"`` around
* ``requirecase``: require identical lower and upper cases (only with the string type)
* ``ignorerepl``: ignore REPL prefixes
* ``ignoreparenthesis``: ignore parenthesis ``( )``

The question directives may define instructions. After the instructions,
the contents of the directive define the choices, the correct solution, and
possible hints. The hints are targeted to specific choices and they are shown
after answering. See the example below.

.. questionnaire:: questionnaire_test_pick_random A
  :title: Test pick randomly in a questionnaire
  :submissions: 50
  :pick_randomly: 3

  .. pick-any:: 10

    what is 1 + 3?
    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 4
    c. 3
    d. 1

  .. pick-any:: 10

    what is 2 + 3?
    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    b. 3
    *c. 5

  .. pick-any:: 10

    what is 3 + 3?

    *a. 6
    b. 9
    c. 3

  .. pick-any:: 10

    what is 4 + 3?

    a. 9
    b. 8
    c. 3
    *d. 7

  .. pick-one:: 10

    what is 5 + 3?

    a. 9
    b. 3
    c. 10
    d. 7
    *e. 8
    f. 1
    g. 2

  .. pick-one:: 10

    what is 6 + 3?

    a. 1
    b. 10
    c. 3
    d. 0
    e. 7
    *f. 9
    g. 8

.. questionnaire:: questionnaire_test_pick_random2 A
  :title: Test pick randomly in a questionnaire 2
  :submissions: 50
  :pick_randomly: 3
  :preserve-questions-between-attempts:

  .. pick-any:: 10

    what is 1 + 2?
    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    b. 4
    *c. 3
    d. 1

  .. pick-any:: 10

    what is 2 + 2?
    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    b. 3
    *c. 4

  .. pick-any:: 10

    what is 3 + 2?

    *a. 5
    b. 9
    c. 3

  .. pick-any:: 10

    what is 4 + 2?

    a. 9
    b. 8
    c. 3
    *d. 6

  .. pick-one:: 10

    what is 5 + 2?

    a. 9
    b. 3
    c. 10
    *d. 7
    e. 8
    f. 1
    g. 2

  .. pick-one:: 10

    what is 6 + 2?

    a. 1
    b. 10
    c. 3
    d. 0
    e. 7
    f. 9
    *g. 8


.. questionnaire:: test_pick_randomly_random_question
  :submissions: 40
  :points-to-pass: 0
  :pick_randomly: 1

  .. pick-any:: 10
    :randomized: 7
    :correct-count: 3
    :partial-points:
    :preserve-questions-between-attempts:

    Which of the following are **yellow**?

    *a. butter
    *b. banana
    c. sky
    d. soil
    e. orange
    f. kiwi
    g. green apple
    h. red apple
    i. watermelon
    j. chicken wings
    k. barbeque pork
    l. cake
    m. strawberry
    n. blueberry
    o. raspberry
    *p. sun
    *q. yellow taxi
    r. British black taxi
    s. Computer peripherals
    *t. Homer Simpson
    *u. lemon
    
    a § yes, butter is yellow
    b § yes, banana is yellow
    p § yes, sun is yellow
    q § yes, yellow taxi is yellow
    t § yes, Homer is yellow
    u § yes, lemon is yellow
    c § no, sky is blue
    l § no, cake is white
    o § no, raspberry is red
    d § no, soil is brown
    m § no, strawberry is red

  .. pick-any:: 10
    :randomized: 7
    :correct-count: 3
    :partial-points:
    :preserve-questions-between-attempts:

    Which of the following are **red**?

    a. butter
    b. banana
    c. sky
    d. soil
    e. orange
    f. kiwi
    g. green apple
    *h. red apple
    *i. watermelon (in the inside)
    j. chicken wings
    k. barbeque pork
    l. cake
    *m. strawberry
    n. blueberry
    *o. raspberry
    p. sun
    q. yellow taxi
    r. British black taxi
    s. Computer peripherals
    t. Homer Simpson
    u. lemon

.. questionnaire:: test_random_question
  :submissions: 40
  :points-to-pass: 0

  .. pick-any:: 10
    :randomized: 5
    :correct-count: 3
    :partial-points:

    Which of the following are **yellow**?

    *a. butter
    *b. banana
    c. sky
    d. soil
    e. orange
    f. kiwi
    g. green apple
    h. red apple
    i. watermelon
    j. chicken wings
    k. barbeque pork
    l. cake
    m. strawberry
    n. blueberry
    o. raspberry
    *p. sun
    *q. yellow taxi
    r. British black taxi
    s. Computer peripherals
    *t. Homer Simpson
    *u. lemon
    
    a § yes, butter is yellow
    b § yes, banana is yellow
    p § yes, sun is yellow
    q § yes, yellow taxi is yellow
    t § yes, Homer is yellow
    u § yes, lemon is yellow
    c § no, sky is blue
    l § no, cake is white
    o § no, raspberry is red
    d § no, soil is brown
    m § no, strawberry is red

  .. pick-any:: 10
    :randomized: 5
    :correct-count: 3
    :partial-points:
    :preserve-questions-between-attempts:

    Which of the following are **red**?

    a. butter
    b. banana
    c. sky
    d. soil
    e. orange
    f. kiwi
    g. green apple
    *h. red apple
    *i. watermelon (in the inside)
    j. chicken wings
    k. barbeque pork
    l. cake
    *m. strawberry
    n. blueberry
    *o. raspberry
    p. sun
    q. yellow taxi
    r. British black taxi
    s. Computer peripherals
    t. Homer Simpson
    u. lemon

Examples
--------

copied from rst-tools README

.. questionnaire:: 1 A
  :submissions: 40
  :points-to-pass: 0

  This is a questionnaire with the key `1` that grants at maximum 70 points
  of difficulty A. Students can make at most 4 submissions.
  This exercise is marked passed when 0 points are reached (the default).

  .. pick-one:: 10
    :required:

    What is 1+1?

    a. 1
    *b. 2
    +c. 3
    d. 4

    !b § Count again!
    b § That is correct!
    c § Too much

  (Hints can be included or omitted in any question.)

  .. pick-one:: 10
    :required:
    :dropdown:

    What is 1+2?

    0. 0
    1. 1
    2. 2
    +*3. 3

  .. pick-any:: 10
    :partial-points:

    Pick the two **first**. Since the 'partial-points' option is set,
    some points are awarded with a partially correct answer. If either one of the
    correct options is not chosen or one of the wrong fields is chosen, 5 points are
    still awarded. Selecting the last neutral option does not affect the points.

    +*a. this is the **first**
    *b. this is the **second**
    c. this is the **third**
    d. this is the **fourth**
    ?e. choosing this does not affect the granted points
    
    a § you chose a: correct
    c § you chose c: incorrect
    e § you chose e: neutral

  .. pick-any:: 15
    :partial-points:
    :required:

    zero non-neutral

    +?a. this is the **first**
    ?b. this is the **second**
    ?c. this is the **third**

  .. pick-any:: 15
    :partial-points:

    one non-neutral

    a. this is the **first**
    ?b. this is the **second**
    ?c. this is the **third**

  .. pick-any:: 20

    no correct options

    a. this is the **first**
    b. this is the **second**
    c. this is the **third**

  .. pick-any:: 15
    :partial-points:

    no correct, partial

    a. this is the **first**
    b. this is the **second**
    c. this is the **third**

  .. pick-any:: 15
    :partial-points:

    two non-neutral, b is correct

    a. this is the wrong
    *b. this is the correct
    ?c. this is the neutral

  .. freetext:: 30 string-ignorews-ignorequotes
    :length: 10

    A textual input can be compared with the model solution as integer, float or string.
    Here the correct answer is "test". Surrounding quotes are ignored in the solution
    as well as whitespace everywhere (modifiers ignorequotes and ignorews).

    test
    !test § Follow the instruction.

  .. freetext:: 10 regexp

    This question accepts either "red" or "blue" as the correct answer.
    The model solution is a regular expression.

    red|blue


.. questionnaire:: questionnaire_demo
  :title: A simple multiple-choice questionnaire
  :submissions: 3

  .. pick-one:: 10
    :required:

    Subdirective ``pick-one`` defines a single-choice question.
    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

    a § Not quite. Remember the cube root.
    b § Correct!
    c § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.

  .. pick-any:: 10
    :required:

    Subdirective ``pick-any`` defines a multiple-choice question.

    When :math:`(x + 1)^2 = 16`, what is :math:`x`?

    a. 4
    *b. an integer
    *c. 3
    d. an irrational number
    e. -3
    *f. -5

    a § Rather close. Remember that you can add or subtract the same number to the both sides of the equation.
    b § Correct!
    c § Correct!
    d § No. This equation has a nice and easy solution.
    e § Remember that :math:`x^2 = q \leftrightarrow x = \pm \sqrt{q}`
    f § Correct!

  .. pick-any:: 10
    :required:
    
    You must select "yes".
    
    *a. Yes

  .. pick-one::

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

  .. pick-any:: 0

    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    *b. 2
    c. 3

  .. freetext:: 1 int
    :required:

    The answer can be a number, an integer. What is :math:`3 + 8`?

    11


The ``freetext`` subdirective creates text boxes and grades based on their
input.

.. questionnaire:: questionnaire_text_demo
  :title: A simple multiple-choice questionnaire
  :submissions: 3

  .. freetext::
    :length: 10

    This is the most basic free text questionnaire. The correct answer is
    ``test``. You can write at most 10 characters into the box.

    test
    !test § Follow the instruction.


  .. freetext:: 0 int
    :length: 7

    The answer can be a number, an integer. What is :math:`3 + 8`?

    11
    !11 § Follow the instructions.


  .. freetext:: 0 float
    :length: 7

    The answer can also be a decimal number (floating point number).
    What is :math:`3 / 8` in decimal? (When the question uses the float type,
    the grader accepts also answers that slightly differ from the model solution.)

    0.378
    !0.378 § Hint: the answer is between 0 and 1. Use the decimal point and write three first decimals, for example, ``0.924``.

Testing the questionnaries
..........................

It is good practise to test your questionnaire, especially if there are
several correct answers. Note that A+ will show the correct answers for the
students who have submitted for the maximum number of times (but not for anyone
else).


.. admonition:: String, int, or float?
  :class: info

  Use the ``int`` answer type always when the answer is an integer. Of course
  the answer could be compared to the right answer as a string. However, the
  benefits of ``int`` over ``string`` are the following. First, extra space
  characters are always ignored. Second, A+ shows a histogram of the numerical
  answers to the teacher when they click on *View all submissions* on the
  exercise box in A+, and then *Summary*. See Figure "the summary a
  float-freetext questionnaire" below.

  ``float`` works the same way as ``int``. Currently it considers the answer
  to be correct if the difference between student's answer and the model
  solution is at most 0.02.

.. figure:: /images/questionnaire/summary-freetext-float.png
   :alt: Screenshot of A+: summary of a float-type freetext question

   **Figure:** *the summary of a float-freetext questionnaire*. In this case, 304
   students (83 %) have answered the question and most of them (300) have
   received 20 points. There is only one question whose correct answer is
   between 4.8 and 5.0, with 300 students giving that answer. Four students
   have an incorrect answer having value between 1.4 and 1.6.


.. figure:: /images/questionnaire/summary-freetext-string.png
  :alt: Screenshot of A+: summary of a string-type freetext question

  **Figure:** *the summary of a string-freetext questionnaire*. The answer
  is an SQL query, and A+ shows the unique answers. There are four identical
  answers of one type and three identical answers of another type.


.. questionnaire:: questionnaire_text_demo_2 10

  .. freetext:: 5 string-ignorews-ignorequotes
    :length: 10


    Here the correct answer is "anothertest". Surrounding quotes are
    ignored in the solution as well as whitespace everywhere. (modifiers
    ignorequotes and ignorews).

    anothertest
    !anothertest § Follow the instruction
    test § This was the answer to the first question.

  .. freetext:: 5 unsortedchars-ignorews
    :length: 7

    An ``unsortedchars`` example. What are the unique vovels in the word
    "cacophonic"? Correct answers are: aio, aoi, iao, ioa, oai, oia, and
    also the versions with two o's, because *unsortedchars* always compares
    unique characters.

    aio


Regular expressions are useful when there are multiple solutions, or when
one wants to have some tolerance in numeric questions, like accept real
numbers beginning with 0.014, 0.015, or 0.016.

.. questionnaire:: questionnaire_regexp 20
  :title: Fun with regular expressions
  :submissions: 10

  .. freetext:: 10 regexp
    :length: 7

    Type either "cat" or "dog".

    ^(cat|dog)$

  .. freetext:: 10 regexp
    :length: 7

    What is the value of :math:`\pi` with four most significant digits?
    This will accept ``3.141``, ``3.1415``, ``3.1416``, ``3.14159``, that is,
    ``3.141`` and zero or more digits after that.

    ^3\.141\d*$


.. submit:: test_ta_pool 10
  :config: exercises/query-spring.yaml


Additional information
----------------------

See the source code of `the A+ RST tools questionnaire directive
<https://github.com/Aalto-LeTech/a-plus-rst-tools/blob/master/directives/questionnaire.py>`_
and the corresponding `form implementation in mooc-grader
<https://github.com/Aalto-LeTech/mooc-grader/blob/master/access/types/forms.py>`_.

.. questionnaire:: questionnaire_test_feedback 3
  :title: Test feedback questionnaire
  :submissions: 30
  :feedback:

  .. pick-one:: 0
    :required:

    Subdirective ``pick-one`` defines a single-choice question.
    When :math:`(x + 1)^3 = 27`, what is :math:`x`?

    a. 9
    b. 2
    c. 3

  .. pick-any::
    :required:

    Subdirective ``pick-any`` defines a multiple-choice question.

    When :math:`(x + 1)^2 = 16`, what is :math:`x`?

    a. 4
    b. an integer
    c. 3
    d. an irrational number
    e. -3
    f. -5

  .. pick-any::
    :required:
    
    You must select "yes".
    
    a. Yes

