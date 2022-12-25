def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    oddDigitsSum = 0

    while len(s)>i:
        if int(s[i])%2 == 1:
            oddDigitsSum += int(s[i])
        i += 1
    return oddDigitsSum