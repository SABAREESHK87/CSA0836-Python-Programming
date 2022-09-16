def minsqr(k):
    if(k<=3):
        return k/k
    r=k
    for i in range(1,k+1):
        t=i*i
        if t>k:
            break
        else:
            r=min(r,1+minsqr(k-t))
    return r

a=int(input("enter the input:"))
print("the perfect square is:",minsqr(a))
        
