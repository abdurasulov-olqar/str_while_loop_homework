def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    digits = 0
    while i<len(s):
        digits += s[i].isdigit()
        i += 1
    return digits

