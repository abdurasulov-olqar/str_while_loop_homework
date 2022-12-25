def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    vorbls = "aeiouAEIOU"
    i= 0
    letters = 0
    while len(s)>i:
        if s[i] not in vorbls:
            letters += 1
        i += 1

    return letters

