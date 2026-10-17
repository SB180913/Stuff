"""
Sophia Babayev, Section 10
Finds and prints the prime factors of an integer.
"""

number = int(input())
divisor = 2
factors = []

while number > 1:
	if number % divisor == 0:
		factors.append(str(divisor))
		number //= divisor
	else:
		divisor += 1

print("*".join(factors))

