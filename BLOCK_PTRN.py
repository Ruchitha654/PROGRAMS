
b=int(input("enter the number of blocks"))
l=int(input("enter the number of lines"))
s=int(input("enter te number of stars"))
sum=0
for k in range(b):
    print(f"-------------BLOCK{k+1}------------")
    count=0
    for i in range(l-k):
        for j in range(s): 
          print("*",end=" ")
          count=count+1
        print()
    print(count)
    sum+=count
print(f"Total:{sum}")
