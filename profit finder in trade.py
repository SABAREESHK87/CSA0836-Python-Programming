def profit(pri,k):
    profit=[0]*k
    max_pri=pri[k-1]
    for i in range(k-2,0,-1):
        if(pri[i])>max_pri:
            max_pri=price[i]
        profit[i]=max(profit[i+1],max_pri-price[i])

    min_price=price[0]
    for k in range(1,k):
        if price[k]<min_price:
            min_price=price[k]
        profit[k]=max(profit[k-1],profit[k]+(price[k]-min_price))
    ans=profit[k-1]
    return ans


price=[]
a=int(input("enter the limit:"))
for i in range(0,a):
    b=int(input("enter the buy and sell price:"))
    price.append(b)
print(price)
print("max_profit is:",profit(price,len(price)))
