# 16.Create a class Publisher with attributes publisher id and publisher name. Derive class Book
# from Publisher with attributes title and author. Derive class Python from Book with
# attributes price and no_of_pages. Write a program that displays information about a Python
# book. Use base class constructor invocation and method overriding.

class publisher:
    def __init__(self,id,name):
        self.id = id
        self.name = name
class book(publisher):
    def __init__(self, id, name,title,author):
        super().__init__(id, name)
        self.title = title
        self.author = author
class python(book):
    def __init__(self, id, name, title, author,price,noOfPages):
        super().__init__(id, name, title, author)
        self.price = price
        self.noOfPages = noOfPages
    
    def displayInfo(self):
        print(f"\nInfo for Book: {self.title}\n\nBook ID: {self.id}\nAuthor: {self.author}\nPrice: {self.price}\nNo of pages: {self.noOfPages}")

newBook = python(1,"samplePub", "sampleBookName","someAuthor",1000,10000)
newBook.displayInfo()

    