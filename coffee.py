from random import *
class coffee:
    total_cost=0


class sort():
    def __init__(self,name,agr,massa):
        self.name =name
        self.agr=agr
        self.masse=massa
        self.cost=randint(300,1500)
        
class coffee1():
    def __init__(self,sort,sost):
        self.sort=sort
        self.sost=sost
        self.mass=randint(20,40)
        self.cost=randint(300,1500)
    def info(self):
        print("сорт: ",self.sort)#1
        print("состояние: ", self.sost)
        print("масса: ",self.mass)
        print("цена: ", self.cost)

class coffee2():
    def __init__(self, sort, sost):
        self.sort = sort
        self.sost = sost
        self.mass = randint(20, 40)
        self.cost = randint(300, 1500)

    def info(self):
        print("сорт: ", self.sort)  # 2
        print("состояние: ", self.sost)
        print("масса: ", self.mass)
        print("цена: ", self.cost)

class coffee3():
    def __init__(self, sort, sost):
        self.sort = sort
        self.sost = sost
        self.mass = randint(20, 40)
        self.cost = randint(300, 1500)

    def info(self):
        print("сорт: ", self.sort)  # 3
        print("состояние: ", self.sost)
        print("масса: ", self.mass)
        print("цена: ", self.cost)

class coffee4():
    def __init__(self, sort, sost):
        self.sort = sort
        self.sost = sost
        self.mass = randint(20, 40)
        self.cost = randint(300, 1500)

    def info(self):
        print("сорт: ", self.sort)  # 4
        print("состояние: ", self.sost)
        print("масса: ", self.mass)
        print("цена: ", self.cost)

class coffee5():
    def __init__(self, sort, sost):
        self.sort = sort
        self.sost = sost
        self.mass = randint(20, 40)
        self.cost = randint(300, 1500)

    def info(self):
        print("сорт: ", self.sort)  # 5
        print("состояние: ", self.sost)
        print("масса: ", self.mass)
        print("цена: ", self.cost)