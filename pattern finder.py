import re
a = input("Enter the first string:")
b = input("Enter the second string:")
b = r"{}".format(a)
b = re.compile(a)
if b.fullmatch(a):
    print("True")
else:
    print("False")
