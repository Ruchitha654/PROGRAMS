a=int(input("enter the number"))
digit=0
while(a!=0):
    digit+=a%10
    a=a//10
print(digit)
    