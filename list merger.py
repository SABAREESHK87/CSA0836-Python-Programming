l1=[]
l2=[]
l=[]
a=int(input("enter the limit of list1:"))
b=int(input("enter the limit of list2:"))
for i in range(0,a):
    c=int(input("enter element in list1:"))
    l1.append(c)
print(l1)
for j in range(0,b):
    d=int(input("enter the element in list2:"))
    l2.append(d)
print(l2)

l=l1+l2
l.sort()
print(l)
