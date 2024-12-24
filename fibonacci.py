def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n-1) + recur_fibonacci(n-2)
    
for i in range(15):
    print(recur_fibonacci(i))