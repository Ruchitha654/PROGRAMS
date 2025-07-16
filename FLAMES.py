boy=input("Enter the name of a boy")
girl=input("enter the name of the girl")
a1=list(boy)
a2=list(girl)
for i in range(len(a1)):
    for j in range(len(a2)):
        if(a1[i]==a2[j]):
            a1[i]='2'
            a2[j]='2'
count=0
for i in a1: 
    if (i!='2'):
        count=count+1
for i in a2:
    if(i!='2'):
        count=count+1
print(count)
ans=['F','L','A','M','E','S']
index=0
while(len(ans)!=1):
    index=(index+(count-1))%len(ans)
    ans.pop(index)
print("The relation is",ans[0])