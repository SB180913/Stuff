"""
Sophia Babayev, Section 10
Checks if there are any duplicate letters in the input
"""


def dupedetector():
    while True:
        text = input()

        if text == "done":
            break 

        if len(text) != len(set(text)):
            print("dupes")
        else:
            print("no dupes")


if __name__ == '__main__':
    dupedetector()