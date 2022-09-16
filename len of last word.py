def lenlastword(k):
    l=0
    b=k
    .strip()
    for i in range(len(b)):
        if b[i]==" ":
            l=0
        else:
            l+=1
    return l

j=str(input("enter the string:"))
print("the length of last word is:",lenlastword(j))
