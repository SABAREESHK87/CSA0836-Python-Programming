def counter(k):
    cnt=0
    a=len(k)
    for i in range(a):
        for j in range(i+1,a):
            if k[i]==k[j]:
                cnt+=1
                if k[i]<k[j]:
                    cnt+=1
    print("NO OF GOOD PAIRS:",cnt)

flame=[]
f=int(input("enter the limit:"))
for i in range(0,f):
    j=int(input("enter element:"))
    flame.append(j)
print(flame)
print(counter(flame))

            
