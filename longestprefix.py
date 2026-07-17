#Write a function to find the longest common prefix among an array of strings.
def longestCommonPrefix(strs):
    if not strs:
        return ""

    strs.sort()

    first = strs[0]
    last = strs[-1]

    i = 0

    while i < len(first) and i < len(last):

        if first[i] != last[i]:
            break

        i += 1

    return first[:i]


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))