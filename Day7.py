#Polymorphism
class Payment:
    def pay(self):
        print("Paid using cash")

class GooglePay(Payment):
    def pay(self):
        print("Paid using Google Pay")

class PhonePe(Payment):
    def pay(self):
        print("Paid using PhonePay")

class CreditCard(Payment):
    def pay(self):
        print("Paid using credit card")

P=Payment()
P.pay()
Gpay=GooglePay()
Gpay.pay()
Ph=PhonePe()
Ph.pay()
CC=CreditCard()
CC.pay()

#Abstraction
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass 

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
    
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started")

car=Car()
car.start_engine()

bike=Bike()
bike.start_engine()

bus=Bus()
bus.start_engine()