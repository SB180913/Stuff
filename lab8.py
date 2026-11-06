"""
Sophia Babayev, Section 10
Lab 8: Favorite Numbers
"""

import string


favorites = {}

while True:
    answer = input("What do you want to do (add favorite number), print favorite numbers for <person>, or quit?")
    parts = answer.split()

    if answer == "quit":
        break

    if parts[0] == "print":
        person = parts[1]
        print(favorites[person])
    elif len(parts) != 2:
        print("Enter one name and one number.")
        continue

    person, number = parts

    try:
        number = int(number)
    except ValueError:
        print("The second part must be an integer.")
        continue

    if number in favorites.values():
        print("That number has already been picked. Be more original!")
    else:
        favorites[person] = number
        print(f"{number} is set as {person}'s favorite")