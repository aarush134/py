file = open('Aarush.txt', 'r')
print(file.read())
file.close()

file = open('Aarush.txt', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'a')
file.write(" Hi! I am Coding King and I am 13 yr old.")
file.close()