def is_palindrome(string):
    left_position = 0
    rigt_position = len(string)-1

    while rigt_position >= left_position:
        if string[left_position] != string[rigt_position]:
            return False

        left_position +=1
        rigt_position -=1

    return True
    
print("IS this palinderome?")
print(is_palindrome(input("Enter The word:")))