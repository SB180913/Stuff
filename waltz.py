"""
Sophia Babayev, Section 10
Takes in a number of steps and produce the string.
"""

steps = int(input())
waltz = ""

for step in range(steps):
    waltz += str(step % 6 + 1)

print(waltz)