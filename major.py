"""
Sophia Babayev, Section 10
What's your major?
"""


print("What is your major?")


major = input()

if major == "CMSC" or major == "CMPE":
    print("You will need to earn at least a B.")
else:
    print("You will need to earn at least a C.")