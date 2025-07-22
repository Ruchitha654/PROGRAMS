class Rectangle:
    info1="*Sum of angle is 360 degree" 
    info2="*Each angle is 90 degree"
    def calculate(self):
        length=int(input("Enter the length of rectagle"))
        self.length=length
        breadth=int(input("Enter the breadth of rectangle"))
        self.breadth=breadth
        Area=length*breadth
        print("The area of the rectangle is {}".format(Area))
        Perimeter=2*(length+breadth)
        print("The perimeter of the rectangle is {}" .format(Perimeter))
print(Rectangle.info1)
print(Rectangle.info2)
r1=Rectangle()
r2=Rectangle()
r1.calculate()
r2.calculate()


# OR


class rect:
    prop1="Sum of angle is 360 degree"
    prop2="Each angle is 90 degree"
    def get_info(self):
        a=int(input("enter the length of rectangle"))
        b=int(input("enter the breadth"))
        self.len=a
        self.breadth=b
    def area(self):
        print(self.len*self.breadth)
    def perimeter(self):
        print((self.len+self.breadth)*2)        
print("The Rectangle Properties")
print(rect.prop1)
print(rect.prop2)
a1=rect()
a2=rect()
a1.get_info()
a2.get_info()
a1.area()
a1.perimeter()
a2.area()
a2.perimeter()
            