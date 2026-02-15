#Hierarchical Inheritance
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