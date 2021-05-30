from random import *
age = {1: '3-7 лет', 2: '5-10 лет', 3: '8-14 лет'}


class room:
    total_cost = 0


class toy1():
    count=0
    def __init__(self,name):
        self.name=name
        self.cost = randint(400, 2000)
        self.group ='3-7 лет'
        total_cost = self.cost
        toy1.count +=1
    def info(self):
        print("имя: ", self.name)
        print("cost: " ,self.cost)
        print("group: " , self.group)
        print("amount: " , toy1.count)
        print("\\\\")
        print("\\\\")

class toy2():
    count=0
    def __init__(self,name):
        self.name =name
        self.cost = randint(400, 2000)
        self.group ='5-10 лет'
        total_cost = self.cost
        toy2.count +=1
    def info(self):
        print("имя: ",self.name)
        print("cost: ", self.cost)
        print("group: ", self.group)
        print("amount: ", toy2.count)
        print("\\\\")
        print("\\\\")

class toy3():
    count=0
    def __init__(self,name):
        self.name =name
        self.cost = randint(400, 2000)
        self.group ='8-14 лет'
        total_cost = self.cost
        toy3.count +=1
    def info(self):
        print("имя: ",self.name)
        print("cost ", self.cost)
        print("group ", self.group)
        print("amount ", toy3.count)
        print("\\\\")
        print("\\\\")


cat1=toy1("занавеска")
cat1.info()

cat2= toy2("гладильная доска")
cat2.info()

cat3=toy3("кресло-качалка")
cat3.info()
