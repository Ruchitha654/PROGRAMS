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