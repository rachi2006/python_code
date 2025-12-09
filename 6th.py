#tuples and sets in python:
print("\nTuples and Sets in Python")
my_tuple = ("apple", "banana", "cherry")# Creating a tuple
number_tuple = (10, 20, 30, 40, 50)# Creating another tuple
print("Tuple 1:", my_tuple)
print("Tuple 2:", number_tuple)

# Accessing elements in a tuple
print("\naccessing elements in a tuple:")
print(my_tuple[1])# Accessing the second element
print(number_tuple[3])# Accessing the fourth element
print(my_tuple[-1])# Accessing the last element

#slicing tuples
print("\nslicing tuples:")
print(number_tuple[1:4])# Slicing from index 1 to 3
print(my_tuple[:2])# Slicing from start to index 1

#tuple operations
print("\ntuple operations:")
combined_tuple = my_tuple + ("date", "elderberry")# Concatenation
print("Combined Tuple:", combined_tuple)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2# Concatenation of two tuples
print("Tuple 3:", tuple3)
repeted_tuple1 = tuple1 * 4# Repetition of tuple1
print("Repeted Tuple 1:", repeted_tuple1)
print("apple" in my_tuple)# Membership test
print("mango" in my_tuple)# Membership test

#tuple methods
print("\ntuple methods:")
a = (5, 10, 15, 20, 25, 10, 30)
print("Count of 10 in tuple a:", a.count(10))# Counting occurrences of 10
print("Index of 20 in tuple a:", a.index(20))# Finding index of 20

# Creating a set
print("\nCreating a set:")
my_set = {"apple", "banana", "cherry"}
print("Set:", my_set)
numbers_set = {10, 20, 30, 40, 50}
print("Numbers Set:", numbers_set)

#set operations
print("\nset operations:")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)# Union
print("Intersection:", set1 & set2)# Intersection
print("Difference (set1 - set2):", set1 - set2)# Difference
print("Symmetric Difference:", set1 ^ set2)# Symmetric Difference

#set methods
print("\nset methods:")
set1.add(5)# Adding an element
print("Set after adding 5:", set1)
set2.remove(3)# Removing an element
print("Set2 after removing 3:", set2)
set1.pop()# Removing an arbitrary element
print("Set1 after popping an element:", set1)
set2.clear()# Clearing the set
print("Set2 after clearing:", set2)
