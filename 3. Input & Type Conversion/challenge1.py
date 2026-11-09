# Challenge:
# Reading input and converting strings to numbers
# Ask the user for a temperature in Celsius, then print it in both Fahrenheit and Kelvin.

# Formulas:
# • Fahrenheit = (C × 9/5) + 32
# • Kelvin     = C + 273.15

# Remember: input() gives you a string, so convert it with float() before doing any math — otherwise you'll hit the classic type error.

# Example:
# Enter temperature in Celsius: 37
# 37.0 C = 98.6 F
# 37.0 C = 310.15 K

# Solution:
# take temprature from user and convert it into float value.
celcius = float(input("Enter temprature in celcius:"))

# Fahrenheit formula
fahrenheit = (celcius * 9/5) + 32
# Kelvin formula
kelvin = celcius + 273.15

# Printing celcius value into fahrenheit and kelvin.
print(celcius, "C =", fahrenheit, "F")
print(celcius, "C =", kelvin, "K")