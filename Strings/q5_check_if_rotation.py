# Uses KMP algorithm for string matching


def areRotations(s1, s2):
    return s1 in s2 + s2
