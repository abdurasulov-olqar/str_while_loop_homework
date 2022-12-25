def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    upperLetters = 0

    while len(s)>i:
        upperLetters += s[i].isupper()
        i += 1 

    return upperLetters