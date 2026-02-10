#Abstraction
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")
    
    def sleep(self):
        print("Dog is sleeping")

class Cat(Animal):
    def sound(self):
        print("Cat meow")

    def sleep(self):
        print("Cat is sleeping")

class Cow(Animal):
    def sound(self):
        print("Cow Moo")

    def sleep(self):
        print("Cow is sleeping")

dog = Dog()
dog.sound()
dog.sleep()

cat = Cat()
cat.sound()
cat.sleep()

cow = Cow()
cow.sound()
cow.sleep() 


# Class Variable + Classmethod + Staticmethod
class Student:
    college_name="ABC College"

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    @classmethod
    def change_college(cls,new_name):
        cls.college_name=new_name

    @staticmethod
    def is_pass(marks):
        if marks>=35:
            return "Pass"
        else:
            return "Fail"
        
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
        print("College:",Student.college_name)

s1=Student("Bhumika",101)
s2=Student("Ammu",102)

s1.display()
print("Result:",Student.is_pass(78))
print()

Student.change_college("XYZ University")

s2.display()
print("Result:",Student.is_pass(30))


#Decorator
def admin_only(dashboard):
    def wrapper(username):
        if username=="admin":
            print("Login success")
            dashboard(username)
        else:
            print("Access Denied")
    return wrapper

@admin_only
def dashboard(username):
    print("Welcome to dashboard")
dashboard("admin") 
