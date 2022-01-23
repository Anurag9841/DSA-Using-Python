class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class linkedlist:
    def __init__(self):
        self.head=None
    
    def traverse_forward(self):
        if self.head==None:
            print("The given node is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next

    def traverse_backward(self):
        if self.head==None:
            print("The given linked list is empty")
        else:
            a=self.get_last_node()
            temp=a
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.prev

    def get_last_node(self):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        return temp
                
    def insert_last(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
            newnode.prev=None
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp
            newnode.next=None

ll=linkedlist()
ll.insert_last(20)
ll.insert_last(30)
ll.insert_last(40)
ll.traverse_forward()
print()
# ll.get_last_node()
print()
ll.traverse_backward()
