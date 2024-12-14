Fruit = ['Apple', 'Banana', 'Orange', 'Guava', 'Peach']

newFruit = Fruit.append('Pear')
print("A fruit has been added to the list:", Fruit)

removeFruit = Fruit.remove('Guava')
print("A fruit has been removed from a list:", Fruit)

lengthFruit = len(Fruit)
print("Length of the list of Fruits:", lengthFruit)

popFruit = Fruit.pop(1)
print("A fruit has been popped from the list:", popFruit)

firstFruit = Fruit[0]
print("This is the first fruit in the list:", firstFruit)

lastFruit = Fruit[-1]
print("This is the last fruit in the list:", lastFruit)

sortFruit = Fruit.sort()
print("This is now a sorted list:", Fruit)

reverseFruit = Fruit.reverse()
print("The list is now reversed:", Fruit)

slicingFruit = Fruit[0:2]
print("The list is now sliced:", slicingFruit)

multiplyFruit = Fruit*4
print("The list is now multiplied:", multiplyFruit)