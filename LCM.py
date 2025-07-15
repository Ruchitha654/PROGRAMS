a=int(input("enter the value for a"))
b=int(input("enter the value for b"))
m=max(a,b)
step=m
while(True):
    if(m%a==0 and m%b==0):
       lcm=m
       break
    else:
        m=m+step
print(lcm)