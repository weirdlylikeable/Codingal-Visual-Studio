f1=open('Codingal.txt', 'r')
f2=open('Codingal2.txt', 'a')

f1.seek(0)
f2.seek(0)

file1=f1.read()
file2=f2.write(file1)

f1.close()
f2.close()