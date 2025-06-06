def is_number_palindrome(num):
    num_str = str(num)
    left = 0
    right = len(num_str)- 1

    while right >= left:
        if num_str[left] != num_str[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

print("Is this a palindorme number?")
number = int(input("Enter number:"))
print(is_number_palindrome(number))