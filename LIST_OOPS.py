class rect:
    def set_dim(self,a,b):
        self.a=a
        self.b=b
        
    def area(self):
        return self.a*self.b
nums=[]

d=int(input("Enter the number"))
for i in range(d):
    R=rect()
    a=int(input("enter the length"))
    b=int(input("enter the breadth"))
    R.set_dim(a,b)
    nums.append(R)
index=0
for  i in nums:
      print("The area of {}: is {}" .format(index,i.area()))
      index=index+1


# extra concepts 
# nums[9].area   = to print 10th rectangle area
# i.a  == to print the length of rectangles only
# if(i.area()%2==0):    ===to print the even areas only 
    # print(i.area())
# R=rect(random.randint(1,5).random.randint(5,10))
      