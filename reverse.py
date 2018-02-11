def reverse(x):
        s = str(x)
        if s[0] == '-':
            s1 = s[:0:-1]
            reverse1=-int(s1)
            if reverse1>2147483648 or reverse1<-2147483648:  #checking for 32 bit signed integer range
                return 0
            else:
                return reverse1
        else:
            s1 = s[::-1]
            reverse1= int(s1)
            if reverse1>2147483648 or reverse1<-2147483648:     #checking for 32 bit signed integer range
                return 0
            else:
                return reverse1




