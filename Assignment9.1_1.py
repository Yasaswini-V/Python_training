class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
def is_prime(n):
    if n<=1:
        return False
    test=2
    while test<n:
        if n%test==0:
            return False
        test+=1
    return True

def is_even(n):
    if n<=1:
        return False
    if (n%2==0):
        return True
    else:
        return False
    
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
        n=self._first
        print("The elements in linked list are: ")
        while n:
            print(n._value,end=" ")
            n=n._next
        return str

    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c

    def __locate(self,index):
        if index>=self.size():
            return None
        
        n=self._first
        for i in range(index):
            n=n._next
            
        return n


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

    def prime_numbers(self):
        if self._first==None: 
            return "LinkedList(empty)"
        n=self._first
        print("\nThe prime numbers in the list: ")
        while n:
            if is_prime(n._value):
                print(n._value,end=" ")
            n=n._next
            
    def even_numbers(self):
        if self._first==None:
            return "Linked list is empty"
        n=self._first
        print("\nThe even numbers in the list are: ")
        while n:
            if is_even(n._value):
                print(n._value,end=" ")
            n=n._next


ll=LinkedList()
maxi=100
for i in range(maxi+1):
    ll.append(i)  
ll.info()
ll.prime_numbers()
ll.even_numbers()