#learning self keyword in python oop
#constructor 
class className:
    def __init__(self, parameter1, parameter2):
        self.attribute1 = parameter1
        self.attribute2 = parameter2

    def methodName(self):
        print(f"attribute1: {self.attribute1}" and {self.attribute2})

#creating object
obj1 = className("value1", "value2")
obj1.methodName() 
#you can also create multiple object also      
#like obj2 = className("value3", "value4") 
#obj3 = className("value5", "value6") etc.
#obj2.methodName()
#obj3.methodName()
