#lists in python
fruits = ["apple", "banana", "cherry"]
mix_list = [1, "hello", 3.14, True]
my_list  = [1, 2, 3, 4, 5]
 #accessing elements
 #we can access elements using indexing
print(fruits[1])#accessing banana
print(mix_list[2])#accessing 3.14
print(my_list[-1])#accessing 5
print(fruits[1:2])#slicing

#we can also modify elements
fruits[0] = "orange"#modifying apple to orange
print(fruits)
my_list.append(6)#adding 6 to the end of my_list
print(my_list)
mix_list.insert(1, "world")#inserting "world" at index 1
print(fruits)
my_list.remove(4)#removing 4 from my_list
print(my_list)
mix_list.pop()#removing last element from mix_list
print(mix_list)
mix_list.pop(1)#removing element at index 1
print(mix_list)
mix_list.clear()#clearing all elements from mix_list
print(mix_list)
 
#slice assignment
a = [1, 2, 3, 4, 5]
print(a[1:4])#prints [2, 3, 4]
print(a[:4])#prints [1, 2, 3, 4]
print(a[2:])#prints [3, 4, 5]
print(a[:])#prints [1, 2, 3, 4, 5]
print(a[::2])#prints [1, 3, 5]
print(a[1::2])#prints [2, 4]

#list functions and methods
print(len(fruits))#length of fruits list
print(max(my_list))#maximum value in my_list
print(min(my_list))#minimum value in my_list
numbers = [3, 1, 4, 1, 5, 9]
print(numbers)
print(sorted(numbers))#sorted list
print(sum(numbers))#sum of elements in numbers list
print(fruits.index("banana"))#index of banana in fruits list
numbers2 = [2, 7, 1, 8, 2, 1, 1, 2, 2]
print(numbers2.count(2))#count of 2 in numbers2 list
print(numbers2.count(1))#count of 2 in numbers2 list
fruits.reverse()#reversing fruits list
print(fruits)
numbers2.sort()#sorting numbers2 list
print(numbers2)
#nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])#prints [1, 2, 3]
print(matrix[1][2])#prints 6
matrix[2][0] = 10#modifying 7 to 10
print(matrix)
