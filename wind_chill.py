# importing the function
import stdio
import sys

# read temperature and wind speed as floats from the command line arguments
t = float(sys.argv[1])
v = float(sys.argv[2])

# wind chill formula calculation
wind_chill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16

# print the wind chill value
stdio.write(wind_chill)


