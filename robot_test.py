"""
Sophia Babayev, Section 10
If else statments
"""

print("Are you a human or a robot?")

being = input()

if being == "human":
    print("Humans must be destroyed!")
elif being == "robot":
    print("Administer the test, which of the following would you most prefer? puppy, flower, or data file?")
    answer = input()
    if answer == "puppy":
        print("Get the intruder! Get the humanoid!")
    elif answer == "flower":
        print("That is acceptable, pass on mechanical friend.")
    elif answer == "data file":
        print("Very good, degrees outside, it is a robot of some esteem.")
        
        