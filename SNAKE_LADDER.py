import random
score1=0
score2=0
while score1<100 or score2<100:
    ch=int(input("Enter the player no. :"))
    match ch:
        case 1:
            n=random.randint(1,6)
            print("Dice:",n)
            if score1>=100:
                print("Player 1 wins!!")
                exit()
            if score2>=100:
                print("Player 2 wins!!")
                exit()
            score1+=n
            if score1==22:
                print("You got caught by snake!!!")
                score1=6
            if score1==45:
                print("YOu got caught by snake!!")
                score1=30
            if score1==96:
                print("YOu got caught by snake!")
                score1=64
            
            if score1==7:
                print("Congratulations you got a ladder!!!")
                score1=24
            if score1==21:
                print("Congratulations you got a ladder!!")
                score1=77
            if score1==40:
                print("Congratulations you got a ladder!")
                score1=60
            print("Player 1:",score1)
            print("Player 2:",score2)
            
            
        case 2:
            n=random.randint(1,6)
            print("Dice:",n)
            if score1>=100:
                print("Player 1 wins!!!")
                exit()
            if score2>=100:
                print("Player 2 wins!!!")
                exit()
            score2+=n
            if score2==22:
                print("You got caught by snake!!!")
                score2=6
            if score2==45:
                print("YOu got caught by snake!!")
                score2=30
            if score2==96:
                print("YOu got caught by snake!")
                score2=64
            
            if score2==7:
                print("Congratulations you got a ladder!!!")
                score2=24
            if score2==21:
                print("Congratulations you got a ladder!!")
                score2=77
            if score2==40:
                print("Congratulations you got a ladder!")
                score2=60
            print("Player 1:",score1)
            print("Player 2:",score2)
            if score1==100:
                print("Player 1 wins!!!")
                exit()
            if score2==100:
                print("Player 2 wins!!!")
                exit()