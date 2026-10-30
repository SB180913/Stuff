"""
Sophia Babayev, Section 10
Scale each value to a character based on its position in the range.
"""


def art_generator(values):
    fill = ".,:;=*#%@$"
    smallest = min(values)
    largest = max(values)

    if smallest == largest:
        return "*" * len(values)

    return "".join(
        fill[int((value - smallest) * 9 / (largest - smallest))]
        for value in values
    )


if __name__ == "__main__":
    line = input()
    while line != "":
        values = []
        for x in line.split():
            values.append(int(x))
        print(art_generator(values))
        line = input()