#for loop in python
for i in range(5):
    print("Iteration:", i)

print("\n")
#Let’s print each name in a list of Kannada cities:
kannada_cities = ["Bengaluru", "Mysuru", "Mangaluru", "Hubballi", "Belagavi"]
for city in kannada_cities:
    print("City:", city)


print("\n")
    #Looping Over Strings
word = "Python"
for letter in word:
    print("Letter:", letter)


print("\n")

#Nested for loop to print multiplication table from 1 to 5
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  # To print an empty line after each table


print("\n")

#Real-Life Example: Distributing Laddus
laddus = 5
friends = ["Rahul", "Sneha", "Aman", "Priya", "trisha", "Rachith"]

for friend in friends:
    if laddus > 0:
        print(f"{friend} gets a laddu!")
        laddus -= 1
    else:
        print("No laddus left!")
