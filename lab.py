"""
Sophia Babayev, Section 10
Lab
"""

def sum_string_lengths(strings):
    """
    Given a list of strings, add up all their lengths.
    """
    total = 0
    for s in strings:
        total += len(s)
    return total


def get_names():
    """
    Ask the user for a list of names in while loop.
    """
    names = []
    while True:
        name = input("Enter a name, STOP to stop: ")
        if name == "STOP":
            break
        names.append(name)
    return names


if __name__ == '__main__':
    kitties = ["Jules", "Stubby", "Flash"]
    # print the sum of the lengths of the strings in kitties
    print("Length of kitties strings is", sum_string_lengths(kitties))

    # gets names from the user and reports how many letters are in all the names
    print("Length of names you typed in is", sum_string_lengths(get_names()))