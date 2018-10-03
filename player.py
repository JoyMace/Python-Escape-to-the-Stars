import items#items are the player inventory
import world#player exists in world
import baddies#player interacts with baddies

class Player:
   def __init__(self):
       self.inventory = [items.RayGun(), items.Water(), items.Food(),
                         items.Bandage(),
                         items.HealingPotion()]#items you start with
       self.x = 4#start player at x =4 and y = 4
       self.y = 4
       self.hp = 100#max hp
       self.gold = 5#gold you start with
       self.spacesuit = 0#need to pick up the spacesuit and flashlight, start with none
       self.flashlight = 0
       self.victory = False#victory only true on victory tile

   def is_alive(self):#alive if HP over 0
      return self.hp > 0
  
   def print_inventory(self):#format of inventory
       print("\nInventory:")
       for item in self.inventory:
           print('* ' + str(item))
       print('Gold: {}'.format(self.gold))
       print('Space Suit: {}'.format(self.spacesuit))
       print('Flashlight: {}'.format(self.flashlight))
       
       

   def most_powerful_weapon(self):#if more than one weapon, attacks with best weapon
      max_damage = 0
      best_weapon = None
      for item in self.inventory:
         try:
            if item.damage > max_damage:
               best_weapon = item
               max_damage = item.damage
         except AttributeError:#if item in inventory isn't a weapon, pass over it
            pass
      return best_weapon

   def move(self, dx, dy):#dx is change in x, dy is change in y
       self.x += dx
       self.y += dy

   def move_north(self):#north = negative y direction
       self.move(dx=0, dy=-1)

   def move_south(self):#south = positvie y direction
       self.move(dx=0, dy=1)

   def move_east(self):#east is positive x direction
       self.move(dx=1, dy=0)

   def move_west(self):#west is negative x direction
       self.move(dx=-1, dy=0)

   def modify_player(self, player):#if baddie is alive, it is attacking
      if self.baddie.is_alive():
         player.hp = player.hp - self.baddie.damage#baddie reduces your HP
         print('\nBaddie does {} damage. You have {} HP remaining.'.format(self.baddie.damage, player.hp))

   def look(self):
      print (room.description)#look around
   
   def attack(self):#if you choose to attack a baddie, pick best weapon, attack baddie on tile
      best_weapon = self.most_powerful_weapon()
      room = world.tile_at(self.x, self.y)
      baddie = room.baddie
      print ('\nYou use {} against {}!'.format(best_weapon.name, baddie.name))
      baddie.hp -=best_weapon.damage
      if not baddie.is_alive():
         print('\nThe {} has been defeated!'.format(baddie.name))
      else:
         print('\nThe {} still has {} HP. Attack again!'.format(baddie.name, baddie.hp))

   def heal(self):#healing method
      consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
#checks inventory for consumables
      if not consumables:
         print('You do not have any items that will heal you!')
         return#exits method if no consumables
#which consumable to use, if multiple items available
      for i, item in enumerate(consumables, 1):
         print('Choose an item to use for healing: ')
         print('{}. {}'.format(i, item))

      valid = False
      while not valid:#looks through inventory, finds consumable, accepts input of choice
         #applies healing, removes from inventory
         choice = input('')
         try:
            to_eat = consumables[int(choice) - 1]
            self.hp = min(100, self.hp + to_eat.healing_value)#caps player HP at 100
            self.inventory.remove(to_eat)
            print('Current HP: {}'.format(self.hp))
            valid = True
         except (ValueError, IndexError):#if input invalid, prompt to make another choice
            print('Invalid choice, try again.')
            

   def wearSuit(self):#have spacesuit? wear if yes, if no, don't 
      spacesuit = self.spacesuit 
      if not spacesuit:
         print('You do not have a Space Suit! You must find one!')
         return
      

  
            
      

   
                  
         
