def val(a):
    if(a=='I'):
        return 1
    if(a=='V'):
        return 5
    if(a=='X'):
        return 10
    if(a=='L'):
        return 50
    if(a=='C'):
        return 100
    if(a=='D'):
        return 500
    if(a=='M'):
        return 1000
    else:
        return -1
def rtod(s):
    r=0
    i=0
    while(i<len(s)):
        s1=val(s[i])
        if(i+1<len(s)):
            s2=val(s[i+1])
            if(s1>=s2):
                r=r+s1
                i=i+1
            else:
                r=r+s2-s1
                i=i+2
        else:
            r=r+s1
            i=i+1
    return r

a=str(input("ENTER THE ROMAN NUMERALS:"))
print("THE DECIMAL NUMBER IS:",rtod(a))
