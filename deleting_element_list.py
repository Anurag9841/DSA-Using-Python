class node:
    def __init__(self,data):
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
#inserting element at the desired place
    def insert_random(self,index,value):
        newnode=node(value)
        if self.head==None:
            self.insert_beginging(value)
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

#deleting element from the beginging
    def delete_begining(self):
        if self.head==None:
            print("The given list is empty")
        else:
            temp=self.head
            self.head=temp.next
#deleting element from desired place
    def delete_random(self,index):
        if self.head==None:
            print("The given list is empty")
        else:
            count=0
            temp=self.head
            while temp!=None:
                if count==index-1:
                    temp.next=temp.next.next
                    break
                count+=1
                temp=temp.next
            
ll=linkedlist()
ll.insertlast(30)
ll.insertlast(20)
ll.insertlast(10)
ll.traversing()
print()
ll.insert_beginging(2)
ll.insert_beginging(40)
ll.traversing()
print()
ll.delete_random(4)
ll.traversing()
print()
ll.insert_random(2,"apple")
ll.traversing()