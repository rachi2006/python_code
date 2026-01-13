#the pillars of oop
#1. Encapsulation
#2. Inheritance
#3. Polymorphism
#4. Abstraction

#. Encapsulation: wrapping data and methods into a single unit
class ATM:
    def __init__(self, balence):#you can also make default balence by seetting balence = 0;
        self.__balence = balence #private attribute

    def deposite(self, amount):
        self.__balence += amount
        print(f"Deposited: {amount}. New balence: {self.__balence}")    
    
    def withdraw(self, amount):
        if amount <= self.__balence:
            self.__balence -= amount
            print(f"Withdrawn: {amount}. New balence: {self.__balence}")
        else:
            print("Insufficient funds")

atm = ATM(500)
atm.deposite(500)
atm.withdraw(200)            

#abstraction: hiding complex implementation details and showing only the necessary parts
class car:
    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Car is accelerating")    

    def brake(self):    
        print("Car is stoping")

car = car()
car.start_engine()
car.accelerate()
car.brake()

class Database:
    def __init__(self):
        self.__storage = {}

    def save_data(self, key, value):
        self.__storage[key] = value
        print(f"Data saved for {key}")

    def get_data(self, key):
        return self.__storage.get(key, "No data found")

db = Database()
db.save_data("user_101", {"name": "Raj", "age": 30})
print(db.get_data("user_101"))






# Inheritance: deriving new classes from existing ones
class Family:
    def __init__(self, surname):
        self.surname = surname

class Child(Family):
    def __init__(self, surname, name):
        super().__init__(surname)
        self.name = name

child = Child("Gowda", "Ajay")
print(f"{child.name} {child.surname}")  # Inherits surname from Family


print("\n")

class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in")

class Admin(User):
    def delete_user(self, user):
        print(f"Admin {self.username} deleted user {user}")

admin = Admin("karnataka_admin")
admin.login()  # Inherited from User
admin.delete_user("user_102")  # Admin-specific method

print("\n")

# Polymorphism: ability to take many forms
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()

    print("\n")

class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")

notifications = [EmailNotification(), SMSNotification()]
for notification in notifications:
    notification.send()
