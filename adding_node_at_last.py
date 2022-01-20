class node:
    def __init__(self,data):#creating node ---> a node consist of data and next
        #data is used to store value and next to store address of next node
        self.data=data
        self.next=None
class linkedlist:#creating link between list
    def __init__(self):
        self.head=None
#inserting element at last
    def insertlast(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
#printing element in linked list
    def traversing(self):
        if self.head==None:
            print("The given node is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
#inserting element at beginging
    def insert_beginging(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
            
ll=linkedlist()
ll.insertlast(30)
ll.insertlast(20)
ll.insertlast(10)
ll.traversing()
print()
ll.insert_beginging(2)
ll.traversing()