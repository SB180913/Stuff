"""
Sophia Babayev, Section 10
Keep only letters that appear in every line
"""


def common_letter(lines):
    common = set(lines[0])

    for line in lines[1:]:
        common &= set(line)

    return common.pop()


if __name__ == "__main__":
    lines = []
    line = input()
    while line != "stop":
        lines.append(line)
        line = input()

    print(common_letter(lines))
