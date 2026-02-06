#Hierarchical Inheritance
'''class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.amount=amount
        self.balance+=amount
        print(f"Deposit:{amount}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdraw:{amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Balance:{self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance,interest_rate):
        super().__init__(account_holder,balance)
        self.interest_rate=interest_rate

    def add_interest(self):
        interest=self.balance*self.interest_rate/100
        self.balance+=interest
        print(f"Interest is:{interest}")

class CurrentAccount(BankAccount):
    def __init__(self,account_holder,balance,overdraft_limit):
        super().__init__(account_holder,balance)
        self.overdraft_limit=overdraft_limit

    def withdraw_with_overdraft(self,amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn {amount} using overdraft")
        else:
            print("Overdraft limit exceeded")

#Savings Account
savings = SavingsAccount("Bhumika", 10000, 5)
savings.deposit(2000)
savings.add_interest()
savings.withdraw(3000)
savings.display_balance()

#Current Account
current = CurrentAccount("Tanu", 5000, 3000)
current.deposit(1000)
current.withdraw_with_overdraft(6500)
current.display_balance()'''

        
#Hybrid Inheritance
class Person:
    def __init__(self,name):
        self.name=name

    def display_person(self):
        print(f"Name:{self.name}")
    
class Student(Person):
    def __init__(self,name,student_id):
        super().__init__(name)
        self.student_id=student_id

    def display_student(self):
        print(f"Student ID:{self.student_id}")

class SportsPlayer(Person):
    def __init__(self,name,sport_name):
        super().__init__(name)
        self.sport_name=sport_name
    
    def display_sports_player(self):
        print(f"Sport Name:{self.sport_name}")

class CollegeStudent(Student,SportsPlayer):
    def __init__(self,name,student_id,sport_name,college_name):
        Person.__init__(self, name)
        self.student_id = student_id
        self.sport_name = sport_name
        self.college_name = college_name

    def display_college_student(self):
        print(f"College Name:{self.college_name}")

college=CollegeStudent("virat",123,"cricket","ABC")
college.display_person()
college.display_student()
college.display_sports_player()
college.display_college_student()
