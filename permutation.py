def permutation(s, i=0):
    if i== len(s):
        print("".join(s))
    for j in range(i, len(s)):
        kai=[c for c in s]
        kai[i], kai[j] = kai[j], kai[i]
   	 

        permutation(kai, i + 1)

a=str(input("enter the number:"))
print(".",permutation(a))
