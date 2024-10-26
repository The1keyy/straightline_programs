import stdio
import sys

# read the number of sides
n = int(sys.argv[1])

# approximate random die rolls
roll1 = n // 2
roll2 = n // 2

# print the sum of the rolls
stdio.writeln(roll1 + roll2)

