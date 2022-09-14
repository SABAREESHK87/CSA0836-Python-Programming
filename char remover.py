def delchar(s,c):
    if(len(c)==1):
        for i in range(len(s)):
            if(c is not s[i]):
                print([s[i]],end="")
            else:
                continue
        
a=str(input("enter the string:"))
b=str(input("enter the character you want to delete on the sentence:"))
print(delchar(a,b))
                
    
