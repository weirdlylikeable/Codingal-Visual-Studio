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

my_dict= {'name': 'Jack', 'age': 26}

print(my_dict['name'])
print (my_dict.get('age'))

my_dict['age']= 27 
print(my_dict)

my_dict['address'] = 'Downtown' 
print(my_dict)

my_dict.pop('age')
print(my_dict)

def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students= [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
print("\nOriginal list of lists:")
print(students)
print("\nConverted lists to a dictionary: ")
print(test(students))