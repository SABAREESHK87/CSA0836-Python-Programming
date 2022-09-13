def stair(k):
    if(k<=1):
        return k
    
    return stair(k-1)+stair(k-2)

def count(a):
    return stair(a+1)

d=int(input("enter the stair case limit:"))
print("number of ways to climb the stair case is:",count(d))
