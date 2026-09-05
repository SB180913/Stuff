"""
Sophia Babayev, Section 10
Distance Formula
"""

x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

distance = float((((x2 - x1)**2)+((y2 - y1)**2))**.5)

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance}")