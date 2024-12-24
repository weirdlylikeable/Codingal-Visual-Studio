arr = [1,5,4,7,8,3]

def bubble_sort(arr):
    lenArr = len(arr)
    swap = False
    for i in range(lenArr-1):
        for j in range((lenArr-1)-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break

bubble_sort(arr)
print(arr)