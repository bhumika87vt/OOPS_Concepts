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


#2nd
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