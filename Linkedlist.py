class Node:
    def __init__(self,data):
        self.data=data
        self.nextnode=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def insertatstart(self,data):
        newnode=Node(data)
        self.size+=1
        if not self.head:
            self.head=newnode
        else:
            newnode.nextnode=self.head
            self.head=newnode
        print(f"Created the first node {data}")
    def append(self,data):
        temp=self.head
        newnode=Node(data)
        if self.head is None:
            self.insertatstart(data)
        else:
            while(temp.nextnode!=None):
                temp=temp.nextnode
            temp.nextnode=newnode
            self.size+=1
        print(f'The node {data} is inserted at the end of the list')

    def insert(self,pos,data):
        count=1
        newnode=Node(data)
        if(pos==1):
            newnode.nextnode=self.head
            self.head=newnode
        else:
            temp=self.head
            while temp!=None and count!=pos-1:
                count+=1
                temp=temp.nextnode    
            newnode.nextnode=temp.nextnode
            temp.nextnode=newnode
        print(f'\nThe {data} is inserted at position {pos}')
        
    
    def ll_size(self):
        print(f'\nThe size of the list is:{self.size}')

    
    def info(self):
        temp=self.head
        if(self.head==None):
            print("Empty List")
        else:
            print("The elements of the linked list are: ")
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.nextnode

    def set(self,data,pos):
        count=0
        temp=self.head
        while temp!=None and count!=pos-1:
            temp=temp.nextnode
            count+=1
        temp1=temp.data
        temp.data=data
        print(f'The node {temp1} is replaced by {data} at {pos} ')

    def get(self,pos):
        count=0
        temp=self.head
        while temp!=None and count!=pos-1:
            temp=temp.nextnode
            count+=1
        print(f'The element at {pos} is {temp.data}')
    
    def remove(self,data):
        if self.head is None:
            return
        curr=self.head
        back=None
        while curr.data!=data:
            back=curr
            curr=curr.nextnode
        if back is None:
            self.head=self.head.nextnode
        else:
            back.nextnode=curr.nextnode
        self.size-=1
        print("\nRemoved the node",data)

    def clear(self):
        self.head=None
        print("List cleared")

    
        


