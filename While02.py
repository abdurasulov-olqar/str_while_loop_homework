def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    let = 0

    while i < len(s):
        let += s[i].isalpha()
        i += 1
    return let