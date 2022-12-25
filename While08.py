def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    oddDigits = 0

    while len(s)>i:
        if int(s[i])%2 == 1:
            oddDigits += 1
        i += 1
    return oddDigits