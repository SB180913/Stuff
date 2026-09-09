"""
Sophia Babayev, Section 10
Find out weather the input number is divisable by 6 or 10 or both.
"""
num = int(input())
if num % 6 == 0 and num % 10 == 0:
    print("JupiterFizzBuzz")
elif num % 6 == 0:
    print("Fizz")
elif num % 10 == 0:
    print("Buzz")
else:
    print(num)