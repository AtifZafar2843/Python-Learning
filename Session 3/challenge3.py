# Challenge:
# f-strings, and using a number as both text and math
# Ask the user for 5 inputs: a name, an animal, a number, a food, and a city. Then weave them into a funny paragraph using an f-string.
# The number must be used TWICE: once as plain text in the story, and once inside a calculation that also appears in the story.

# Example:
# Enter a name: Aisha
# Enter an animal: panda
# Enter a number: 3
# Enter a food: samosa
# Enter a city: Delhi

# One day in Delhi, Aisha met a talking panda.
# The panda ate 3 samosas... then asked for 3 * 2 = 6 more!

# Remember to convert the number input with int() before doing the multiplication.

# Solution:
name = input("Enter Your Name:")
animal = input("Enter an animal name:")
num = int(input("Enter a number:"))
food = input("Enter a food name:")
city = input ("Enter your city:")

print(name)
print(animal)
print(num)
print(food)
print(city)

print(f"One day in {city}, {name} met a talking {animal}. The {animal} ate {num} {food}... then asked for {num} * 2 = {num * 2} more!")