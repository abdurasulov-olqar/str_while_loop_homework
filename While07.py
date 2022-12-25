def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    evenDigits = 0

    while len(s)>i:
        if int(s[i])%2 == 0:
            evenDigits += 1
        i += 1
    return evenDigits