# Given a string s, the task is to identify all characters that appear more than once and print each as a list containing the character and its count.

def printDuplicates(s):

    # Hash map to store frequency of each character
    freq = {}

    # Count frequency of each character
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # Traverse the map and print characters with count > 1
    for key in freq:
        if freq[key] > 1:
            print(["{}".format(key), freq[key]], end=", ")