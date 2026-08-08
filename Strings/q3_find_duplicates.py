# Given a string s, the task is to identify all characters that appear more than once and print each as a list containing the character and its count.


def method_1(s):
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1
    duplicates = [[char, count] for char, count in char_count.items() if count > 1]
    return duplicates


def method_2(s):
    s = list(sorted(s))
    duplicates = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        if count > 1:
            duplicates.append([s[i], count])
        i += 1
    return duplicates
