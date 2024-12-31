def removeandsort(array1, array2):
    common_values = set(array1) & set(array2)
    array1 = sorted(set(array1) - common_values)
    array2 = sorted(set(array2) - common_values)
    return array1, array2

arr1 = [8,9,6,4,2,1,7,16,19,3]
arr2 = [14,15,6,8,9,5,7,12,11,1]

result1, result2 = removeandsort(arr1, arr2)
print("Sorted and deduplicated array1:", result1)
print("Sorted and deduplicated array2:", result2)