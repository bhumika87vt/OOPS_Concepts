#Polymorphism->Methodoverriding

class RoyalMessenger:
    def deliver(self, message):
        return f"Delivered: {message}"
        
class UrgentMessenger(RoyalMessenger):
    def deliver(self, message):
        return f"URGENT: Delivered: {message}"

# Example usage
royal = RoyalMessenger()
urgent = UrgentMessenger()
print(royal.deliver("Your taxes are due."))
print(urgent.deliver("Enemy at the gates!"))


class Robot:
    def communicate(self):
        return "Beep beep."

class ExplorerRobot(Robot):
    def communicate(self):
        return "Exploring new planets!"

r = Robot()
e = ExplorerRobot()
print(r.communicate())
print(e.communicate())


class Appliance:
    def status(self):
        return "Appliance is off."

class SmartAppliance(Appliance):
    def status(self):
        return "Appliance is on and connected."

a = Appliance()
s = SmartAppliance()
print(a.status())
print(s.status())