num = int(input("Enter your number:"))

for i in range(2, num):
    if  num % i == 0:
        is_prime = 0
        break

if is_prime == 1:
    print("Prime number")

else:
    print("Composite number")