#These are items you carry or find in the game
class Weapon:#superclass
    def __init__(self):
        raise NotImplementedError('Do not create raw Weapons objects.')#can't create
    #'weapon' weapon
    
    def __str__(self):
        return self.name

class RayGun(Weapon):#subclass of Weapon
    def __init__(self):
        self.name = 'Ray Gun'
        self.description = 'A small gun that rapidly shoots blasts of lasers.'
        self.damage = 10#Ray Gun does 10 damage        
        
class Flashlight(Weapon):
    def __init__(self):
        self.name = 'Flashlight'
        self.description = 'A small electic torch. Very bright when turned on!'
        self.damage = 1#not a good weapon...

class Consumable:#consumables can be used up throughout the game
    def __init__(self):
        raise NotImplementedError('Do not create raw Consumable Objects')

    def __str__(self):
        return '{} (+{} HP)'.format(self.name, self.healing_value)
    
class Water(Consumable):#subclass of Consumable
    def __init__(self):
        self.name = 'Water Bottle'
        self.healing_value = 20#amount it heals

class Food(Consumable):
    def __init__(self):
        self.name = 'Bit of Food'
        self.healing_value = 35

class HealingPotion(Consumable):
    def __init__(self):
        self.name = 'Healing Potion'
        self.healing_value = 100

class Bandage(Consumable):
    def __init__(self):
        self.name = 'Bandage'
        self.healing_value = 50
