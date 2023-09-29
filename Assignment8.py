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
    def get(list,index):
        n=list._first
        for i in range(index):
            n=n._next
            if n==None:
                break
        else:
            return n._value
    def set(list,index,value):
        n=list._first
        for i in range(index):
            n=n._next
            if n==None:
                break
        else:
            n._value=value
    def insert(list, index, value):
        new=Node(value)
        if(index==1):
            new._next=list._first
            list._first._previous=new
            list._first=new
        else:
            n=list._first
            for i in range(1,index-1):
                if n!=None:
                    n=n._next
            new._next=n._next
            new._previous=n
            n._next=new           

    def remove(list, index):
        if list._first is None:
            print("List is empty")
        n=list._first
        for i in range(1,index):
            n=n._next
        if n._previous is None:
            list._first=list._first.nextnode
        else:
            n._previous._next=n._next

l1=LinkedList()
for i in range(10):
    l1.append(i)
print("------Inserted---------")
print(l1.info())
print("-------Inserting at pos 4---------")
l1.insert(4,30)
print(l1.info())
print("------Inserting at pos 1------")
l1.insert(1,11)
print(l1.info())
print("-------Removing at 5---------")
l1.remove(5)
print(l1.info())