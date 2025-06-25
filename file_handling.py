class file_operation:
    def create_file(self):
        file_name = input("enter the text file name:")
        f = open(file_name, "w")
        f.write(input("enter what do you want top write:"))
        f.close

    def read_files(self):
        file_name = input("enter the name of the text file you want to read:")
        f = open(file_name, "r")
        context = f.read()
        print(context)
        f.close

f1 = file_operation()

print("wellcome to my file operation program")
print("press 1 to create files")
print("press 2 to read files")

running = True

while running:
    choice = int(input("enter your chocie:"))

    if choice == 1:
        f1.create_file()
    
    elif choice == 2:
        f1.read_files()
    
    else:
        print("Invalid choice")
        running = False
        