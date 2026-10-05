"""
Sophia Babayev, Section 10
Approximate pi with a loop.
"""

n = int(input())
pi = 3.0
sign = 1

for term in range(1, n + 1):
    denominator = (2 * term) * (2 * term + 1) * (2 * term + 2)
    pi += sign * 4 / denominator
    sign *= -1

print(round(pi, 8))
