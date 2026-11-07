"""
Sophia Babayev, Section 10
Update a group's bill or return its total when they check out
"""


def tablemath(groups, command):
    parts = command.split()
    action, group = parts[0], parts[1]

    if action == "seat":
        groups[group] = 0
    elif action == "spend":
        groups[group] += int(parts[2])
    elif action == "checkout":
        return groups.pop(group)


if __name__ == "__main__":
    groups = {}
    line = input()
    while line != "stop":
        result = tablemath(groups, line)
        if result is not None:
            print(result)
        line = input()
