file=open('Codingal.txt', 'r')
print(file.read())
file.close()
file=open('Codingal2.txt', 'a')
file.write("I'm just a kid")
file.close()
file=open('Codingal.txt', 'w')
file.write('Hi')
file.close()