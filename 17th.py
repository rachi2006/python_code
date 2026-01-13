#Getters, Setters, Method Overloading & Overriding, super(), Abstract Classes
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # Private attribute

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validation
            self.__age = age
        else:
            print("Invalid age")

# Usage
student = Student("Anita", 20)
print("Age:", student.get_age())  # Accessing age with getter
student.set_age(21)  # Modifying age with setter
print("Updated Age:", student.get_age())


print("\n")
#method overloading
class MathOperation:
    def add(self, a, b , c = 0):
        return a+b+c#handles both 2 and 3 parameter cases
math = MathOperation()
print("sum of 2 numbers :", math.add(5, 10))
print("sum of 3 numbers :", math.add(5, 10, 15))

print("\n")
#method overriding
class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")  # Overrides the parent class method

# Usage
animal = Animal()
animal.sound()
dog = Dog()
dog.sound()  # Calls the overridden method in Dog class
print("\n")

#super() function
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the parent class's __init__ method
        self.breed = breed

    def sound(self):
        super().sound()  # Calling the parent class's sound method
        print(f"{self.name} barks")

# Usage
dog = Dog("Buddy", "Labrador")
dog.sound()


print("\n")
# Abstract Classes
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method with no implementation

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

# Usage
car = Car()
car.start_engine()
