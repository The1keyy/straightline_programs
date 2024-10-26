# importing the function
import sys
import stdio

# read the weight and the height as floats from command line arguments
weight = float(sys.argv[1])
height = float(sys.argv[2])

# calculate bmi using the formula
bmi = weight / (height * height)

# print the bmi value
stdio.write(bmi)
