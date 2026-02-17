#Hybrid Inheritance
class Device:
    def __init__(self, brand):
        self.brand=brand
class VoiceControl(Device):
    def voice_activate(self):
        super().__init__()
        return self.brand
class AppControl(Device):
    def app_activate(self):
        super().__init__()
        return self.brand
class SmartSpeaker(VoiceControl, AppControl):
    def control_methods(self):
        def __init__(self):
            super().__init__()
        return f"{self.brand} can be controlled via voice and app."
s1 = SmartSpeaker("Echo")
print( s1.control_methods())



class User:
    def __init__(self, name, **kwargs):
        self.name=name
class Driver(User):
    def __init__(self, name, car, **kwargs):
        super().__init__(name,**kwargs)
        self.car=car
class Rider(User):
    def __init__(self, name, pickup_location, **kwargs):
        super().__init__(name,**kwargs)
        self.pickup_location=pickup_location
class Trip(Driver, Rider):
    def __init__(self, name, car, pickup_location):
        super().__init__(name=name,car=car,pickup_location=pickup_location)
    def summary(self):
        return f"{self.name} will pick up the rider from {self.pickup_location} using {self.car}."
t1 = Trip("Amit", "Honda City", "Sector 21")
print( t1.summary())



class Product:
    def __init__(self, name, **kwargs):
        self.name=name
class DigitalProduct(Product):
    def __init__(self, name, size, **kwargs):
        super().__init__(name,**kwargs)
        self.size=size
class PhysicalProduct(Product):
    def __init__(self, name, weight, **kwargs):
        super().__init__(name,**kwargs)
        self.weight=weight
class HybridProduct(DigitalProduct, PhysicalProduct):
    def __init__(self, name, size, weight):
        super().__init__(name=name,size=size,weight=weight)
    def details(self):
        return f"{self.name} includes {self.size} digital files and weighs {self.weight}."
hp1 = HybridProduct("Python Mastery", "2GB", "1kg")
print( hp1.details())


class Person:
    def __init__(self, name, **kwargs):
        self.name=name
class Faculty(Person):
    def __init__(self, name, subject, **kwargs):
        Person.__init__(self,name)
        self.subject=subject
    def teach(self):
        return self.subject
class Staff(Person):
    def __init__(self, name, department, **kwargs):
        super().__init__(name)
        self.department=department
    def work(self):
        return self.department
class Administrator(Faculty, Staff):
    def __init__(self, name, subject, department):
        Faculty.__init__(self,name,subject)
        Staff.__init__(self,name,department)
    def profile_data(self):
        return f"{self.name} teaches {self.teach()} and works in {self.work()} department."
a1 = Administrator("Rakesh", "Math", "Operations")
print( a1.profile_data())
