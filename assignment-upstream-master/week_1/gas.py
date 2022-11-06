# Write a script that prompts the user for a number of gallons of gasoline.
# Reprint that value, along with its conversion to other measurements:
# - Equivalent number of liters
# - Number of barrels of oil required to produce it * Price in U.S. dollars
# Figures to use:
# - 1 gallon is equivalent to 3.7854 liters.
# - 1 barrel of oil produces 19.5 gallons of gas.
# - The average price of gas is approximately $3.65.
# Save your script as gas.py

liter_conversion = 3.78541178
barrel_conversion = 19.5
avg_price = 3.65

gallons = input("Enter a number of gallons of gasoline:")
print("The Number of gallons entered is:", gallons)
print("Equivalent number of liters", gallons * liter_conversion)
print("Number of barrels of oil required to produce it: ", gallons / barrel_conversion)
price = round(gallons * avg_price, 2)
print("Price: $", price)
