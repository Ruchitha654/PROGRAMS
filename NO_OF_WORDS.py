str1=input("enter the sentence")
count=0
for i in range(len(str1)):
    if (str1[i]==" " and str1[i+1]!=" "):
        count=count+1
print(count+1)