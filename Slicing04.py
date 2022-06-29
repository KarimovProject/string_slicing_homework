def main(s,n):
    """
    The s string variable is given. return n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    if n>0:
        return s[:n]
    else:
        return "notog'ri qiymat kiritildi"
print(main("salom", 2))