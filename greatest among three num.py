# program to find greatest among three numbers#

f_num=int(input("enter the first number:"))
s_num=int(input("enter the second number:"))
t_num=int(input("enter the third number:"))
if(f_num > s_num)and(f_num > t_num):
    print("the greatest number is",f_num)

elif(s_num > f_num)and(s_num > t_num):
    print("the greatest nuumber is",s_num)

else:
    print("the greatest number is",t_num)
