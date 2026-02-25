#Multiple Inheritance
class Phone:
    def make_call(self, number):
        self.number=number
        return f"Calling {self.number}"
class MusicPlayer:
    def play_song(self, song):
        self.song=song
        return f"Playing {self.song}"
class SmartDevice(Phone, MusicPlayer):
    def __init__(self):
        Phone.__init__(self)
        MusicPlayer.__init__(self)
s1 = SmartDevice()
print( s1.make_call("123"))
print(s1.play_song("Imagine"))



class Book:
    def read_page(self, page):
        return f"Reading page {page}"

class BatteryPowered:
    def battery_status(self, level):
        return f"Battery at {level}%"

class EBookReader(Book, BatteryPowered):
    pass

e1 = EBookReader()
print( e1.read_page(10))
print(e1.battery_status(80))


class Speaker:
    def speak(self, message):
        return f"Speaking: {message}"
        
class Scheduler:
    def schedule(self, task, time):
        return f"Scheduled {task} at {time}"

class SmartAssistant(Speaker, Scheduler):
        pass

s1 = SmartAssistant()
print( s1.speak("Hi"))
print(s1.schedule("Meeting","10AM"))