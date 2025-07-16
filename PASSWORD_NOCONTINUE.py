password = input("Enter the password: ")

up = 0
lw = 0
dg = 0
sp = 0
repeat = 0

if len(password) > 7:
    prev = ""
    for ch in password:
        if ch == prev:
            repeat = 1
        if ch.isupper():
            up = 1
        elif ch.islower():
            lw = 1
        elif ch.isdigit():
            dg = 1
        else:
            sp = 1
        prev = ch

    if up and lw and dg and sp and repeat == 0:
        print("Good password")
    else:
        print("Not a good password")
else:
    print("Bad password: too short")
