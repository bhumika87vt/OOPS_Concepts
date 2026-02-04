#Single Inheritance
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author 

    def display_book_details(self):
        print(f"The title of the book is {self.title} and is written by {self.author}")

class IssuedBook(Book):
    def __init__(self,title,author,issued_to,issued_date):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    
    def display_issued_book_details(self):
        print(f"Title:{self.title}\n Author:{self.author}\n Issued to:{self.issued_to}\n Issued Date:{self.issued_date}")

Issue=IssuedBook("History of APJ Abdul Kalam","APJ Abdul kalam","Bhumika","02-02-2026")
Issue.display_book_details()
Issue.display_issued_book_details()