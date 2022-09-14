def count(n,s):
    if(n==0):
        return 1
    cnt=0
    for i in range(s,5):
        cnt+=count(n-1,i)
    return cnt
def vowels(n):
    
    return count(n,0)
    

f=int(input("enter the input:"))
print("the count of combination of vowels is:",vowels(f))
