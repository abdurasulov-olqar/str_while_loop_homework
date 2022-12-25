def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    lowerLetters = 0

    while len(s)>i:
        lowerLetters += s[i].islower()
        i += 1
    return lowerLetters