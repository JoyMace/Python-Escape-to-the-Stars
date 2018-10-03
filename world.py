import random#baddies appear randomly
import baddies#baddies appear on tiles, so we need their attribtues imported
import player#the player is modified on some tiles, and moves on tiles, so we need it imported

class MapTile:#main class of tile
    def __init__(self, x, y):#initiates at a specified location
        self.x = x
        self.y = y

    def intro_text(self):#text that prints every time you enter the tile
        raise NotImplementedError('Create a subclass instead!')#so you can't try to do just MapTile, have to specify which kind

    def modify_player(self, player):
        pass#do not call method unless on enemy tile
    
class StartTile(MapTile):#You start here. Subclass of MapTile, so automatically gets MapTile attribtues like __init__        
    def intro_text(self):
        return '''\nYou are in an Observatory.\n'''

class SpaceSuitTile(MapTile):#Tile where you get the spacesuit. Can't escape to the stars without it
    def __init__(self, x, y):
        self.spacesuit = 1
        self.spacesuit_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):#when you pass over this tile, you claim the spacesuit, but only once, then it is consumed
        if not self.spacesuit_claimed:
            self.spacesuit_claimed = True
            player.spacesuit = player.spacesuit + self.spacesuit
            print("You picked up the Space Suit")

    def intro_text(self):#if the spacesuit has been claimed already, it will be gone, otherwise it will be there
        if self.spacesuit_claimed:
            return '''\nNothing to see here!'''
        else:
            return '''\nYou found a Space Suit: made from material suitable for space travel!'''
    

class FlashlightTile(MapTile):#same deal as spacesuit tile
    def __init__(self, x, y):
        self.flashlight = 1
        self.flashlight_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.flashlight_claimed:
            self.flashlight_claimed = True
            player.flashlight = player.flashlight + self.flashlight
            print("You turn on the Flashlight! Now you can see!")

    def intro_text(self):
        if self.flashlight_claimed:
            return '''\nNothing to see here!'''
        else:
            return '''\nYou found a Flashlight. It is a small electric torch, but the beam is super bright!'''
    
        

class UseSpacesuitTile(MapTile):#when youpass over this tile you 'use' the spacesuit
    def intro_text(self):
        return '''You put on the Spacesuit!'''      
        
    

class VictoryTile(MapTile):#when you pass over this tile, the game ends
    def modify_player(self, player):
        player.victory = True
        
    def intro_text(self):
        return '''\nYou see a rocket ship primed and ready to launch! You're saved!'''
    

class DoorTileN(MapTile):#door tiles indicate the passage from room to room, one tile for each unique door
    def intro_text(self):
        return '''\nYou enter the North Room. There are scratches covering the walls\n
and a foul smell. Be careful!'''#into text is also room description

class DoorTileS(MapTile):
    def intro_text(self):
        return '''\nYou enter the South Room.\n
It looks like someone used to sleep in here. There is a bed and a closet.\n
There is a door to the North, where you came in.'''

class DoorTileE(MapTile):
    def intro_text(self):
        return '''\nYou enter the East Room. This looks more like a hallway than a room.\n
Maybe the exit is nearby! There is a door to the east...'''

class DoorTileW(MapTile):
    def intro_text(self):
        return '''\nYou enter the West Room. There are empty shelves and diagrams on the walls.\n
Everything has been destroyed by something... or someone...!'''

class DoorTileV(MapTile):
    def intro_text(self):
        return '''\nYou enter the Final room. To the East the room opens up into a large launch pad area!\n
This is it!'''
      

class BaddieTile(MapTile):#baddies randomly appear on tiles
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:#appears 50% of the time
            self.baddie = baddies.GreenAlien()#name of baddie
            self.alive_text = '\nA Green Alien snarls from the darkness!'#if alive, return this text
            self.dead_text = '\nThe Green Alien lies still.'#if dead, return this text
                
        elif r < 0.80:
            self.baddie = baddies.BlueFluff()
            self.alive_text = '\nIt looks... fluffy but furious!\nIt is a Blue Fluff! Watch out!'
            self.dead_text = '\nWhat a shame to have killed something so cute...'
                
        elif r < 0.95:
            self.baddie = baddies.MommaAlien()
            self.alive_text = '\nMomma Alien knows what you did! She looks murderous!'
            self.dead_text = '\nThe Momma Alien lies still.'
                
        else:
            self.baddie = baddies.RolyPoly()
            self.alive_text = '\nA giant Roly Poly rolls into view!'
            self.dead_text = '\nGeorge has rolled for the last time.'

        super().__init__(x, y)#calls for super class attributes

    def intro_text(self):
        text = self.alive_text if self.baddie.is_alive() else self.dead_text#this determines which intro text to return
        return text

    def modify_player(self, player):#baddie can damage you
        if self.baddie.is_alive():
            player.hp = player.hp - self.baddie.damage
            print('\n{} does {} damage. You have {} HP remaining!'
                  .format(self.baddie.name,self.baddie.damage, player.hp))#displays damage done, HP left

class FindGoldTile(MapTile):#tile with gold on them, but only once
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):#allows your gold inventory to grow
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return '''\nNothing to see here!'''
        else:
            return '''\nYou found some gold!'''
        
class NoTile(MapTile):#notile means no go
    def intro_text(self):
        print('There is a wall there. Choose a different direction.')

class DeathTile(MapTile):#instant death if you go off the map
    def __init__(self, x, y):
        self.baddie = baddies.ROUS()
        self.alive_text = '\nYou are instantly eaten by an R.O.U.S.'
        
    def intro_text(self):
        text = self.alive_text if self.baddie.is_alive() else self.dead_text#this determines which intro text to return
        return text

    def modify_player(self, player):#baddie can damage you
        if self.baddie.is_alive():
            player.hp = player.hp - self.baddie.damage
            print('\n{} does {} damage. You have {} HP remaining!'
                  .format(self.baddie.name,self.baddie.damage, player.hp))#displays damage done, HP left
        
       
#building the actual world tiles like a grid            
world_map = [
    [NoTile(0,0), NoTile(1,0), NoTile(2,0), DeathTile(3,0), SpaceSuitTile(4,0), DeathTile(5,0), NoTile(6,0), NoTile(7,0), NoTile(8,0)],
    [NoTile(0,1), NoTile(1,1), NoTile(2,1), DeathTile(3,1), BaddieTile(4,1), DeathTile(5,1), NoTile(6,1), NoTile(7,1), NoTile(8,1)],
    [NoTile(0,2), NoTile(1,2), NoTile(2,2), DeathTile(3,2), DoorTileN(4,2), DeathTile(5,2), NoTile(6,2), NoTile(7,2), NoTile(8,2)],
    [NoTile(0,3), NoTile(1,3), DeathTile(2,3), BaddieTile(3,3), FlashlightTile(4,3), BaddieTile(5,3), DeathTile(6,3), NoTile(7,3), NoTile(8,3)],
    [FindGoldTile(0,4), BaddieTile(1,4), DoorTileW(2,4), FindGoldTile(3,4), StartTile(4,4),
     FindGoldTile(5,4), DoorTileE(6,4), UseSpacesuitTile(7,4), VictoryTile(8,4)],
    [DeathTile(0,5), DeathTile(1,5), DeathTile(2,5), BaddieTile(3,5), FindGoldTile(4,5), BaddieTile(5,5), DeathTile(6,5), NoTile(7,5), NoTile(8,5)],
    [NoTile(0,6), NoTile(1,6), DeathTile(2,6), DeathTile(3,6), DoorTileS(4,6), DeathTile(5,6), DeathTile(6,6), NoTile(7,6), NoTile(8,6)],
    [NoTile(0,7), NoTile(1,7), DeathTile(2,7), DeathTile(3,7), BaddieTile(4,7), DeathTile(5,7), NoTile(6,7), NoTile(7,7), NoTile(8,7)],
    [NoTile(0,8), NoTile(1,8), DeathTile(2,8), DeathTile(3,8), FindGoldTile(4,8), DeathTile(5,8), NoTile(6,8), NoTile(7,8), NoTile(8,8)]
    ]


def tile_at(x, y):#if outside parameters, return None, keeps player on map
    if (x < 0 or x > 8) or (y < 0 or y > 8):
       return None
    
    try:
        return world_map[y][x]
    except IndexError:
        return None      
