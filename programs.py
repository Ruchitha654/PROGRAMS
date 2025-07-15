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




# a=10
# for i in range(50):
#     if(i%2==0 or i%3==0 or i%5==0 or i%7==0):
#         continue
#     print("hii")
#     a=a+2
# print(a)
    

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
#  
#        m=m+step
# print(lcm)
# a=int(input("enter the value for a"))
# b=int(input("enter the value for b"))
# m=max(a,b)
# step=m
# while(True):
#     if(m%a==0 and m%b==0):
#        lcm=m
#        break
#     else:
#         m=m+step
# print(lcm)

    

# second largets number
# a=int(input("Enter num1"))
# b=int(input("Enter num2"))
# c=int(input("Enter num3"))
# if(a>=b and a<=c):
#     print(a)
# elif(b>=a and b<=c):
#     print(b)
# else:
#     print(c)
    
    
# prime number
# a=int(input("enter any number"))
# c=0
# for i in range(2,a):
#     if(a%i==0):
#         c=c+1
# if(c==0):
#     print("Its a prime number")
# else:
#     print("its a composite number")

# pattern
# for i in range(10):
#     print("*",end=" ")
# print( )
# for i in range(10):
#     print("*                 *")
# for i in range(10):
#     print("*",end=" ")


# 15-07-2025
# a=input("enter the passwword")
# up=0
# lw=0
# sp=0
# dg=0
# if(len(a)>7):
#     for i in a:
#         if(i.isupper()):
#             up=up+1
#         elif(i.islower()):
#             lw=lw+1
#         elif(i.isdigit()):
#             dg=dg+1
#         else:
#             sp=sp+1
#     if(up>0 and lw>0 and dg>0 and sp>0):
#         print("it is a good password")
#     else:
#         print("not a good password")
# else:
#     print("bad password as the characters arent enough")


# try the code for removing the continus characters , as characters must no be backtoback

# ANARGAM  (if sorted strigs are equal)
# a="cdfkjgicdfgr"       this is for ascending order
# b=sorted(a)
# print(b)


# a="abcdefghijklmna"
# b=sorted(a,reverse=True)
# print(b)


# final code of anargam
# str1=input("Enter the string1")
# str2=input("Enter the second string")
# a=str1.lower()
# b=str2.lower()
# a1="".join(i for i in a if i!=" ")
# b1="".join(i for i in b if i!=" ")
# a2=sorted(a1)
# b2=sorted(b1)
# if( a2==b2):
#     print("Anargam")
# else:
#     print("not Anargam")


#counting the number of words in a sentence 
# str1=input("enter the sentence")
# count=0
# for i in range(len(str1)):
#     if (str1[i]==" " and str1[i+1]!=" "):
#         count=count+1
# print(count+1)


# to print star pattern 
# a=int(input("enter the number of rows"))
# for i in range(a):
#     for i in range(i+1):
#         print("*",end=" ")
#     print()

# to print the above pattern in reverse order
# a=int(input("enter the number of rows"))
# for i in range(a):
#     for i in range(a-i):
#         print("*",end=" ")
#     print()
    
    
# assignment make triangle pattern
# a=int(input("enter the number of rows"))

# b=int(input("enter the number of blocks"))
# l=int(input("enter the number of lines"))
# s=int(input("enter te number of stars"))
# sum=0
# for k in range(b):
#     print(f"-------------BLOCK{k+1}------------")
#     count=0
#     for i in range(l-k):
#         for j in range(s): 
#           print("*",end=" ")
#           count=count+1
#         print()
#     print(count)
#     sum+=count
# print(f"Total:{sum}")

#        OR

# b=int(input("enter the number of blocks"))
# l=int(input("enter the number of lines"))
# s=int(input("enter te number of stars"))
# sum=0
# for i in range(b):
#     print(f"-------------BLOCK{i+1}------------")
#     for i in  range(l):
#         for j in range(s): 
#           print("*",end=" ")
#         print()
#     sum=sum+(l*s)
#     print(l*s)
#     l=l-1
# print(f"total number of stars={sum}")

# given total number of heads and total number of legs of a group of hens and cows
# each hen has 1 head and 2 legs
# each cow has 1 head and 4 legs
# write a program to determine the number of hens and cows
# if no valid combination is possible tell that no solution exists 
# h=int(input("enter the total number of heads"))
# l=int(input("enter the total number of legs"))
# flag=False
# for hen in range(h):
#     cow=h-hen
#     if(cow*4 + hen*2 ==l):
#         print("COWS: ",cow)
#         print("HENS: ",hen)
#         flag=True
#         break
# if(not flag):
#     print("NO SOLUTION")


# print  50 possible 3 digit prime numbers that is possibly least

# count=0
# for i in range(100,1000):
#     c=0
#     for j in range(2,i):
#         if(i%j==0):
#             c=c+1
#     if(c==0):
#         count=count+1
#         if(count<20):
#             print(i,end= " ")
    


# print  50 possible 3 digit prime numbers that is possibly greatest

# count=0
# for i in range(1000,100,-1):
#     c=0
#     for j in range(2,i):
#         if(i%j==0):
#             c=c+1
#     if(c==0):
#         count=count+1
#         if(count<20):
#             print(i,end= " ")
    
# tcs sum 
rows=int(input("enter the rows"))     
num=1
for i in range(1,rows+1):
    if(i%2==1):
        for j in range(i):
            print(num,end= " ")
            num=num+1
        print()
    else:
        temp=num+i-1
        for j in range(1,i+1):
            print(temp,end=" ")
            if j<i:
               print("*",end=" ")
            temp=temp-1
            num=num+1
        print()
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    



