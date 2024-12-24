def recur_factorial(n):
    if n == 1:
        return n
    else:
        return 
num=int(input("Please enter a number"))

if num < 0:
    print("Factorials do not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else: 
    print("The factorial of the number ", num, "is", recur_factorial(num))