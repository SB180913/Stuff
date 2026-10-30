"""
Sophia Babayev, Section 10
Prints a checkerboard of the requested size
"""

def checkerboard(size, symbol_1, symbol_2):
    for row in range(size):
        line = ""
        for column in range(size):
            if (row + column) % 2 == 0:
                line += symbol_1
            else:
                line += symbol_2
        print(line)


if __name__ == "__main__":
    size = int(input())
    symbols = input().split()
    checkerboard(size, symbols[0], symbols[1])