print("PRess 1 to Add")
print("prtess 2 to subtract")
print("presds 3 to multiply")
print("press 4 ot divide")

def add():
    a = float(input("enter num:"))
    b = float(input("enter  num:"))
    print(a+b)

def subtract():
    a = float(input("enter f num:"))
    b = float(input("enter num:"))
    print(a-b)

def multiply():
    a = float(input("enter num:"))
    b = float(input("enter num:"))
    print(a*b)

def divide():
    a = float(input("enter num:"))
    b = float(input("enter num:"))
    if b <= 0:
        print("The number cannot be divided.")

Running = True

while Running:
    choice = int(input("etner your number:"))

    if choice == 1:
        add()
    
    elif choice == 2:
        subtract()
    
    elif choice == 3:
        multiply()
    
    elif choice == 4:
        divide()