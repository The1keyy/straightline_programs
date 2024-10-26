# importing the function
import sys
import stdio


# reads the month, day, and year from the command line argument
month = int(sys.argv[1])
day = int(sys.argv[2])
year = int(sys.argv[3])

# performs the day of week calculation
year_adjusted = year - (14 - month) // 12
x = year_adjusted + year_adjusted // 4 - year_adjusted // 100 + year_adjusted // 400
adjusted_month = month + 12 * ((14 - month) // 12) - 2
day_of_week = (day + x + (31 * adjusted_month) // 12) % 7

# print day of week
stdio.write(day_of_week)

