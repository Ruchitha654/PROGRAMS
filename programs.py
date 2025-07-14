# a=int(input("enter a number"))
# for i in range(1,11):
#     print("{} X {} = {}".format(i,a,i*a))


# sum of digits 
# a=int(input("enter the number"))
# digit=0
# while(a!=0):
#     digit+=a%10
#     a=a//10
# print(digit)
    
    
#enter the marks , if user is giving number >100 , dont consider, consider the marks below 100, take input till user is giving 0, consider the marks and find the total
# a=int(input("enter the number"))
# sum=0
# while(a!=0 and a<100):
#     sum+=a
#     a=int(input("enter the number"))
# print(sum)
    
    #OR
# sum=0
# while(True):
#     x=int(input("enter the numbers"))
#     if x<=100:
#         sum+=x
#     if x==0:
#         break
# print(sum)




a=10
for i in range(50):
    if(i%2==0 or i%3==0 or i%5==0 or i%7==0):
        continue
    print("hii")
    a=a+2
print(a)
    

#digital clock
# import time
# import sys
# h=12
# m=30
# s=0
# while True:
#     sys.stdout.write(f"\r{h:02d}:{m:02d}:{s:02d}")
#     sys.stdout.flush()
#     time.sleep(1)
#     s=s+1
#     if(s==60):
#         m=m+1
#         s=0
#     if(m==60):
#         h=h+1
#         m=0
#     if(h==13):
#         h=0
#         m=0  


    
#euclid's algorithm (GCD) 
# a=int(input("enter the value for a"))
# b=int(input("enter the value for b"))
# while(b!=0):
#     q=a//b
#     r=a%b
#     a=b
#     b=r
# print(a)
#inorder to find the gcd of 3 numbers, find the gcd of 2 numbers first then use the result with the third 



#LCM of 2 numbers
# a=int(input("enter the value for a"))
# b=int(input("enter the value for b"))
# m=max(a,b)
# step=m
# while(True):
#     if(m%a==0 and m%b==0):
#        lcm=m
#        break
#     #else:
#         #m=m+step
# print(lcm)
    


    
    
