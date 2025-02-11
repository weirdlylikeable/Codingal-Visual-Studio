def sum(n):
    return (n*(n-1))/2

print(sum(6))

def arraysum(n):
    total=0
    for i in n:
        total=total+i
    return total

a= [12,15,19,7]
print(arraysum(a))

def summ(n):
    if (n<=0):
        return 0
    else:
        return n + summ(n-1)

print(summ(6))