"""
Sophia Babayev, Section 10
Sidewalk
"""

square_p_step = float(input("Enter the number of sidewalk squares you move with each step. "))
num_steps = float(input("Enter the total number of steps taken. "))

num_squares = square_p_step * num_steps
round_squares = int(round(num_squares))

is_odd = bool(round_squares % 2)

print(is_odd)