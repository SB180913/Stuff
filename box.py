"""
Sophia Babayev, Section 10
Make digital boxes.
"""

rows = int(input())
columns = int(input())

for row in range(rows):
    for column in range(columns):
        if row == 0 or row == rows - 1 or column == 0 or column == columns - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()