file=open('Codingal.txt', 'r')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

for line in file:
    print(line)
file.close()