stock={"app":180,"TSLA":250,"google":400}
tot=0
n=int(input("Enter the number of stocks owned: "))
for x in range(0,n):
    market=input("Enter the enterprise name: " )
    if market in stock:
        
        quan=int(input("Enter the quantity: "))
        tot+=stock[market]*quan
    else:
        print("Invalid")
print(f"total investment is {tot}")

