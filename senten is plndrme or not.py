def ispalindrome(a):
    r=a.replace(' ','')
    r=r.lower()
    r1=r[::-1]
    return True if r==r1 else False

s=str(input("eenter the sentence:"))
if(ispalindrome(s)):
    print("The sentence is palindrome")
else:
    print("The sentence is  not a palindrome")
