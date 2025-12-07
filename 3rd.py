#converting user entered data into type conversion
name = input("Enter your name >> ")
age = int(input("Enter your age >> "))

#displaying output to console 
print("hello "+ name + " you are " + str(age) + " years old.")
#or
print(f"hello,  {name} your age {age} years old.")

# common string operations
#1.concateration
First_name = "Rachith"
Last_name = "Kumar"
Full_name = First_name + " "  + Last_name
print(Full_name)

#2.repetition
print(Full_name* 3)
 #or
greeting = "   hello   " * 3
print(greeting)

#string methods
print(Full_name.upper())
print(Full_name.lower())
print(Full_name.title())
print(Full_name.strip())
a = Full_name.replace("Rachith", "Rishi")
print(a) 

print(len(Full_name))

print("#accessing characters in string") #accessing characters in string
print(Full_name[0])  #first character
print(Full_name[-1]) #last character
print(Full_name[0:6]) #slicing
print(Full_name[6]) #slicing
print(Full_name[7:12]) #slicing

print("#escape sequences")#escape sequences
print("Hello\nWorld") #new line
print("Hello\tWorld") #tab space
print("He said, \"Hello World\"") #double quotes
