def fun1(n):
    for i in range(1,n+1):
        name="Ayan"
        print (name)
    return name

print (fun1(10))

def fun2(n):
    name="Ayan"
    return (name + "\n")*n

print(fun2(10))

def fun3(n):
    for i in range(1, n+1):
        for j in range(n+1, (n+1)**2):
            name="Ayan"
            return (name + "\n")*n
        
print (fun3(10))