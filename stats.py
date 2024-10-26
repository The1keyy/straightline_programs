import stdio
import sys

# read range for generating random like numbers
a = int(sys.argv[1])
b = int(sys.argv[2])

# approximate the random number generation using mid range values
x1 = (a + b) / 2
x2 = (a + b) / 2
x3 = (a + b) / 2

# calculate mean, variance, and standard deviation using basic arithmetic
mean = (x1 + x2 + x3) / 3
variance = ((x1 - mean)**2 + (x2 - mean)**2 + (x3 - mean)**2) / 3
dev = variance ** 0.5

# print the  mean, variance, and standard deviation
stdio.write(mean)
stdio.write(variance)
stdio.write(dev)


...
