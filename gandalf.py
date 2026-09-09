"""
Sophia Babayev, Section 10
To find out which LOTR character I am based on the inputs
"""

print("What is your race: human, maiar, or hobbit?")
race = input()
if race == "human":
    print("Are you the King of Gondor?")
    king = input()
    if king == "yes":
        print("You are Aragorn son of Arathorn")
    else:
        print("Did you try to take the ring from Frodo?")
        ring = input()
        if ring == "yes":
            print("You are Boromir, poor guy...")
        else:
            print("You are Theoden, probably.")
elif race == "maiar":
    print("Are you good or evil?")
    philo = input()
    if philo == "good":
        print("You are Gandalf")
    elif philo == "evil":
        print("Did you forge the One Ring?")
        forge = input()
        if forge == "yes":
            print("You are Sauron")
        else:
            print("You are Saruman")
elif race == "hobbit":
    print("Do you carry the One Ring?")
    carry = input()
    if carry == "yes":
        print("You are Frodo Baggins")
    else:
        print("Are you a gardener?")
        gard = input()
        if gard == "yes":
            print("You are Samwise")
        else:
            print("You are either Merry or Pippin")
else:
    print("You are an Orc, sorry about that.")

        