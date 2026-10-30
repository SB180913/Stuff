"""
Sophia Babayev, Section 10
Return the next row using adjacent values from level.
"""


def next_level(level):
    if not level:
        return []

    next_row = [level[0]]
    for index in range(len(level) - 1):
        next_row.append(level[index] + level[index + 1])
    next_row.append(level[0])

    return next_row


if __name__ == "__main__":
    in_string = input()

    while in_string != "":
        values = []
        for value in in_string.split():
            values.append(int(value))

        print(next_level(values))
        in_string = input()
