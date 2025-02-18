numberLargest=int(input("Please enter a larger number:"))
numberSmallest=int(input("Please enter a smaller number:"))

while (numberSmallest):
    numberCurrent=numberSmallest
    numberSmallest=numberLargest % numberSmallest
    numberLargest=numberCurrent
    
print(numberLargest)