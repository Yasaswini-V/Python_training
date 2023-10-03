class Book:
    def __init__(self):
        self.Books=list()

    def insert_book(self,id,title,author,price,rating):
        b=Book()
        b._id=int(id)
        b._title=title
        b._author=author
        b._price=int(price)
        b._rating=int(rating)
        self.Books.append(b)

    def __str__(self):
        print("------------------------")
        return f'1.Book id={self._id}\n2.Book Title={self._title}\n3.Book price={self._price}\n4.Book rating={self._rating}'
               
    def info(self):
        for Book in self.Books:
            print(Book)

    def find_by_id(self,id):
        for Book in self.Books:
            if Book._id==id:
                print(Book)
        else:
            return f"Book with {id} is not found"

    def find_by_author(self,author):
        for Book in self.Books:
            if Book._author==author:
                print(Book)
        else:
            return f"Book written by {author} is not found"

    def find_in_range(self,maxi):
        for Book in self.Books:
            if Book._rating<=maxi:
                print(Book)
        else:
            return f"Book in range {max} is not found"
    
    def find_in_price(self,price):
        for Book in self.Books:
            if Book._price<=price:
                print(Book)
        else:
            return f"Book in range {price} is not found"

    
def main():
    B=Book()
    B.insert_book(1,"abc","wer",200,4)
    B.insert_book(2,"wed","okj",500,5)
    B.insert_book(1,"plm","bnh",2000,1)
    B.insert_book(2,"okj","wer",300,3)
    B.insert_book(3,"yue","pos",900,3)
    print("-------By id---------")
    B.find_by_id(1)
    print("-------By author---------")
    B.find_by_author("wer")
    print("-------In range---------")
    B.find_in_range(3)
    print("-------In price---------")
    B.find_in_price(500)



   

