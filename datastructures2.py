my_tuple= ()
print(my_tuple)

my_tuple= (1,2,3)
print(my_tuple)

my_tuple= ("mouse", 1, 2, 5, 6, 8)
print(my_tuple)

my_tuple= ("mouse", (3,4,7), (5,8,9))
print(my_tuple[2][1])

my_tuple= ("mouse", 3, 4, 7, 9)
print(my_tuple[1:4])

my_tuple= ('p','l','k','j','r','t')
for letter in my_tuple:
    print("Hello", letter)

my_set= {1,2,2,3,4,4,4}
print(my_set)

my_set= {1,2,2,3,4,4,4}
my_set.add(5)
print(my_set)

my_set= {1,2,2,3,4,4,4}

set1= my_set
set2= {2,4,6,6}

print(set1.difference(set2))
print(set1.symmetric_difference(set2))

setx= {"blue", "green"}
sety= {"green", "yellow"}

setz= setx.intersection(sety)
print(setz)

setw= setx.union(sety)
print(setw)