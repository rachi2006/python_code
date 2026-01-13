#while loop in python
i = 1
while i<=10:
    print(i)
    i += 1

#counting sheep
sheep_count = 1
while sheep_count <= 10:
    print(f"{sheep_count} shepp...")
    sheep_count += 1


#usind break to exit while loop
sheep_count = 1
while sheep_count <= 10:
    print(f"{sheep_count} shepp...")
    if sheep_count == 5:
        print("that's enough sheep for now!")
        break
    sheep_count += 1


#Using continue to Skip an Iteration
#to skip counting sheep that are number 4
sheep_count = 1
while sheep_count <= 10:
    if sheep_count == 4:
        sheep_count += 1
        continue
    print(f"{sheep_count} shepp...")
    sheep_count += 1

#by user inputUsing while Loops for User Input
pin = ""
correct_pin = "1234"
trial = 1
while trial <= 3:
    pin = input(f"trials- {trial} |Enter your PIN: ")
    trial += 1
    if pin == correct_pin:
        print("PIN accepted. Access granted.")
        break
    else:
        print("Incorrect PIN. Try again.")
