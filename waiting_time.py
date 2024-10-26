import stdio
import sys

# read from command line arguments
lmbda = float(sys.argv[1])
t = float(sys.argv[2])

# calculate the waiting time probability using basic exponentiation
p = 2.71828 ** (-lmbda * t)

# print the calculated probability
stdio.write(p)



