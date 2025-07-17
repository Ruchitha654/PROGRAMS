import random
name1=input("Enter the name of player 1")
name2=input("Enter the name of player 2")
print("Computer has fixed five numbers from the range 1 to 100")
print("You guys have to guess it.Ready???")
nums=[]
while(len(nums)!=5):
    d=random.randint(1,10)
    nums.append(d)
print("*********************")
s1=0
s2=0
player1=[]
player2=[]
for i in range(3):
    print("Dear {} , enter your choice".format(name1))
    ch=int(input())
    player1.append(ch)
    if(ch in nums):
        print("CORRECT")
        s1=s1+1
    else:
        print("WRONG")
    print("Dear {} , enter your choice".format(name2))
    ch=int(input())
    player2.append(ch)
    if(ch in nums):
        print("CORRECT")
        s2=s2+1
    else:
        print("WRONG")
print("numbers decided by comp {}".format(nums))
print("numbers guessed by {} : {}".format(name1,player1))
print("numbers guessed by {} : {}".format(name2,player2))
print("s1: {}".format(s1))
print("s2: {}".format(s2))
if(s1>s2):
    print("Player1 is winner")
else:
    print("player 2")

