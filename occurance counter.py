a=str(input("enter the string:"))
k=int(input("enter the occurance:"))

b=a
a.split()
b.split()
cnt=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[i]:
            cnt=1
        elif a[i]!=b[i]:
            cnt+=1
print(cnt)
            
