
a=int(input("enter the number"))
sum=0
while(a!=0 and a<100):
    sum+=a
    a=int(input("enter the number"))
print(sum)
    
    #OR
sum=0
while(True):
    x=int(input("enter the numbers"))
    if x<=100:
        sum+=x
    if x==0:
        break
print(sum)