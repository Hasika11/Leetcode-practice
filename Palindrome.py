def isPalindrome(x):
    s = str(x)
    if s[0] == '-':
        return False
    if s[0]!='-':
        s1 = s[::-1]
        reverse1 = int(s1)
        if reverse1 > 2147483648 or reverse1 < -2147483648:  # checking for 32 bit signed integer range
            return False
        else:
            reverse1=int(s1)
        if reverse1 == x:
            return True
        else:
            return False

