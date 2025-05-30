a = float(input("Enter your First Number:"))
b = float(input("Enter your Second number:"))

print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
print("press 5 for floor division")
print("press 6 for remainder")
print("press 7 for exponent")
print("press 8 for square root")

choice = int(input("Enter your choice:"))

if choice == 1:
    print("Addition:", a+b)

elif choice == 2:
    print("Subtraction", a-b)

elif choice == 3:
    print("multiplication:", a*b)

elif choice == 4:
    print("division:", a/b)

elif choice == 5:
    print("Floor division:", a//b)

elif choice == 6:
    print("Remainder:", a%b)

elif choice == 7:
    print("Exponent:", a**b)

elif choice == 8:
    x = int(input("Enter a number:"))
    print("Square Root:", x** .5)

else:
    print("Invalid choice😡")
