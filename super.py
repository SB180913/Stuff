"""
Sophia Babayev, Section 10
If else statments super
"""

print("Are you a hero or villain?")

role = input()

if role == "hero":
    print("How many people have you saved?")
    saved = int(input())
    if saved >= 100:
        print("Wow, great job saving the city!")
    elif saved > 10 and saved < 100:
        print("Sounds like you’re making a difference!")
    else:
        print("Go on more patrols!")
elif role == "villain":
    print("What’s your name?")
    name = input()
    print(f"Welcome, {name}. You sounds pretty evil!")
else:
    print("Invalid input.")