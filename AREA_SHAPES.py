def circle():
    r=int(input("enter the radius of the circle"))
    print("the area of circle is",3.14*r*r)
def square(s):
    print("the area of square is ",s*s)
def triangle():
    b=int(input("enter the base"))
    h=int(input("enter the height"))
    return 0.5*b*h
def rectangle(l,br):
    return l*br
a=1
while(a>0):
    print("1 Circle")
    print("2 Square")
    print("3 Triangle")
    print("4 Rectangle")
    print("5 EXIT")
    a=int(input("enter your choice"))
    match a:
        case 1:
            circle() 
        case 2:
            s=int(input("enter the side"))
            square(s)
        case 3:
            tri=triangle()
            print("the area of triangle is ",tri)
        case 4:
            l=int(input("enter the length"))
            br=int(input("enter the breadth"))
            rec=rectangle(l,br)
            print("the area of rectangle is ",rec)
        case 5:
            exit ()
