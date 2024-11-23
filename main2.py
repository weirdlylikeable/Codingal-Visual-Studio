name="Penguin" 
age=15
is_student=True
weight=38.5
print("Name", name)
print("Data Type of Name is", type(name)) 
print("Age", age)
print("Data Type of Age is", type(age))
print("Are they a student ", is_student)
print("Data Type of Is_Student is", type(is_student))
print("What is their weight?", weight)
print("Data Type of Weight is", type(weight))

name=str(name)
print("Data Type of Name is", type(name))
age=int(age)
print("Data Type of Age is", type(age))
weight=int(weight)
print("Dta Type of Weight is", type(weight))

num1=7
num2=3
print("Number 1:", num1)
print("Number 2:", num2)
print("Addition:", num1+num2)
print("Subtrction:", num1-num2)
print("Multiplication:", num1*num2)
print("Division:", num1/num2)
print("Floor Division:", num1//num2)
print("Remainder:", num1%num2)
print("Squared:", num1**2)
print("Square Root:", num1**0.5)

print("Equal?:", num1==num2)
print("Not Equal?:", num1!=num2)
print("Greater Than?:", num1>num2)
print("Less Than?:", num1<num2)

first_name="Codingal"
last_name="Educations"
full_name=first_name+last_name

example="hhhh"*5

print("Multiplied Word:", example)
print("Slicing:", first_name[0:4])

x= input("Enter a number:")
y= input("Enter a number:")

temp = x
x = y
y = temp

print("The value of x is:", x)
print("The value of x is:", y)