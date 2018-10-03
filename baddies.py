#baddies to fight you on your way to escape
class Baddie:#superclass
    def __init__(self):
        raise NotImplementedError('Do not create raw Baddie objects')
#can't make a "baddie" baddie
    def __str__(self):
        return self.name
    def is_alive(self):#baddie alive until HP =<0
        return self.hp > 0

class GreenAlien(Baddie):#subclass Baddie
    def __init__(self):
        self.name = 'Green Googly Eyed Alien'
        self.hp = 15#how many HP baddie has
        self.damage = 1#how much damage baddie does
        
 
class BlueFluff(Baddie):
    def __init__(self):
        self.name = 'Blue Fluffy Fury'
        self.hp = 20
        self.damage = 10
        

class MommaAlien(Baddie):
    def __init__(self):
        self.name = 'Big Green Momma'
        self.hp = 30
        self.damage = 10

class RolyPoly(Baddie):
    def __init__(self):
        self.name = 'George the Giant Roly Poly'
        self.hp = 50
        self.damage = 10
        
        
class ROUS(Baddie):
    def __init__(self):
        self.name = 'R.O.U.S.'
        self.hp = 1000
        self.damage = 1000
