def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

num1= int(input("Please enter a number:"))
num2= int(input("Please enter a number:"))

print("Addition:", add(num1,num2))
print("Subtraction:", subtract(num1,num2))
print("Multiplication:", multiply(num1,num2))
print("Division:", divide(num1,num2))