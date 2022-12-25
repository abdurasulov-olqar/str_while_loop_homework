import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    punc = 0

    while len(s)>i:
        if s[i] in string.punctuation:
            punc += 1
        i += 1
    return punc 

print(main('11!!@#09hdfjh'))