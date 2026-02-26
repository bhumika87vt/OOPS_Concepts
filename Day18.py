#Encapsulation
#Public access

class Book:
    def __init__(self):
        pass

b = Book()
b.title = "1984"
print(b.title)


class Student:
    def __init__(self):
        self.present_days=0


s = Student()
s.present_days = 15
print(s.present_days)


class Course:
    def __init__(self):
        self.completed_modules=0

c = Course()
c.completed_modules = 5
print(c.completed_modules)


class BankAccount:
    def __init__(self):
        pass

acc = BankAccount()
acc.account_holder = "Alice"
print(acc.account_holder)