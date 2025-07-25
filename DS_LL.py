class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def add_data(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
        else:
            temp=self.head
            while(temp.next!=None):
              temp=temp.next 
            temp.next=newNode
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end="->")
            temp=temp.next
        print("None")
            
    def delete(self, a):
        if(self.head == None):
            print("Not possible")
            return
        elif(a==1):
            temp = self.head
            self.head = temp.next
        else:
            prev = None
            current = self.head
            for i in range(1, a):
                prev = current
                current = current.next
                if current == None:
                    print("Element not found")
                    return
            prev.next = current.next
l=LinkedList()
l.add_data(20)
l.add_data(10)
l.add_data(25)
l.add_data(28)
l.delete(2)
l.display()