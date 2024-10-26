# importing the function
import stdio
import sys

# defining the gravitational constant formula
g = 6.674 * 10**-11

# reading the masses and distance as floats from the commandline arguments
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# gravitational force calculation
force = g * (m1 * m2) / (r * r)

# prints out the calculated force
stdio.write(force)


