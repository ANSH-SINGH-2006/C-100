import random
class Car(object):
    def __init__(self):
        self.speed= 12
        self.engineType= 123
        self.color= 33
        self.brand="brand"
    
    def randomSpeed1(self):
        self.speed= random.randint(30, 120)
        print("Speed: "+str(self.speed))

    def engineType1(self):
        self.engineType= random.randint(1, 3)
        print("Engine Type: ",self.engineType)

    def color1(self):
        rgbl=[255,0,0]
        random.shuffle(rgbl)
        self.color=tuple(rgbl)
        print(str(self.color))

    def brand1(self):
        self.brand="XYZ BRAND"
        print(self.brand)

abc=Car()
abc.randomSpeed1()
abc.engineType1()
abc.color1()
abc.brand1()