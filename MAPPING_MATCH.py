
n=int(input("enter the number of teams"))
teams=[]
for i in range(n):
    t=input("enter the team names:")
    teams.append(t)
meet=int(input("enter the number of meeting"))
match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            match.append([teams[i],teams[j]])
index=1
for i in match:
    print("{} vs {}".format(i[0],i[1]))