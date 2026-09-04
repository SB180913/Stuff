"""
Sophia Babayev, Section 10
Price Change
"""

old = float(input("What was the original price?"))
new = float(input("What is the new price?"))


my_result = int(round(((new - old)/old)*100))


print(f"Price changed by {my_result}%")
