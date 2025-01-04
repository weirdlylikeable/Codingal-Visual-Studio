file=open('Codingal.txt', 'r')
counter=0
contents=file.read()
colist=contents.split("\n")
for i in colist:
    if i:
        counter+=1

print(counter)