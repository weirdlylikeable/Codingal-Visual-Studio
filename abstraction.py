class Animal:
    def move(self):
        pass

class Snake(Animal):
    def move(self):
        print("I can crawl.")

class Dog(Animal):
    def move(self):
        print("I can bark.")

class Lion(Animal):
    def move(self):
        print("I can roar.")

class Human(Animal):
    def move(self):
        print("I can walk.")

s = Snake()
s.move()
d = Dog()
d.move()
l = Lion()
l.move()
h = Human()
h.move()