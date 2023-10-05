class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
        
class LinkedList:
    def __init__(self, *args):
        self._first=None
        self._last=None
        self._count=0
        self.append(*args)
        

    def append(self, *args):
        for value in args:
            self._append(value)


    def _append(self, value):
        node=Node(value,previous=self._first)
        if not self._first:
            self._first=node
        else:
            self._last._next=node
        self._last=node
        self._count+=1
                  
                  
    #def info(self):
    def __str__(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="Books:\n"
        n=self._first
        while n:
            str+=f'Book id={n._value["b_id"]}\nBook title={n._value["title"]}\nBook author={n._value["author"]}\nBook price={n._value["price"]}\nBook rating={n._value["rating"]}'
            n=n._next
            str+="\n----------------------------------\n"
        return str

    #def size(self):
    def __len__(self):
        return c
        

    def __locate(self,index):
        if index>=len(self):
            raise IndexError(f'Invalid Index :{index}')
        
        n=self._first
        for i in range(index):
            n=n._next
            
        return n


             
    #def get(self,index):
    def __getitem__(self,index):
        n=self.__locate(index)
        return n._value  #if n else None
    

    #def set(self,index,value):
    def __setitem__(self,index,value):
        n=self.__locate(index)
        n._value=value

    def insert(self, index, value):
        y=self.__locate(index)
        x=y._previous 

        new_node=Node(value,previous=x,next=y)
        
        if x:
            x._next=new_node
        else:
            self._first=new_node

        y._previous=new_node
        self._count+=1

    def remove(self, index):
        n=self.__locate(index)
        x= n._previous
        y= n._next
        if x:
            x._next=y
        else:
            self._first=y
        if y:
            y._previous=x    
        self._count-=1
        return n._value
                  
    
    def __iter__(self):
        return LinkedList.Iterator(self)

    def print_obj(self,n):
        str=""
        str+=f'Book id={n["b_id"]}\nBook title={n["title"]}\nBook author={n["author"]}\nBook price={n["price"]}\nBook rating={n["rating"]}'
        str+="\n----------------------------------\n"
        return str


    def find_by_id(self,id):
        it=iter(self)
        try:
            while True:
                value1=next(it)
                if value1["b_id"]==id:
                    print(self.print_obj( value1))
        except StopIteration:
            print('done')

    def find_by_author(self,author):
        it=iter(self)
        try:
            while True:
                value=next(it)
                if value["author"]==author:
                    print(self.print_obj(value))
        except StopIteration:
            print('')

    def find_in_range(self,maxi):
        it=iter(self)
        try:
            while True:
                value=next(it)
                if value["rating"]<=maxi:
                    print(self.print_obj(value))
        except StopIteration:
            print('')
    
    def find_in_price(self,price):
        it=iter(self)
        try:
            while True:
                value=next(it)
                if value["price"]<=price:
                    print(self.print_obj(value))
        except StopIteration:
            print('')

    
    class Iterator:
        def __init__(self, list):
            self._list=list
            self._current=None
            
        def __next__(self):
            if not self._current:
                self._current=self._list._first
            else:
                self._current=self._current._next
                
            if self._current:
                return self._current._value
            else:
                raise StopIteration()

            

# max=50
l=LinkedList()
# for i in range(max):
#     l.append(i)
b1=dict()
b1={"b_id":1,"title":"abc","author":"wer","price":200,"rating":3}
b2={"b_id":2,"title":"wed","author":"okj","price":500,"rating":5}
b3={"b_id":1,"title":"plm","author":"bnh","price":2000,"rating":1}
b4={"b_id":2,"title":"okj","author":"wer","price":300,"rating":3}
b5={"b_id":3,"title":"yue","author":"pos","price":900,"rating":3}
l.append(b1)
l.append(b2)
l.append(b3)
l.append(b4)
l.append(b5)
print("---------info-----------")
print(l)
print("---------By id------------")
l.find_by_id(1)
print("---------By author---------")
l.find_by_author("wer")
print("---------In price-----------")
l.find_in_price(500)
print("---------In rating-----------")
l.find_in_range(3)