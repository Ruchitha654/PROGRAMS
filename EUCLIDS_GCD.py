a=int(input("enter the value for a"))
b=int(input("enter the value for b"))
while(b!=0):
    q=a//b
    r=a%b
    a=b
    b=r
print(a)