K=str(input("enter the month and the first letter of month in capital:"))
S=int(input("enter the date:"))
if K in('January','Febuary','March'):
    print("the season is winter")
elif K in('April','May','June'):
    print("the season is summer")
elif K in('July','August','September'):
    print("the season is spring")
elif K in('October','November','December'):
    print("the season is fall")

if(K=='March')and(S>19):
    print("the season is summer")
elif(K=='June')and(S>20):
    print("the season is spring")
elif(K=='September')and(S>21):
    print("the season is fall")
elif(K=='December')and(S>20):
    print("the seasson is winter")
    
