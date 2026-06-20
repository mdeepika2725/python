class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
    def display(self):
        temp= self.head
        while(temp!=None):
            print(temp.data, end='-->')
            temp=temp.next
x = LinkedList()
x.insert(20)
x.insert(220)
x.insert(320)
x.insert(420)
x.display()
