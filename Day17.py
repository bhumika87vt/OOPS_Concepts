#Encapsulation
#Protected Access

class Product:
    def __init__(self, name, stock):
        self.name=name
        self._stock=stock
    def sell(self, quantity):
        if quantity<=self._stock:
            self._stock-=quantity
            return f"Sold {quantity} units of {self.name}"
        else:
            return "Insufficient stock"
    def get_stock(self):
        return self._stock
p = Product("Laptop", 10)    
p.sell(3)   
p.sell(8)   
print(p.get_stock())


class SavingsAccount:
    def __init__(self, initial_balance):
        self._balance=initial_balance

    def add_interest(self):
        interest=self._balance*5/100
        self._balance+=interest
        return self._balance
        
s1 = SavingsAccount(100)
print( round(s1.add_interest(), 2))


class Student:
    def __init__(self, name):
        self.name=name
        self._grade=0

    def update_grade(self, new_grade):
        if new_grade>self._grade:
            self._grade=new_grade
        return self._grade

s1 = Student("Bob")
print( s1.update_grade(80))


class Employee:
    def __init__(self, name):
        self.name=name
        self._access_count=0
        
    def log_access(self):
        self._access_count+=1
        return self._access_count
        
e1 = Employee("A")
print( e1.log_access())