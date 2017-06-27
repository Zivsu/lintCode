# Check a positive number is a palindrome or not.
# A palindrome number is that if you reverse the whole number 
# you will get exactly the same number.

def palindrome_number(num):
    return (int(str(num)[::-1]) == num) 

