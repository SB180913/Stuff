"""
Sophia Babayev, Section 10
Return the name of the person whose alibi conflicts with a confirmation
"""


def alibi(statements):
    stories = {}

    for statement in statements:
        words = statement.split()
        person, partner, time = words[0], words[3], words[5]
        stories.setdefault(time, {})[person] = partner

    for time_stories in stories.values():
        for person, partner in time_stories.items():
            if time_stories.get(partner) not in (None, person):
                return person


if __name__ == "__main__":
    statements = []
    statement = input()
    while statement != "stop":
        statements.append(statement)
        statement = input()

    print(alibi(statements))