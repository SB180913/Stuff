"""
Sophia Babayev, Section 10
pig latin agian
"""

my_string = input()
my_string = my_string.lower()
words = my_string.split()

new_sentence = []
for word in words:
    new_word = word[1:] + word[0] + "ay"
    new_sentence.append(new_word)

print(" ".join(new_sentence))
