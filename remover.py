"""
Sophia Babayev, Section 10
Removes every matching character from the line
"""


def remover(line, to_remove):
    characters = list(line)
    index = 0

    while index < len(characters):
        if characters[index] == to_remove:
            characters.pop(index)
        else:
            index += 1

    return "".join(characters)


if __name__ == "__main__":
    sentence = input()
    while sentence != "stop":
        letter_to_remove = input()
        print(remover(sentence, letter_to_remove))
        sentence = input()
