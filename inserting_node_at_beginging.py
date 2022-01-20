class node:
    def __init__(self,data):#creating node ---> a node consist of data and next
        #data is used to store value and next to store address of next node
        self.data=data
        self.next=None
class linkedlist:#creating link between list
    def __init__(self):
        self.head=None


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
ll.insert_beginging(2)
ll.insert_beginging(4)
ll.insert_beginging(10)
ll.traversing()