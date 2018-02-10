from itertools import permutations
def lengthOfLongestSubstring(s):
    perms = []
    list=[]
    dict={'char':0,'freq':0}
    for i in range(1, len(s) + 1):
        for c in permutations(s, i):
            perms.append("".join(c))
    for j in range(len(perms)):
        if perms[j] in s:
            list.append(perms[j])
    for each in list:
        dict['char']=set(each)
        dict['freq']=len(each)
    max = -float('inf')
    for val in dict.itervalues():
        if val > max:
            max = val
    print len(max)



lengthOfLongestSubstring("abcab") # calling to function to check
