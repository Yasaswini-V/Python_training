class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
        
class LinkedList:
    def __init__(self):
        self._first=None

    def append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c

    def insert(self, index, value):
        y=self.__locate(index)
        if not y:
            return 
        x=y._previous 
        new_node=Node(value,previous=x,next=y)
        if x:
            x._next=new_node
        else:
            self._first=new_node
        y._previous=new_node

    def sorting(self):
        if self._first==None:
            return
        current=self._first
        while current._next!=None:
            temp=current._next
            while temp!=None:
                if (current._value>temp._value):
                    temp1=current._value
                    current._value=temp._value
                    temp._value=temp1
                temp=temp._next
            current=current._next
            
ll=LinkedList()
ll.append(5)
ll.append(4)
ll.append(10)
ll.append(1)
print(ll.info())
ll.sorting()
print("After sorting",ll.info())