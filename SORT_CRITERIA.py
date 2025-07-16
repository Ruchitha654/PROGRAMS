
a=[10,11,"Zakir","Bala",123,44,53,"Anuj",20,46,7,"Jack"]
even=[]
odd=[]
alpha=[]
for i in a:
    if(type(i)==str):
        alpha.append(i)
    elif(i%2!=0):
        odd.append(i)
    elif(i%2==0):
        even.append(i)
odd.sort()
even.sort()
alpha.sort()   
print(odd+even+alpha)
