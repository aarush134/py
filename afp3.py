number_str = input("Enter a number: ")

number = int(number_str)
num_digits = len(number_str)

sum_of_powers = 0
temp_number = number
position = num_digits

while temp_number > 0:
    digit = temp_number % 10
    sum_of_powers += digit ** position
    temp_number //= 10
    position -= 1

if sum_of_powers == number:
    print("It is a Disarium number.")

#elif sum_of_poers == number:
    
else:
    print("It is not a Disarium number.")