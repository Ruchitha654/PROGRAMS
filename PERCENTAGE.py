# need to get 5 names from user and 3 subjects marks from 1 student and display their names with percentage in the format 

import time
names=[] 
marks=[]   
for i in range(5):
    n=input("Enter the name{}".format(i+1))
    names.append(n)
    student=[]
    for j in range(3):
        m=int(input("Enter mark {}: " .format(j+1)))
        student.append(m)
    marks.append(student)
    
per=[]
for i in marks:
    res=sum(i)//3
    per.append(res)

time.sleep(3)
print("-------------")
for i in range(5):
    print("{}.{} : {}".format(i+1,names[i],per[i]))
    
    
        #   or
        
        
names=[]
sub=[]
per=[]
for i in range(5):
    a=input(f"Name {i+1}:")
    names.append(a)
    tot=0
    p=0
    for j in range(3):
        b=int(input(f"sub {j+1} mark:"))
        sub.append(b)
        tot=tot+b
    p=tot//3
    per.append(p)
print("----------------")
for i in range(5): 
    print(f"{i+1}. {names[i]} : {per[i]}%")
print()