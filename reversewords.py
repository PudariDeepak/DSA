#Given a string s, reverse the order of the words.
def reverseWords(s):
    words = []
    word = ""

    for ch in s:
        if ch != " ":
            word += ch
        elif word:
            words.append(word)
            word = ""

    if word:
        words.append(word)

    result = ""

    for i in range(len(words) - 1, -1, -1):
        result += words[i]

        if i != 0:
            result += " "

    return result


s = "  Deepak is good boy   "
print(reverseWords(s))