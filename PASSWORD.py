a=input("enter the passwword")
up=0
lw=0
sp=0
dg=0
if(len(a)>7):
    for i in a:
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            lw=lw+1
        elif(i.isdigit()):
            dg=dg+1
        else:
            sp=sp+1
    if(up>0 and lw>0 and dg>0 and sp>0):
        print("it is a good password")
    else:
        print("not a good password")
else:
    print("bad password as the characters arent enough")