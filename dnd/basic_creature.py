
from dnd.basic_creature_info_definitions import creature_list
from dnd.creature_xp import determineXPperHP
from dnd.util import findNameInList
from dnd.roll import roll


from random import randint

def __main__():
    creature_names = [x.name for x in creature_list]

    while True:
        name = input('Enter creature: ')
        match = findNameInList(name, creature_names)
        
        if match:
            if type(match) is str:
                creature_info = creature_list[creature_names.index(match)]
                creature = BasicCreature(creature_info)
                print(creature)
                
            else:
                print('Found {} matches:'.format(len(match)))
                print(match)
        else:
            print('Creature not found')

def creatureInfoFromName(name):
    creature_names = [x.name for x in creature_list]
    match = findNameInList(name, creature_names)
    
    if type(match) is str:
        creature_info = creature_list[creature_names.index(match)]
        return creature_info
        
    elif type(match) is list:
        print('Found {} matches:'.format(len(match)))
        print(match)
        return
        
    else:
        print('Creature not found')
        return
        
def creatureFromName(name):
    creature_names = [x.name for x in creature_list]
    match = findNameInList(name, creature_names)
    
    if type(match) is str:
        creature_info = creature_list[creature_names.index(match)]
        creature = BasicCreature(creature_info)
        return creature
        
    elif type(match) is list:
        print('Found {} matches:'.format(len(match)))
        print(match)
        return
        
    else:
        print('Creature not found')
        return
            
class BasicCreature():
    def __init__(self, creature_info):
        self.name = creature_info.name
        self.hit_dice = randint(creature_info.hit_dice[0],
                                creature_info.hit_dice[1])
        
        hp_mod = randint(
            creature_info.hit_point_mod[0],
            creature_info.hit_point_mod[1])
            
        xp_per_hp = determineXPperHP(self.hit_dice, hp_mod)
        
        self.hit_points = roll(8,self.hit_dice) + hp_mod
        self.hit_points = max(self.hit_points, 1)

        self.xp = (
            creature_info.base_xp +
            self.hit_points * xp_per_hp)
            
    def __str__(self):
        return '{}, {} HP, {} XP'.format(
            self.name,
            self.hit_points,
            self.xp)
        
def calcXP(hd, hp_mod, base_xp=0, lvl=None):
        self.name = name
        self.hit_dice = hd
        self.hit_point_mod = hp
        self.base_xp = base_xp
        self.level = lvl

        
if __name__ == '__main__':
    __main__()
        