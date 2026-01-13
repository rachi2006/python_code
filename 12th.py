"""""
pin = "1234"
trials = 1
while  trials <=3:
    correct_pin = input(f"trail - {trials} || pin : ")
    trials += 1
    if correct_pin == pin:
        print("******entered pin is correct******* ")  
        break
    else:
        print("-----incorrect-------")
"""""

#functons
def greet(boy, girl):
    print(f"boy nameis {boy}")
    print(f"girl name is {girl}")
    print(f"{boy} loves {girl}")
    
greet("Rachith", "Trisha")
a = "rachith"
print(f"hello --- {a}")

print("\n")
def tables(num):
    for i in range(1, 11):
        print(f"{num}x{i} = {num*i}")
    

tables(2)
print("\n")
tables(3)
print("\n")
tables(4)

print("\n")
def frindes(name1, name2,name3):
    print(f"my friends are {name1}, {name2}, {name3}")

frindes("Rachith", "Trisha", "Kumar")
print("\n")

def frindes_list(names):
    for name in names:
        print(f"my friend is {name}")

friends_names = ["Rachith"]
