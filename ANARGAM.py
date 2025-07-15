str1=input("Enter the string1")
str2=input("Enter the second string")
a=str1.lower()
b=str2.lower()
a1="".join(i for i in a if i!=" ")
b1="".join(i for i in b if i!=" ")
a2=sorted(a1)
b2=sorted(b1)
if( a2==b2):
    print("Anargam")
else:
    print("not Anargam")