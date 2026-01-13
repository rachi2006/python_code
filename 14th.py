#starting oop inn python

class car:
    #Atttributes
    def __init__(self, brand, model):
        self.brand = brand #instance variable
        self.model = model #instance variable

        #method
    def display_info(self):
        print(f"car brand: {self.brand}, car model: {self.model}")


#creating object
my_car = car("toyota", "corolla")
my_car.display_info()

print("\n")
print("\n")
print("---------------------------------------------------")
print("creating multiple objects")
print("---------------------------------------------------")

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f" hello, my name is {self.name} and i am {self.age} years old.")

person1 = person("rachith", 20)   
person2 = person("trisha", 19)     

person1.greet()
person2.greet()
