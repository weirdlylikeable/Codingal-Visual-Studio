def isPal(value):
    value_str=str(value)
    return value_str == value_str[::-1]

value=input("Enter a word, phrase or number to be checked:")
if isPal(value):
    print("This string is a palindrome.")
else:
    print("This string isn't a palindrome.")