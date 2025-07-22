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
# rows=int(input("Enter the number of rows"))
# num=1
# for i in range(1,rows+1):
#   if(i%2==1):
#     for j in range(1,i+1):
#       print(num,end=" ")
#       if(j<i):
#         print("*",end=" ")
#       num=num+1
#   else:
#      temp=num+i-1
#      for j in range(1,i+1):
#       print(temp,end=" ")
#       if(j<i):
#         print("*",end=" ")
#       temp=temp-1
#       num=num+1
#   print()



# 16/07/2025
# to print the 3d list 
# a=[[[11,22,33],[44,55,66],[77,12,32]],[[41,42,43],[52,54,56],[98,97,95]]]
# for i in range(2):
#     for j in range(3):
#         for k in range(3):
#             print(a[i][j][k],end=" ")
#         print()
#     print()

# grid 
# grid=[[" " for i in range(10)]for i in range(10)]
# for i in range(10):
#     for j in range(10):
#         if(j==0 or j==9):
#             grid[i][j]="*"
#         if(i==j and i<5):
#             grid[i][j]="*"
#         if(i+j==8 and i<5):
#             grid[i][j]="*"
# for i in range(10):
#     for j in range(10):
#         print(grid[i][j],end=" ")
#     print()

# need to get 5 names from user and 3 subjects marks from 1 student and display their names with percentage in the format of
# import time
# names=[] 
# marks=[]   
# for i in range(5):
#     n=input("Enter the name{}".format(i+1))
#     names.append(n)
#     student=[]
#     for j in range(3):
#         m=int(input("Enter mark {}: " .format(j+1)))
#         student.append(m)
#     marks.append(student)
    
# per=[]
# for i in marks:
#     res=sum(i)//3
#     per.append(res)

# time.sleep(3)
# print("-------------")
# for i in range(5):
    # print("{}.{} : {}".format(i+1,names[i],per[i]))
        #   or
# names=[]
# sub=[]
# per=[]
# for i in range(5):
#     a=input(f"Name {i+1}:")
#     names.append(a)
#     tot=0
#     p=0
#     for j in range(3):
#         b=int(input(f"sub {j+1} mark:"))
#         sub.append(b)
#         tot=tot+b
#     p=tot//3
#     per.append(p)
# print("----------------")
# for i in range(5): 
#     print(f"{i+1}. {names[i]} : {per[i]}%")
# print()


# MATCH (MAPPING)
# n=int(input("enter the number of teams"))
# teams=[]
# for i in range(n):
#     t=input("enter the team names:")
#     teams.append(t)
# meet=int(input("enter the number of meeting"))
# match=[]
# for i in range(n-1):
#     for j in range(i+1,n):
#         for k in range(meet):
#             match.append([teams[i],teams[j]])
# index=1
# for i in match:
#     print("{} vs {}".format(i[0],i[1]))


# sort based on criteria
# a=[10,11,"Zakir","Bala",123,44,53,"Anuj",20,46,7,"Jack"]
# even=[]
# odd=[]
# alpha=[]
# for i in a:
#     if(type(i)==str):
#         alpha.append(i)
#     elif(i%2!=0):
#         odd.append(i)
#     elif(i%2==0):
#         even.append(i)
# odd.sort()
# even.sort()
# alpha.sort()   
# print(odd+even+alpha)


# the students with score greater than 5 and not in notorius gang 
# notorious=["DHARSHAN","ANUJ","ROHIT"]
# names=["ANU","DHARSHAN","ROHIT","JACK","PRIYA","BALA","RAI","RAM","RAJ","BEN"]
# score=[2,5,6,8,3,5,6,9,8,2]
# for i in range(len(names)):
#     if score[i]>5:
#         if names[i] not in notorious:
#             print(names[i])
            #  OR
# notorious=["DHARSHAN","ANUJ","ROHIT"]
# names=["ANU","DHARSHAN","ROHIT","JACK","PRIYA","BALA","RAI","RAM","RAJ","BEN"]
# score=[2,5,6,8,3,5,6,9,8,2]
# for i in range(len(names)):
#     if(names[i] not in notorious and score[i]>5 ):
#         print(names[i])


# average of numbers in list , max mark is 100
# a=[23,129,45,200,45,34,27,77,88,127]
# for i in a:
#     if(i>100):
#         a.remove(i)
# print(sum(a)/len(a))
        
# FLAMES
# boy=input("Enter the name of a boy")
# girl=input("enter the name of the girl")
# a1=list(boy)
# a2=list(girl)
# for i in range(len(a1)):
#     for j in range(len(a2)):
#         if(a1[i]==a2[j]):
#             a1[i]='2'
#             a2[j]='2'
# count=0
# for i in a1: 
#     if (i!='2'):
#         count=count+1
# for i in a2:
#     if(i!='2'):
#         count=count+1
# print(count)
# ans=['F','L','A','M','E','S']
# index=0
# while(len(ans)!=1):
#     index=(index+(count-1))%len(ans)
#     ans.pop(index)
# print("The relation is",ans[0])
   

# computer  game
# import random
# name1=input("Enter the name of player 1")
# name2=input("Enter the name of player 2")
# print("Computer has fixed five numbers from the range 1 to 100")
# print("You guys have to guess it.Ready???")
# nums=[]
# while(len(nums)!=5):
#     d=random.randint(1,10)
#     nums.append(d)
# print("*********************")
# s1=0
# s2=0
# player1=[]
# player2=[]
# for i in range(3):
#     print("Dear {} , enter your choice".format(name1))
#     ch=int(input())
#     player1.append(ch)
#     if(ch in nums):
#         print("CORRECT")
#         s1=s1+1
#     else:
#         print("WRONG")
#     print("Dear {} , enter your choice".format(name2))
#     ch=int(input())
#     player2.append(ch)
#     if(ch in nums):
#         print("CORRECT")
#         s2=s2+1
#     else:
#         print("WRONG")
# print("numbers decided by comp {}".format(nums))
# print("numbers guessed by {} : {}".format(name1,player1))
# print("numbers guessed by {} : {}".format(name2,player2))
# print("s1: {}".format(s1))
# print("s2: {}".format(s2))
# if(s1>s2):
#     print("Player1 is winner")
# else:
#     print("player 2")



    
    
# name1 = input("Enter name ")
# name2 = input("Enter name")
# player1 = []
# player2 = []
# s1 = 0
# s2 = 0
# nums = []
# while(len(nums)!=5):
#     d=random.randint(1,10)
#     nums.append(d)

# for i in range(3):
#     ch = input("Enter choice player1")
#     if ch in nums:
#         s1 += 1
#         print("CORRECT")
#         player1.append(ch)
#     else:
#         print("WRONG")
#     while(ch in player1 or ch in player2):
#         ch = input("Already done retry: ")
        
#     ch = input("Enter choice player2")
#     if ch in nums:
#         s2 += 1
#         print("CORRECT")
#         player2.append(ch)
#     else:
#         print("WRONG")
#     while(ch in player1 or ch in player2):
#         ch = input("Already done retry: ")
        
# if s1>s2:
#     print("")


# greed
# coins=[500,200,100,50,20,10,5,2,1]
# amount=int(input("Enter amount in rupees"))
# for i in coins:
#     while(amount>=i):
#         print(i,end=" ")
#         amount=amount-i
        



# 17.05.2025  

# to get the sum of max and min digits of the input
# a=int(input("enter number"))
# b=int(input("enter number"))
# l1=[int(i) for i in str(a)]
# l2=[int(i) for i in str(b)]
# r1=max(l1)+max(l2)
# r2=min(l1)+min(l2)
# print(r1+r2)


# names=["a","b","c","d"]
# marks=[20,40,50,60]
# res=list(zip(names,marks))
# print(res)


# names=["a","b","c","d"]
# marks=[100,45,32,67]
# res=list(zip(names,marks))
# q=sorted(res,key=lambda x:x[1])
# print(q)


# firing employees
# names=["A","B","C","D","E","F","G","H","I","J"]
# memo=[0,1,1,1,2,2,1,2,1,2]
# salary=[1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]
# l=[]
# res=list(zip(names,memo,salary))
# for i in res:  
#     if i[2]>4000:
#        res.remove(i)
#        l.append(i)
# print(l)
# s=sorted(res)
# print(res)
# for j in res:
#     if j[1]>1:
#         l.append(j)
#         res.remove(j)
# print(l)
# index=1
# for i in l:
#     print("{}.Name:{} salary :{}  memo:{}".format(index,i[0],i[2],i[1]))
#     index=index+1
    
    
    
# sirs code for firing 
# names=["A","B","C","D","E","F","G","H","I","J"]
# memo=[0,1,1,1,2,2,1,2,1,2]
# salary=[1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]
# data=list(zip(salary,memo,names))
# removed1=[]
# removed2=[]
# for i in data:
#   if(i[0]>4000):
#     removed1.append(i)
# remaining=[i for i in data if i[0]<4000]    
# a=sorted(remaining,key=lambda x:x[0],reverse=True)
# index=0
# for i in a:
#   if(i[1]>=2):
#     removed2.append(i)
#   if(len(removed2)>3):
#     break
# final=removed1+removed2
# for i in final:
#   print("{}.{} : Memo{}:salary {}".format(index,i[2],i[1],i[0]))
#   index=index+1



# to search for the missing element 
# a=[1,3,7,6,2,4,5,9]
# find the sum and subtract 

# compressed form of string 
# a="aaabbcccccaa"
# c=1
# res=""
# for i in range(len(a)):
#     if(i+1<len(a) and (a[i]==a[i+1])):
#         c=c+1
#     else:
#         res=res+a[i]
#         res=res+str(c)
#         c=1
# print(res)


# to calculate the percentage and print the rank 
# students = [
#     {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
#     {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
#     {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
#     {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
#     {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
# ]
# for i in students:
#     sum1=sum(i["marks"])
#     per=sum1//3
#     i["per"]=per
# des=["FIRST","SECOND","THIRD","FOURTH","FIFTH"]
# b=sorted(students,key=lambda x:x["per"], reverse=True)
# index=1
# for i in b:
#      print("{}. {} stands {} : {}".format(index,i["name"],des[index-1],i["per"]))
#      index=index+1


# from datetime import datetime
# a=input("Enter first date (YYYY -MM-DD):")
# b=input("Enter first date (YYYY -MM-DD)")
# d1=datetime.strptime(a,"%Y-%m-%d")
# d2=datetime.strptime(b,"%Y-%m-%d")
# diff=d2-d1
# print("Difference:", abs(diff.days),"days")


# from datetime import datetime
# import pytz
# a='Asia/Kolkata'
# tz=pytz.timezone(a)
# b=datetime.now(tz)
# print(b)

# from datetime import datetime
# import pytz
# for i in pytz.all_timezones:
#     print(i)

# to print the calender 
# import calendar
# print(calendar.calendar(2025))


    #  18.07.2025
    
# dict={'A':1,'B':10,'C':100,'D':1000,'E':10000,'F':100000}
# ip="ABCFDAABC"
# res=0
# for i in ip:
#     if(i in dict):
#         res=res+dict[i]
# print(res)


# Shapes
# def circle():
#     r=int(input("enter the radius of the circle"))
#     print("the area of circle is",3.14*r*r)
# def square(s):
#     print("the area of square is ",s*s)
# def triangle():
#     b=int(input("enter the base"))
#     h=int(input("enter the height"))
#     return 0.5*b*h
# def rectangle(l,br):
#     return l*br
# a=1
# while(a>0):
#     print("1 Circle")
#     print("2 Square")
#     print("3 Triangle")
#     print("4 Rectangle")
#     print("5 EXIT")
#     a=int(input("enter your choice"))
#     match a:
#         case 1:
#             circle() 
#         case 2:
#             s=int(input("enter the side"))
#             square(s)
#         case 3:
#             tri=triangle()
#             print("the area of triangle is ",tri)
#         case 4:
#             l=int(input("enter the length"))
#             br=int(input("enter the breadth"))
#             rec=rectangle(l,br)
#             print("the area of rectangle is ",rec)
#         case 5:
#             exit ()


# to print coprime triplets
# def cop(a , b):
#     return gcd(a,b)==1
# def gcd(a,b):
#     while(b!=0):
#        temp=a%b
#        a=b
#        b=temp
#     return a    
# n=int(input("enter the range"))
# for i in range(1,n):
#     for j in range(1,i):
#         for k in range(1,j):
#             if(k*k+j*j==i*i and cop(i,j) and cop(j,k) and cop(i,k)):
#                 print(i,j,k)
 
            
# 3 digit prime numbers

# def numprime(i):
#     if(i==1):
#         return False
#     for j in range(2,i): 
#         if(i%j==0):
#             return False
#     return True
        
# def sumprime(i):
#     d=list(str(i))
#     x=sum([int (i) for i in d])
#     return numprime(x)
# def digprime(i):
#     while(i>0):
#         d=i%10
#         if(not numprime(d)):
#             return False
#         i=i//10
#     return True     
# for i in range(100,1000):
#     if(numprime(i) and sumprime(i) and digprime(i)):
#         print(i,end=" ") 




            
# bank
# def deposit(amt,ch,Account):   
#     Account[ch]+=amt
#     print("the amount {} is deposited to account number {}".format(amt,ch)) 
# def transfer(t_amt,t_acc):
#     if Account[ch]<t_amt:
#         print("No money")
#     else:   
#         Account[ch]-=t_amt
#         Account[ch]+=t_amt 
#     print("Amout {} trnasferred to { } from {}".format(t_amt,t_acc,Account_[ch]))
# Account={101:1000,102:2000,103:3000}
# ch=int(input("enter your account number"))
# while(True):
#     if(ch not in Account):
#         print("Account not found")
#     else:
#         print("----BANK ACCOUNT DETAILS------")
#         print("1 CHECK BALANCE")
#         print("2 DEPOSIT ")
#         print("3 TRANSFER")
#         print("4 WITHDRAW")
#         print("5 LOGOUT")
#         a=int(input("Enter the choice"))
#         match a:
#             case 1:
#                 print("balance is",Account[ch])
#             case 2:
#                 amt=int(input("enter the amount"))
#                 deposit(amt,ch,Account)
                
#             case 3:
#                 t_acc=int(input("enter the account number to transfer"))
#                 if(t_acc not in Account):
#                     print("Cant proceed , no acc ")
#                 else:
#                     t_amt=int(input("Enter the amount to transfer"))
#                     transfer(t_acc,t_amt)
#             case 4:
#                 w_amt=int(input("Enter the amount to withdraw"))
             
            
            
# from tabulate import tabulate
# headers = ["Name","Age","Department"]
# data =[
#     ["Ravi",25,"HR"],
#     ["Anjali",30,"Finance"],
#     ["Mohan",28,"IT"],
#     ["Sneha",24,"HR"],
#     ["Arun",32,"Logistics"]
# ]
# print(tabulate(data,headers=headers,tablefmt="fancy_grid"))

    
    
# headers = ["Name","Age","Department"]
# data =[
#     ["Ravi",25,"HR"],
#     ["Anjali",30,"Finance"],
#     ["Mohan",28,"IT"],
#     ["Sneha",24,"HR"],
#     ["Arun",32,"Logistics"]
# ]   
# print(f"{headers[0]:<12}{headers[2]:<15}") 
# print("*" * 30)
# for row in data:
#     print(f"{row[0]:<12}{row[1]:<5}{row[2]:<15}")
#     print("-" * 30)


# 19.07.2025

# Ishita is a curious girl and one day she decides to check whether a number is prime or not. so she wants to write an algorithm 
# to determine  if a number N is round or not. A round number is a number defined by the following process:
#     -First starting with any positive integer,replace the number by the sum of the squares of its digits.
#     -Repeat the process until the number equals 1(where it will stay),or it loops endlessly in a cycle which does not include 1
#     -Those numbers for which this process ends in 1 are round numbers.
#     Return true if N is a rounded number false is not.
    
    
# n=int(input("Enter any number"))
# l=[]
# while(n not in l):
#     l.append(n)
#     n=sum([int (i)* int(i) for i in str(n)])
# if(n==1):
#     print("ROUND NUMBER")
# else:
#     print("Not")



# spiral
# matrix=[[1,2,3,4],
#         [5,6,7,8],
#         [9,1,2,3],
#         [4,5,6,7],
#         [8,9,10,11]]
# cols=len(matrix[0])
# rows=len(matrix)
# left=0
# top=0
# right=cols-1
# bottom=rows-1
# while(top<=bottom and left<=right):
    
#     for i in range(left,right+1):
#         print(matrix[top][i],end=" ")
#     top=top+1
    
    
#     for i in range(top,bottom+1):
#         print(matrix[i][right],end=" ")
#     right=right-1
    
   
    
#     for i in range(right,left-1,-1):
#         print(matrix[bottom][i],end=" ")
#     bottom=bottom-1
    
    
#     for i in range(bottom,top-1,-1):
#         print(matrix[i][left],end=" ")
#     left=left+1
   
    
    # this code works for 3*3 matrx also , whereas the previous one doesnt 
# matrix=[[1,2,3,4],
#         [5,6,7,8],
#         [9,1,2,3],
#         [4,5,6,7],
#         [8,9,10,11]]
# cols=len(matrix[0])
# rows=len(matrix)
# left=0
# top=0
# right=cols-1
# bottom=rows-1
# while(top<=bottom and left<=right):
    
#     for i in range(left,right+1):
#         print(matrix[top][i],end=" ")
#     top=top+1
    
    
#     for i in range(top,bottom+1):
#         print(matrix[i][right],end=" ")
#     right=right-1
    
#     if(top<=bottom):
#         for i in range(right,left-1,-1):
#              print(matrix[bottom][i],end=" ")
#         bottom=bottom-1

#     if(left<=right):
#         for i in range(bottom,top-1,-1):
#              print(matrix[i][left],end=" ")
#         left=left+1
   
    
    
    # 21.07.2025
    # prime factorization
    
# def factor(n):
    
#     for i in range(2,n+1):
#         if(n%i==0):
#             print(i)
#             factor(n//i)
#             break
    
# n=int(input("enter the number"))
# factor(n)
    # OR
# def factor(n):
#     if n==1:
#         return
#     i=2
#     while(n%i!=0):
#         i=i+1
#     print(i,end=" ")
#     factor(n//i)
# n=int(input("enter the number"))
# factor(n)


# FACTORIAL 
# def fact(n):
#     if(n<=1):
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter the number"))
# print(fact(n))

# NQUEENS
# def print_board(board):
#     for row in board:
#         print(" ".join(row))
#     print()
# def safe(board,row,col,n):
#     for i in range(row):
#         if board[i][col]=="Q":
#             return False
#     i=row-1
#     j=col-1
#     while (i>=0 and j>=0):
#         if(board[i][j]=="Q"):
#             return False
#         i=i-1
#         j=j-1
    
#     i=row-1
#     j=col+1
#     while i>=0 and j<n:
#         if(board[i][j]=="Q"):
#             return False
#         i=i-1
#         j=j+1
        
#     return True   
    
    
# def solve(board,row,n):
#     if row==n:
#         print_board(board)
#         return 
#     for col in range(n):
#         if (safe(board,row,col,n)):
#             board[row][col]="Q"
#             solve(board,row+1,n)
#             board[row][col]="."      

# n=4
# board=[["." for _ in range(n)]for _ in range(n)]
# solve(board,0,n)


# TOWER OF HANOII
# def tower(disk,source,auxi,dest):
#     if(disk==1):
#         print("move {} from {} to {}".format(disk,source,dest))
#         return
#     else:
#         tower(disk-1,source,dest,auxi)
#         print("move {} from {} to {}".format(disk,source,dest))
#         tower(disk-1,auxi,source,dest)

# disk=int(input("Enter any number: "))
# print("Steps involved are")
# tower(disk,'A','B','C')


# Fibonacci
# def fibo(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# a=int(input("enter any number"))
# for i in range(a):
#     print(fibo(i),end=" ")

# 22.7.2025
# classes and objects

# class Rectangle:
#     info1="*Sum of angle is 360 degree" 
#     info2="*Each angle is 90 degree"
#     def calculate(self):
#         length=int(input("Enter the length of rectagle"))
#         self.length=length
#         breadth=int(input("Enter the breadth of rectangle"))
#         self.breadth=breadth
#         Area=length*breadth
#         print("The area of the rectangle is {}".format(Area))
#         Perimeter=2*(length+breadth)
#         print("The perimeter of the rectangle is {}" .format(Perimeter))
# print(Rectangle.info1)
# print(Rectangle.info2)
# r1=Rectangle()
# r2=Rectangle()
# r1.calculate()
# r2.calculate()

# class rect:
#     prop1="Sum of angle is 360 degree"
#     prop2="Each angle is 90 degree"
#     def get_info(self):
#         a=int(input("enter the length of rectangle"))
#         b=int(input("enter the breadth"))
#         self.len=a
#         self.breadth=b
#     def area(self):
#         print(self.len*self.breadth)
#     def perimeter(self):
#         print((self.len+self.breadth)*2)
        
# print("The Rectangle Properties")
# print(rect.prop1)
# print(rect.prop2)
# a1=rect()
# a2=rect()
# a1.get_info()
# a2.get_info()
# a1.area()
# a1.perimeter()
# a2.area()
# a2.perimeter()
            
        
        # CONSTRUCTOR
        
# class india:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print("{} is good player" .format(self.name))

# a1=india("SACHIN")
# a1.name="RUCHI"
# a1.display()

#              LIST AND OOPS
# class rect:
#     def set_dim(self,a,b):
#         self.a=a
#         self.b=b
        
#     def area(self):
#         return self.a*self.b
# nums=[]

# d=int(input("Enter the number"))
# for i in range(d):
#     R=rect()
#     a=int(input("enter the length"))
#     b=int(input("enter the breadth"))
#     R.set_dim(a,b)
#     nums.append(R)
# index=0
# for  i in nums:
#       print("The area of {}: is {}" .format(index,i.area()))
#       index=index+1


# extra concepts 
# nums[9].area   = to print 10th rectangle area
# i.a  == to print the length of rectangles only
# if(i.area()%2==0):    ===to print the even areas only 
    # print(i.area())
# R=rect(random.randint(1,5).random.randint(5,10))
      
     
class rect:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def set_dim(self,a,b):
        self.a=a
        self.b=b     
    def area(self):
        return self.a*self.b
nums=[]
d=int(input("Enter the number"))
for i in range(d):
    R=rect(i+10,i+20)
    a=int(input("enter the length"))
    b=int(input("enter the breadth"))
    R.set_dim(a,b)
    nums.append(R)
index=0
for  i in nums:
      print("The area of {}: is {}" .format(index,i.area()))
      index=index+1
 
      
      
    