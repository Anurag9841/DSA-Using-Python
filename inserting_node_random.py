class node:
    def __init__(self,data):#creating node ---> a node consist of data and next
        #data is used to store value and next to store address of next node
        self.data=data
        self.next=None
class linkedlist:#creating link between list
    def __init__(self):
        self.head=None

#inserting element at the desired place
    def insert_random(self,index,value):
        newnode=node(value)
        if self.head==None:
            self.head==newnode
        else:
            temp=self.head
            count=0
            while temp!=None:
                if count==index-1:
                    newnode.next=temp.next
                    temp.next=newnode
                    break
                count+=1
                temp=temp.next


#traversing node
    def traversing(self):
     if self.head==None:
            print("The given node is empty")
     else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next


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

ll=linkedlist()
ll.insertlast(30)
ll.insertlast(20)
ll.insertlast(10)
ll.traversing()
print()
ll.insert_random(2,"apple")
ll.traversing()