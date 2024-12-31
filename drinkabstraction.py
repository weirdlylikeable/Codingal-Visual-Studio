class Drink:
    def drink(self):
        pass

class Water(Drink):
    def drink(self):
        print("I am a necessity.")

class Pepsi(Drink):
    def drink(self):
        print("I am a fizzy drink.")

class OrangeJuice(Drink):
    def drink(self):
        print("I am a refreshing juice.")

class Milkshake(Drink):
    def drink(self):
        print("I am a calorie-filled drink.")

w = Water()
w.drink()
p = Pepsi()
p.drink()
oj = OrangeJuice()
oj.drink()
ms = Milkshake()
ms.drink()