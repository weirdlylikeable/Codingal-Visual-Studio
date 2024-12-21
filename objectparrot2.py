class parrot:

    def __init__(self,name,age):

        self.name= name
        self.age = age
    
    def sing(self, sing):
        return "{} is singing {}".format(self.name, sing)
    
    def dance(self,dancing):
        return "{} is dancing to {}".format(self.name, dancing)

Blu = parrot("Blu", 8)

print(Blu.sing("Happy"))
print(Blu.dance("Happy"))