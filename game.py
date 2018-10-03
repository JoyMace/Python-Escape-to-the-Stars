from player import Player #imports player and all the Player attributes
import world #imports world and all the world attibutes
from collections import OrderedDict #create ordered dictionary to store legal actions

def play():#main bulk of game is here
    print('''                           Escape to the Stars!\n
          The domed ceiling is made of glass.
You can see the Stars up above, calling your name.
There are four doors to the North, South, East and West.
There's all kinds of creepy things lurking around.
You've got to get the heck out of here!
But first, find as much gold as you can!''')
    player = Player()#calls Player and attributes
    while player.is_alive() and not player.victory:#because if player.is_dead, game is over
        room = world.tile_at(player.x, player.y)# game is played where player "is" on map
        print(room.intro_text())#prints intro text of room right away on tile
        room.modify_player(player) # if player is damaged/healed this line calls the method
        if player.is_alive() and not player.victory:#player.victory ends game
            choose_action(room, player)#if player can play, let them choose what to do
        elif not player.is_alive():#player dead = game over
            print('You have failed to escape! The End.')
            
def get_available_actions(room, player):#this way a player always knows what is possible
    #on a tile
    actions = OrderedDict()#always displays the actions in order
    print('\nChoose an action: ')#prompt for choice
    
    if player.inventory:#if player has no inventory, action not available
            action_adder(actions, 'i', player.print_inventory, 'Print inventory')
    if isinstance(room, world.BaddieTile) and room.baddie.is_alive():#can only attack if baddie
            action_adder(actions, 'a', player.attack, 'Attack')
    if isinstance(room, world.NoTile):#can't go that way on a no tile
        print('You cannot go that way')
    
    else:#any other time you can do these things
        if world.tile_at(room.x, room.y):#you can always look around
            action_adder(actions, 'l', room.intro_text, "Look around")
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
        if player.hp < 100:
            action_adder(actions, 'h', player.heal, 'Heal')
        
            
    return actions#display actions that are available


def action_adder(action_dict, hotkey, action, name):#allows upper or lower hotkey
          action_dict[hotkey.lower()] = action
          action_dict[hotkey.upper()] = action
          print('{}: {}'.format(hotkey, name))

def choose_action(room, player):#which action can be chosen?
          action = None
          while not action:#will wait for input
              available_actions = get_available_actions(room, player)
              action_input = input('What do you want to do?: ')
              action = available_actions.get(action_input)
              if action:
                  action()#action references the function, action() runs the function
              else:#if player enters invalid key
                  print('\nYou cannot do that!')


play()#calls play function to start up game

