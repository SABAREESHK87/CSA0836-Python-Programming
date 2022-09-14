a=int(input("enter the number:"))
b=[]
for i in range(1,a):
    if(i%15==0):
        b.append("FIZZ BUZZ")
    elif(i%3==0):
        b.append("FIZZ")
    elif(i%5==0):
        b.append("BUZZ")
    else:
        b.append(i)
print(b)
