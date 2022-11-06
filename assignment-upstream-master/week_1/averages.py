# Write a script that prompts the user for two numbers, a and b.
# Output the the following types of averages:
# 1. The arithmetic mean
# 2. The geometric mean
# 3. The root mean square

from math import sqrt

a, b = [int(x) for x in raw_input("Enter two values: ").split()]
print("The arithmetic mean: ", (a+b)/2)
print("The geometric mean: ", sqrt(a * b))
print("The root mean square: ", sqrt((a ** 2 + b ** 2) / 2))
