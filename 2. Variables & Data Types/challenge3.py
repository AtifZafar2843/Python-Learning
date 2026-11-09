# Challenge:
# Reassignment order and why sequence matters
# You are given three variables:
# a = 10
# b = 20
# c = 30
# Rotate their values so that:
# • a takes b's value
# • b takes c's value
# • c takes a's ORIGINAL value
# After the rotation, printing a, b, c should give:
# 20 30 10
# Rules:
# • Do it in as few lines as possible.
# • Do NOT hardcode 10, 20, or 30 after the initial setup.
# In a comment, explain why the ORDER of your assignments matters — what would happen to a's original value if you overwrote it first?

# Solution:
a = 10
b = 20
c = 30

a = b
b = c
c = a
print(a, b, c)
# Mujhe output 20, 30, 20 show hua hai
# Agar mein a ki value ko kahi bacha kar hi nahi rakhunga to a ki ORIGINAL value to mujhe milegi hi nahi that's why Assignment ORDER metter karta hai 

# Agar mujhe 20, 30, 10 show karana hai output me to mujhe ek aur temprory veriable chahiye hoga:
a = 10
b = 20
c = 30

temp = a
a = b
b = c
c = temp
print(a, b, c)