import stdio
import sys


# reading the radius = (r) and angle in degrees = (theta)
r = float(sys.argv[1])
theta = float(sys.argv[2])

# converting degrees to radians using an approximation for pi
pi = 3.14159
theta_radians = theta * (pi / 180)

# using basic approximations for sin and cos
x = r * (2.71828 ** (0 * theta_radians))
y = r * (2.71828 ** (0.5 * theta_radians))

# print the cartesian coordinates
stdio.write(x)
stdio.write(y)

