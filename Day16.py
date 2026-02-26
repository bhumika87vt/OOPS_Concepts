#Encapsulation
#Private Access

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance=initial_balance

    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrawal successful. Remaining balance: {self.__balance}")
        else:
            print(f"Insufficient funds. Balance remains: {self.__balance}")

acc = BankAccount(1000)
acc.withdraw(200)
acc.withdraw(900)


class StudentResult:
    def __init__(self):
        self.__score=0

    def update_score(self, new_score):
        if new_score>self.__score:
            self.__score=new_score
            print(f"Score updated to {new_score}")
        else:
            print(f"New score is lower. Score remains: {self.__score}")

s = StudentResult()
s.update_score(70)


class UserAccount:
    def __init__(self):
        self.__points=0

    def add_points(self, amount):
        if amount>0:
            self.__points+=amount
            return True
        else:
            return False

    def get_points(self):
        return self.__points

u1 = UserAccount()
u1.add_points(10)
print( u1.get_points())


class FlightSeat:
    def __init__(self):
        self.__is_booked=False

    def book(self):
        if not self.__is_booked:
            self.__is_booked=True
            return "Booking successful"
        else:
            return "Seat already booked"
    def status(self):
        if self.__is_booked:
            return "Booked"
        else:
            return "Available"
s1 = FlightSeat()
print( s1.status())