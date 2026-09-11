"""
Sophia Babayev, Section 10
Finding wheather or not the user can open the imaginary door with their inputs
"""

knob1 = int(input())
knob2 = int(input())
switch = input()

if not 1 <= knob1 <= 12 or not 1 <= knob2 <= 12:
    print("Knobs need to be set between 1-12")
elif knob1 % 2 == 0 and knob2 % 2 != 0 and switch == "up":
    print("The door opens, you get all the loot.")
elif knob1 % 2 == 0 or knob2 % 2 != 0 and switch != "up":
    print("The door clanks but does not open, try again.")
else:
    print("The handle doesn't budge.")
