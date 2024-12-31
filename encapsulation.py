class computer:
    
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print(f"Selling price of computer is: {self.__maxprice}")

    def setMaxPrice(self,price):
        self.__maxprice = price

comp1= computer()

comp1.sell()
comp1.setMaxPrice(1000)
comp1.sell()