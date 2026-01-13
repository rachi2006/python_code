def add(*a):
    return sum(a)

print(add(1, 102, 2))

students = [
    {"name": "Rachith", "marks": 50},
    {"name": "Trisha", "marks": 92},
    {"name": "Kumar", "marks": 78}
]
students.sort(key= lambda x : x["marks"], reverse = True)
print(students)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
