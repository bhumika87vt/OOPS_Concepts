#Multi level Inheritance

class Organization:
    def __init__(self, company):
        self.company=company
class Department(Organization):
    def __init__(self, company, dept):
        super().__init__(company)
        self.dept=dept
class Employee(Department):
    def __init__(self, company, dept, emp_name):
        super().__init__(company,dept)
        self.emp_name=emp_name
    def get_details(self):
        return f"{self.emp_name} works in {self.dept} department at {self.company}"
e1 = Employee("Innotech", "HR", "Meera")
print(e1.get_details())


class Animal:
    def __init__(self, category):
        self.category=category
class Mammal(Animal):
    def __init__(self, category, temperature):
        super().__init__(category)
        self.temperature=temperature
class Dog(Mammal):
    def __init__(self, category, temperature, breed):
        super().__init__(category,temperature)
        self.breed=breed
    def describe(self):
        return f"This is a {self.breed}. It is a {self.temperature} {self.category}."
d1 = Dog("Animal", "Warm-blooded", "Husky")
print( d1.describe())


class Publisher:
    def __init__(self, publisher):
        self.publisher=publisher
class Series(Publisher):
    def __init__(self, publisher, series_name):
        super().__init__(publisher)
        self.series_name=series_name
class Book(Series):
    def __init__(self, publisher, series_name, title):
        super().__init__(publisher,series_name)
        self.title=title
    def info(self):
        return f"{self.title} is part of the {self.series_name} series published by {self.publisher}."
b1 = Book("Harper", "Earth Saga", "Final Planet")
print( b1.info())


class System:
    def __init__(self, os_type):
        self.os_type=os_type
class SmartSystem(System):
    def __init__(self, os_type, connectivity):
        super().__init__(os_type)
        self.connectivity=connectivity
class SmartHome(SmartSystem):
    def __init__(self, os_type, connectivity, owner):
        super().__init__(os_type,connectivity)
        self.owner=owner
    def status(self):
        return f"SmartHome of {self.owner} is running {self.os_type} and is currently {self.connectivity}."
sh1 = SmartHome("Linux", "Online", "Ravi")
print( sh1.status())


class Platform:
    def __init__(self, name):
        self.name=name
class Course(Platform):
    def __init__(self, name, title):
        super().__init__(name)
        self.title=title
class Module(Course):
    def __init__(self, name, title, module_name):
        super().__init__(name,title)
        self.module_name=module_name
    def full_title(self):
        return f"'{self.module_name}' is a module in '{self.title}' course on {self.name}"
m1 = Module("Udemy", "Python Bootcamp", "Functions")
print( m1.full_title())