a=str(input("enter the month:"))
b=int(input("enter the date:"))
if a ==('January','Febuary','March'):
    print("the season is winter")
elif a ==('April','May','June'):
    print("the season is summer")
elif a ==('July','August','September'):
    print("the season is spring")
else:
    print("the season is fall")

if(a=='March')and(b>19):
    print("the season is summer")
elif(a=='June')and(b>20):
    print("the season is spring")
elif(a=='September')and(b>21):
    print("the season is fall")
elif(a=='December')and(b>20):
    print("the seasson is winter")
    
