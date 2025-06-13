# Dictionary provided
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Take user input
key = int(input("Enter a key (1-6): "))

# Check and print the value
if key in d:
    print(f"The value for key {key} is {d[key]}")
else:
    print("Key not found.")
