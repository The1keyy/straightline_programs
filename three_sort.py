# importing the function
import sys
import stdio

# read the three integers from commandline arguments
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# use min max and arithmetic to sort the numbers
smallest = min(x, y, z)
largest = max(x, y, z)
middle = x + y + z - smallest - largest

# print the sorted numbers
stdio.write(str(smallest) + " " + str(middle) + " " + str(largest))

