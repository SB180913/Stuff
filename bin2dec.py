"""
Sophia Babayev, Section 10
C10onvert a binary string to decimal.
"""

binary_string = input()
decimal = 0
place_value = 2 ** (len(binary_string) - 1)

for bit in binary_string:
    if bit == "1":
        decimal += place_value
    place_value //= 2

print(decimal)