"""
Sophia Babayev, Section 10
First project
"""

Q1 = "What is your favorite horror/thriller movie? "
A1 = input(Q1)
print("Unser claims " + A1 + " is the best horror/thriller movie")

Q2 = "What is your favorite sci-fi movie? "
A2 = input(Q2)
print("Unser claims " + A2 + " is the best sci-fi movie")

Q3 = "What is the best movie of all time? "
A3 = input(Q3)
print("Unser claims " + A3 + " is the best movie OF ALL TIME!")

Q4 = "What would they rate it from 1-10? "
A4 = float(input(Q4))
A4 = 10 - A4
AP1 = "They rate it a "
AP2 = " out of 10"
print(AP1 , A4 , AP2)
