# a monkey has to climb the post of "x" meters , every minute it climbs "a" meters and in the next minute it slides down by "b" minutes. find the total time taken by the monkey to reach top
def cal(x,a,b):
    m=0
    while x>0 :
        x=x-a
        m=m+1
        if x==0:
            return m
        x=x+b
        m=m+1
    return m
print(cal(25,7,4))
print(cal(30,10,5))
        