class parrot:

    species = "bird"

    def __init__(self,name,age):

        self.name= name
        self.age = age

blu = parrot("Blu", "10")
woo = parrot("Woo", "13") 

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("{} is of age {}".format(blu.name,blu.age))
print("{} is of age {}".format(woo.name,woo.age))

