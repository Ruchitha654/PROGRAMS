def factor(n):
    for i in range(2,n+1):
        if(n%i==0):
            print(i)
            factor(n//i)
            break 
n=int(input("enter the number"))
factor(n)
      
      
    #   OR 

def factor(n):
    if n==1:
        return
    i=2
    while(n%i!=0):
        i=i+1
    print(i,end=" ")
    factor(n//i)
n=int(input("enter the number"))
factor(n)

