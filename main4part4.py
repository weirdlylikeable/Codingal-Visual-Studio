num=int(input("Enter a number:"))
if num > 1:
    for i in range(2, num+1):  # Check divisibility up to square root of num
        if num % i == 0:
              print("This is not a prime number.")
              break
    else: 
        print("This is a prime number.")
else: ("This is not a prime number.")