import sys

max_points = 10
points = 0
try:
    with open('solution') as submitted_file:
        # student's submission
        solution = int(submitted_file.read().strip())

    if solution == 1:
        # correct solution
        points = max_points

    with open('/personalized_exercise/mydata', 'rb') as f:
        binary_hex = f.read().hex()

    print("Your solution was: {}".format(solution))
    print("Your personalized binary file was: {}".format(binary_hex))

except Exception as e:
    print("ERROR", file=sys.stderr)
    print(e, file=sys.stderr)
finally:
    print("TotalPoints: {}".format(points))
    print("MaxPoints: {}".format(max_points))
