"""
Sophia Babayev, Section 10
Solving a 2x2 grid sudoku game with user inputs
"""

print("Enter the numbers for the 2x2 grid (a b c d) one by one")

a = int(input())
b = int(input())
c = int(input())
d = int(input())


if a != b and c != d and a != c and b != d:
    print("solved")
else:
    print("unsolved")