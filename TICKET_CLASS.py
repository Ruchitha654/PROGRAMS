# from datetime import datetime
# class Bus:
#     def __init__ (self,bno,ac,cap):
#         self.bno=bno
#         self.ac=ac
#         self.cap=cap
#     def get_bno(self):
#         return self.bno 
#     def get_ac(self):
#         return self.ac
#     def get_cap(self):
#         return self.get_cap
#     def display(self):
#         print("us number",self.get_bno())
#         print("AC",self.get_ac())
#         print("Capacity",self.get_cap())
# BUSES=[Bus(1,True,2),Bus(2,False,60),Bus(3,True,55)]        
        
# class Booking:
#     def __init__(self):
#         name=input("Enter your name")
#         bno=int(input("Enter the bus number"))
#         d=input("Enter the date in the format of dd-mm-yyyy")
#         date=datetime.strptime(d,"%d-%m-%Y").date()
#         self.name=name
#         self.bno=bno
#         self.date=date
#     def make_booking(self,BUSES,BOOKINGS):
#         if(self.is_available(BUSES,BOOKINGS,self.bno,self.date)):
#             BOOKINGS.append(self)
#         else:
#             print("Bookings full")
#     def is_available(self,BUSES,BOOKINGS,bno,date):
#         booked=0
#         capacity=0    
#         for i in BUSES:
#             capacity=0
#             booked=0
#             if (self.bno==i.get_bno):
#                 capacity=i.cap
                    
#         for i in BOOKINGS:
#             if(i.bno==bno) and (i.date==date):
#                 booked=booked+1
#         return booked<capacity
#     def display_book_info(self):
#          print(f"Passenger: {self.name}, Bus No: {self.bno}, Date: {self.date}")          

# print("Available buses are")
# for i in BUSES:
#     i.display()
#     print("----------")
# BOOKINGS=[]
# while(True):
#     print("PRESS 1 TO BOOK TICKETS")
#     print("PRESS 2 TO VIEW BOOKING")
#     print("PRESS 3 TO EXIT")
#     ch=int(input("Enter your choice"))
#     if(ch==1):
#         b=Booking()
#         b.make_booking(BUSES,BOOKINGS)
#     elif(ch==2):
#         if(not BOOKINGS):
#             print("No Booking so far")
#         else:
#           for i in BOOKINGS:
#             i.display_book_info()
#     elif(ch==3):
#         print("Exiting the system.Thank You")
    
#     else:
#         print("Invalid choice")         
            
            

        
                
                
                
                
from datetime import datetime

class Bus:
    def __init__(self, bno, ac, cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno 

    def get_ac(self):
        return self.ac

    def get_cap(self):
        return self.cap

    def display(self):
        print("Bus number:", self.get_bno())
        print("AC:", "Yes" if self.get_ac() else "No")
        print("Capacity:", self.get_cap())

BUSES = [Bus(1, True, 2), Bus(2, False, 60), Bus(3, True, 55)]        

class Booking:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.bno = int(input("Enter the bus number: "))
        d = input("Enter the date in the format of dd-mm-yyyy: ")
        self.date = datetime.strptime(d, "%d-%m-%Y").date()

    def make_booking(self, BUSES, BOOKINGS):
        if self.is_available(BUSES, BOOKINGS, self.bno, self.date):
            BOOKINGS.append(self)
            print("Booking successful!")
        else:
            print("Bookings full")

    def is_available(self, BUSES, BOOKINGS, bno, date):
        booked = 0
        capacity = 0    
        for bus in BUSES:
            if bus.get_bno() == bno:
                capacity = bus.get_cap()
                break
        
        for booking in BOOKINGS:
            if booking.bno == bno and booking.date == date:
                booked += 1

        return booked < capacity

    def display_book_info(self):
        print(f"Passenger: {self.name}, Bus No: {self.bno}, Date: {self.date}")
print("Available buses are:")
for bus in BUSES:
    bus.display()
    print("----------")

BOOKINGS = []

while True:
    print("\nPRESS 1 TO BOOK TICKETS")
    print("PRESS 2 TO VIEW BOOKINGS")
    print("PRESS 3 TO EXIT")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        b = Booking()
        b.make_booking(BUSES, BOOKINGS)
    elif ch == 2:
        if not BOOKINGS:
            print("No bookings so far.")
        else:
            for booking in BOOKINGS:
                booking.display_book_info()
    elif ch == 3:
        print("Exiting the system. Thank you!")
        break
    else:
        print("Invalid choice")






         
                    
# from datetime import datetime
# class Bus:
#    def _init_(self,bno,ac,cap):
#     self.bno=bno
#     self.ac=ac
#     self.cap=cap
#    def get_bno(self):
#     return self.bno
#    def get_ac(self):
#     return self.ac
#    def get_cap(self):
#     return self.cap
#    def display(self):
#     print(f"1.BUS N0",self.get_bno())
#     print(f"2.Ac",self.get_ac())
#     print(f"3.CAPACITY",self.get_cap())

# class Booking:
#    def _init_(self):
#       name=input("Enter passenger name")
#       bno=int(input("Enter bus no"))
#       d=input("Enter date(dd-mm-yyyy)")
#       date=datetime.strptime(d,"%d-%m-%Y").date()
#       self.name=name
#       self.bno=bno
#       self.date=date
#    def make_booking(self,BUSES,BOOKINGS):
#       if(self.is_available(BUSES,BOOKINGS,self.bno,self.date)):
#          BOOKINGS.append(self)
#       else:
#          print("BUS IS FULL")
#    def is_available(self,BUSES,BOOKINGS,bno,date):
#       booked=0
#       capacity=0
#       for i in BUSES:
#          if(i.bno==bno):
#             capacity=i.cap
#       for i in BOOKINGS:
#          if(i.bno==bno and i.date==date):
#             booked=booked+1
#          return booked<capacity
#    def display_book_info(self):
#       print(f"passenger")            

         
# BUSES=[Bus(1,True,2),Bus(2,False,60),Bus(3,True,55)]
# print("Available buses are")
# for i in BUSES:
#     i.display()
#     print("----------")
# BOOKINGS=[]
# while(True):
#     print("PRESS 1 TO BOOK TICKETS")
#     print("PRESS 2 TO VIEW BOOKING")
#     print("PRESS 3 TO EXIT")
#     ch=int(input("Enter your choice"))
#     if(ch==1):
#         b=Booking()
#         b.make_booking(BUSES,BOOKINGS)
#     elif(ch==2):
#         if(not BOOKINGS):
#             print("No Booking so far")
#         else:
#           for i in BOOKINGS:
#             i.display_book_info()
#     elif(ch==3):
#         print("Exiting the system.Thank You")
    
#     else:
#         print("Invalid choice")         
            
            
