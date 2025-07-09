import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempt = random.randint(5,15)

print("Welcom to the number guessing game!")
print(f"You have {max_attempt} tries only!")

while attempts < max_attempt:
    guess = int(input("Enter your guess:"))
    attempts += 1

    if guess < secret_number:
        print("Too low, try a little bit higher!")
    
    elif guess > secret_number:
        print("Too high, try a little bit lower")
    
    else:
        print(f"You got it in {attempts} attempts Congrats!")
        break

else: 
    print(f"The game is over! The number secret number was {secret_number}")