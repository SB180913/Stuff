"""
Sophia Babayev, Section 10
Finds the most common word in the input lines
"""

import string


def wordcoach(lines):
    counts = {}

    for line in lines:
        for word in line.lower().split():
            word = word.strip(string.punctuation)
            if word:
                counts[word] = counts.get(word, 0) + 1

    if not counts:
        return ""

    return max(counts, key=counts.get)


if __name__ == "__main__":
    lines = []

    line = input()
    while line != "stop":
        lines.append(line)
        line = input()

    print(wordcoach(lines))