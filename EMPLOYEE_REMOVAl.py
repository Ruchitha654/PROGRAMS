names=["A","B","C","D","E","F","G","H","I","J"]
memo=[0,1,1,1,2,2,1,2,1,2]
salary=[1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]
l=[]
res=list(zip(names,memo,salary))
for i in res:  
    if i[2]>4000:
       res.remove(i)
       l.append(i)
s=sorted(res)
for j in res:
    if j[1]>1:
        l.append(j)
index=1
for i in l:
    print("{}.Name:{} salary :{}  memo:{}".format(index,i[0],i[2],i[1]))
    index=index+1
    
    
    # OR
names=["A","B","C","D","E","F","G","H","I","J"]
memo=[0,1,1,1,2,2,1,2,1,2]
salary=[1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]
data=list(zip(salary,memo,names))
removed1=[]
removed2=[]
for i in data:
  if(i[0]>4000):
    removed1.append(i)
remaining=[i for i in data if i[0]<4000]    
a=sorted(remaining,key=lambda x:x[0],reverse=True)
index=0
for i in a:
  if(i[1]>=2):
    removed2.append(i)
  if(len(removed2)>3):
    break
final=removed1+removed2
for i in final:
  print("{}.{} : Memo{}:salary {}".format(index,i[2],i[1],i[0]))
  index=index+1