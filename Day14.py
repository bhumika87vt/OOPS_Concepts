#Single Level Inheritance
class Employee:
    def __init__(self, name, base_salary):
        self.name=name
        self.base_salary=base_salary
class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name,base_salary)
        self.bonus=bonus
    def calculate_salary(self):
        total_salary=self.base_salary+self.bonus
        return total_salary
d1 = Developer("A", 40000, 5000)
print( d1.calculate_salary())


class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        super().__init__(name,price)
        self.discount_percent=discount_percent
    def get_discounted_price(self):
        discount=self.price/100*self.discount_percent
        return self.price-discount
p1 = DiscountedProduct("Phone", 10000, 10)
print( p1.get_discounted_price())


class Vehicle:
    def __init__(self, vehicle_type, speed):
        self.vehicle_type=vehicle_type
        self.speed=speed
class Flight(Vehicle):
    def __init__(self, vehicle_type, speed, flight_number, duration):
        super().__init__(vehicle_type,speed)
        self.flight_number=flight_number
        self.duration=duration
    def flight_summary(self):
        return f"Flight {self.flight_number} ({self.vehicle_type}) travels at {self.speed} km/h for {self.duration} hours"

f1 = Flight("Airbus", 700, "A123", 3)
print( f1.flight_summary())