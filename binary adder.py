print("Enter First Binary Number: ")
a = int(input())
print("Enter Second Binary Number: ")
b = int(input())

a = str(a)
b = str(b)
c= int(a, 2) + int(b, 2)
d = bin(c)

print("Result = " , d)
