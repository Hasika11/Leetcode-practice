def longestPalindrome(x):
    from itertools import combinations
    if isPalindrome(x)==True:
        return x
    results = [''.join(x[i:j]) for i, j in combinations(range(len(x) + 1), 2)]
    pal=[]
    for each in results:
        if isPalindrome(each)== True:
             pal.append(each)
    return max(pal,key=len)

def isPalindrome(x):
   # s = str(x)
    s1 = x[::-1]
    reverse1 = s1
    if reverse1 == x:
        return True
    else:
        return False
