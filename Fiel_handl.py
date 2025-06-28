with open('Codingal1.txt', 'w') as file:
    file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

with open('Codingal1.txt', 'r') as file:
    data = file.readlines()
print("Words in this file are....")
for line in data:
    word = line.split()
    print(word)