# importing the function
import stdio
import sys

# read player 1 pennies, player 2 pennies, and the probabilty
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# basic probability calculations using arithmetic
q = 1 - p

# calculate player 1 and player 2 probabilities
p1 = (1 - (q / p) ** n2) / (1 - (q / p) ** (n1 + n2))
p2 = (1 - (p / q) ** n1) / (1 - (p / q) ** (n1 + n2))

# print the probabilities for both players
stdio.write(str(p1)+" "+str(p2))
# stdio.write(p2)



