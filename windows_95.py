"""
Sophia Babayev, Section 10
Check if the string key is valid or not
"""

key = input()
valid = len(key) % 3 == 0

for index in range(2, len(key), 3):
    if int(key[index]) % 2 != 0:
        valid = False

if valid:
    print("Welcome! Booting the system!")
else:
    print("Invalid key! The authorities have been notified.")
