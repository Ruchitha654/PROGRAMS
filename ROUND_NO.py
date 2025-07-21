# Ishita is a curious girl and one day she decides to check whether a number is prime or not. so she wants to write an algorithm 
# to determine  if a number N is round or not. A round number is a number defined by the following process:
#     -First starting with any positive integer,replace the number by the sum of the squares of its digits.
#     -Repeat the process until the number equals 1(where it will stay),or it loops endlessly in a cycle which does not include 1
#     -Those numbers for which this process ends in 1 are round numbers.
#     Return true if N is a rounded number false is not.


n=int(input("Enter any number"))
l=[]
while(n not in l):
    l.append(n)
    n=sum([int (i)* int(i) for i in str(n)])
if(n==1):
    print("ROUND NUMBER")
else:
    print("Not")