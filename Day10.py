#Hierarchical Inheritance
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade=grade
    def get_details(self):
        return f"{self.name} is {self.age} years old and studies in {self.grade} grade."
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name,age)
        self.subject=subject
    def get_details(self):
        return f"{self.name} is {self.age} years old and teaches {self.subject}."
s1 = Student("Asha", 15, "10th")
print( s1.get_details())
s2=Teacher("Mr . Roy",40,"Mathematics")
print(s2.get_details())



class Vehicle:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand,model)
        self.doors=doors
    def description(self):
        return f"{self.brand} {self.model} with {self.doors} doors."
class Bike(Vehicle):
    def __init__(self, brand, model, engine):
        super().__init__(brand,model)
        self.engine=engine
    def description(self):
        return f"{self.brand} {self.model} with {self.engine} engine."
c1 = Car("Toyota", "Camry", 4)
print( c1.description())
c2=Bike("Yamaha","FZ","220cc")
print(c2.description())



class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
class Instructor(User):
    def __init__(self, name, email, course):
        super().__init__(name,email)
        self.course=course
    def role(self):
        return f"{self.name} ({self.email}) teaches {self.course}."
class Learner(User):
    def __init__(self, name, email, course):
        super().__init__(name,email)
        self.course=course
    def role(self):
        return f"{self.name} ({self.email}) is enrolled in {self.course}."
i1 = Instructor("Arjun", "arjun@edu.com", "Python")
print( i1.role())
l1=Learner("Neha","neha@edu.com","Python")
print(l1.role())



class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title,author)
        self.genre=genre
    def details(self):
        return f"'{self.title}' by {self.author} is a {self.genre} novel."
class Magazine(Book):
    def __init__(self, title, author, issue):
        super().__init__(title,author)
        self.issue=issue
    def details(self):
        return f"'{self.title}' by {self.author}, Issue: {self.issue}."
n1 = Novel("The Alchemist", "Paulo Coelho", "Fiction")
print( n1.details())
m1=Magazine("Tech Times","Editor Team","August 2025")
print(m1.details())
