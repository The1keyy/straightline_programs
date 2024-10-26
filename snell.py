import stdio
import sys

# read incident angle and refractive indices n1 and n2
theta1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# calculate the angle of refraction using snell's law
theta2 = theta1 * (n1 / n2)

# output the refracted angle
stdio.write(theta2)


