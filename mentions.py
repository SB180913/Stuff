"""
Sophia Babayev, Section 10
Prints and return unique usernames and hashtags from the text
"""


def mentions(the_text):
    usernames = []
    hashtags = []

    for word in the_text.split():
        if word.startswith("@") and len(word) > 1:
            username = word[1:]
            if username not in usernames:
                usernames.append(username)
        elif word.startswith("#") and len(word) > 1:
            hashtag = word[1:]
            if hashtag not in hashtags:
                hashtags.append(hashtag)

    print(usernames)
    print(hashtags)
    return [usernames, hashtags]


if __name__ == "__main__":
    line = input()
    while line != "":
        mentions(line)
        line = input()
