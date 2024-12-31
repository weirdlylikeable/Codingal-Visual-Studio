class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def make_sound(self):
        print("I am a dog, I can bark.")

class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def make_sound(self):
        print("I am a cat, I can meow.")

dog1= Dog("Happy", 6.5)
cat1= Cat("Lucky", 4)

for i in (dog1,cat1):
    i.make_sound()