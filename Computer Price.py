class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Sellin' price {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice = price
C = Computer()
C.sell()
C.__maxprice = 2000
C.sell()
C.setmaxprice(2000)
C.sell()