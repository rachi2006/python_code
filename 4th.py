#operators
print("Assignment operators")
x = 10#x -=3 x *= 4 x /= 2
x += 5 #assignment operator 
print(x)

 #comparison operators
print("\nComparison operators")
a = 10
b = 20
print( a == b)
print(a > b)#print(a < b), (a >= b), (a <= b), (a != b)

#logical operators
print("\nLogical operators")
a1 = input("enter the number1 : ")
a2 = input("enter the number2 : ")
a3 = input("enter the number3 : ")
print(a1 > a2 and a1 < a3)
print(a1 > a2 or a1 < a3)
print(not(a1 > a2))

#membership operators
print("\nMembership operators")
my_list = [1, 2, 3, 4, 5]
my_string = "Rachith"
print(3 in my_list)
print("R" in my_string)
