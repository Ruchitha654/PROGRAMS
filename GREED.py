coins=[500,200,100,50,20,10,5,2,1]
amount=int(input("Enter amount in rupees"))
for i in coins:
    while(amount>=i):
        print(i,end=" ")
        amount=amount-i
        