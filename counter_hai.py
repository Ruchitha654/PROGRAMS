from collections import Counter
a={2,3,4,5,6}
b={2,3,8,7,9}
c=Counter(b)
for i in a&b:
    for j in range(c[7]):
        print("Hai",end=" ")
