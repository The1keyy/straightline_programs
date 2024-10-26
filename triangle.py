import stdio
import sys

# read the sides of the triangle
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# check if the sides form a valid triangle using the triangle inequality
is_triangle = x <= y + z and y <= x + z and z <= x + y

# print the result
stdio.write(is_triangle)

...
