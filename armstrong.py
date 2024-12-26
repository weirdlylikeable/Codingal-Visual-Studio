def armstrong_num(num):
    digits=str(num)
    power=len(digits)
    total=sum(int(digit)** power for digit in digits)
    return total==num

number= int(input("Enter a number to check if it is an Armstrong number:"))
if armstrong_num(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")