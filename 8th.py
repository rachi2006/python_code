#conditional statements in python
a = int(input("Enter your roll number:"))
if a == 7:
    print("a is your roll number")
else:
    print("a is not your roll number")


time = 15
if time == 8:
    print("it's breakfast time!")
elif time == 13:
    print("it's lunch time!")
elif time == 20:
    print("it's dinner time!")
else:
    print("it's not meal time!")



# Practice Problem: Ticket Pricing Based on Age
age = int(input("Enter your age:"))

if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")
