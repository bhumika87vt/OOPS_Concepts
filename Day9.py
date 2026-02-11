#Dunder Methods
#__str__() and __repr__()
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"Book:'{self.title}' by {self.author}, price:{self.price}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price})"

b1=Book("Python","John",499)
b2=Book("Java","Bob",699)

print(b1)
print(b2)

print([b1,b2])


#__eq__()
class Mobile:
    def _init_(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    
    def __eq__(self,other):
        return(
            self.brand==other.brand and
            self.model==other.model and
            self.price==other.model
        )
    
m1=Mobile("Apple","iphone13",50000)
m2=Mobile("Apple","iphone15",55000)
m3=Mobile("Android","Oneplus",45000)

print(m1==m2)

#__new__() and __init__()
class User:
    
    def __new__(cls, *args, **kwargs):
        print("Object is being created")
        return super().__new__(cls)  

    def __init__(self, name):
        print("Object is initialized")
        self.name = name

u1 = User("Bhumika")

#__enter__() and __exit__()
class DatabaseConnection:

    def __enter__(self):
        print("Database Connected")
        return self   

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database Closed")

with DatabaseConnection():
    print("Performing Query...")
