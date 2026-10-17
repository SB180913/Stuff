"""
Sophia Babayev, Section 10
Accumulates integers until the Gauss sum reaches the input.
"""


number = int(input())
iterations = 0
gauss_sum = 0

while gauss_sum < number:
	iterations += 1
	gauss_sum += iterations

print(
	f"After {iterations} iterations, the gauss sum is {gauss_sum} "
	f"which exceeds (or is equal to) the number {number}"
)