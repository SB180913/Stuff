"""
Sophia Babayev, Section 10
Fixes the misspeled words by checking the first letter typed in each word that is in the list.
"""

word_list = ["algorithm", "we", "compile", "dog", "ethernet", "fetch", "grit", "have", "internet", "kernel", "build"]

while True:
    text = input()
    
    if text == "done":
        break  
        
    corrected_words = []
    for word in text.split(" "):
        if word in word_list:
            corrected_words.append(word)
            continue

        replacement = next((candidate for candidate in word_list if candidate[0] == word[0]), word)
        corrected_words.append(replacement)

    print(" ".join(corrected_words))

