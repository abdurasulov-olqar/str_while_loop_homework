def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    summa = 0
    
    while len(s)>i:
        summa += int(s[i])
        i += 1
    return summa