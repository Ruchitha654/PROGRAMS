file=open("file2.txt",'r')
data=file.readlines()
for i in data:
    print(i)
    print(i.split())

