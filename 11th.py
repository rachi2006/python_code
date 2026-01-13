#Lists and Dictionaries with For Loops, List Comprehension, and Dictionary Comprehension
l = [21, 34, 56, 34, 65, 78, 90]
dl = []
total = 0
for num in l:
    total = total + num # 0r total = toal + num
    print(total)
    #print("\n")
    #dl.append(num*2)
    #print(dl)

print("\n")
student_marks = {
    "Rachith" : 85,
     "trisha" : 92,
      "kumar" : 78
}
for student in student_marks.values():
    print(student) 
    #if i need only keys = student_marks.keys()
    #if i need only values = student_marks.values()
    #if i need both keys and values = student_marks.items()
#for student, marks in student_marks.items():
#print(f"{student} ----- {marks}")


print("\n")
students = ["Rachith", "trisha", "kumar"]
marks = [85, 92, 78]
student_marks = {}
for index, student in enumerate(students):
    student_marks[student] = marks[index]
print(student_marks)
#or
#for i in range(len(students)):
#student_marks[students[i]] = marks[0]

print("\n")
#List Comprehension
#Double the numbers in the list
l = [1, 2, 3, 4, 5]
dl = [num*2 for num in l]
print(dl)
#squares of numbers
squares = [num**2 for num in l]
print(squares)
#Even numbers from the list
even_numbers = [num for num in l if num%2 == 0]
print(even_numbers)



print("\n")
l = [ x for x in range(1, 11)]
print(l)
rdl = [ x*2 for x in l]
print(rdl)
