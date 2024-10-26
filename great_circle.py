import stdio
import sys

# read the coordinates for two points
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# approximate trigonometric functions
pi = 3.14159
sin_x1 = x1 * (pi / 180)
sin_x2 = x2 * (pi / 180)
cos_x1 = 1 - sin_x1**2
cos_x2 = 1 - sin_x2**2
cos_y_diff = 1 - (y1 - y2)**2

# great circle distance calculation using an approximation
d = 6359.83 * (sin_x1 * sin_x2 + cos_x1 * cos_x2 * cos_y_diff)

# print the distance
stdio.write(d)


...
