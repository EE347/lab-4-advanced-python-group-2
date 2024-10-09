name = input("Enter Your Name BIatch: ")

with open("task3.txt", "a") as file:
    file.write(name + "\n")