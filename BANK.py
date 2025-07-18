def deposit(acc,amt):
    accounts[acc]+=amt
def withdraw(acc,amt):
    if(amt>accounts[acc]):
        print("Insufficient Balance!!")
    else:
        accounts[acc]-=amt
        print("Remaining balance:",accounts[acc])
    
def transfer(to_acc,amt):
    if(amt>accounts[acc]):
        print("Insufficient Balance!!")
    else:
        accounts[to_acc]+=amt
        accounts[acc]-=amt
accounts={101:1000,102:2000,103:500}
while True:
    print("------WELCOME TO MULTIACCOUNT BANKING SYSTEM-----")
    acc=int(input("Please enter the account number(0 TO EXIT):"))
    if(acc==0):
        print("THANK YOU...VISIT AGAIN...EXITING")
        exit()
    elif(acc not in accounts):
        print("Account not found!!")
    else:
        ch=1
        while ch!=5:
            print("--------ACCOUNT MENU--------")
            print("1.CHECK BALANCE")
            print("2.DEPOSIT")
            print("3.WITHDRAW")
            print("4.TRANSFER")
            print("5.LOGOUT")
            ch=int(input("Enter your choice:"))
            match ch:
                case 1:
                    print("Balance is: ",accounts[acc])
                case 2:
                    amt=int(input("Enter the amount to deposit:"))
                    deposit(acc,amt)
                case 3:
                    amt=int(input("Enter the amount to withdraw:"))
                    withdraw(acc,amt)
                case 4:
                    to_acc=int(input("Enter the account to transfer:"))
                    if(to_acc not in accounts):
                        print("Account not found!!")
                    else:
                        amt=int(input("Enter the amount to transfer:"))
                        transfer(to_acc,amt)
                case 5:
                    print("Logging out.....")
                    break
