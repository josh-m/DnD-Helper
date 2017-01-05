from dnd.currency import Wealth
from dnd.roll import roll
from dnd.treasure import Treasure
from dnd.magic_item import (generateMagicItem, generatePotion, generateScroll,
    generateRing, generateRod, generateArmorShield,
    generateMiscMagic, generateMagicWeapon)
from dnd.magic_weapon import generateSword, generateMiscWeapon

from random import random, randint

class Map():
    def __init__(self, known_rwd=None, known_rwd2=None):
        self.wealth = Wealth()
        self.description = generateMap()
        [self.m_type,self.wealth,self.maps,
            self.items,self.gems,self.jewelry] = generateTreasure()
        
        if not known_rwd:
            [self.m_type,self.wealth,self.maps,
            self.items,self.gems,self.jewelry] = generateTreasure()
        else:
            [self.m_type,self.wealth,self.maps,
            self.items,self.gems,self.jewelry] = generateTreasure(known_rwd[0],known_rwd[1],known_rwd[2])
            
        if known_rwd2:
            t,w,m,i,g,j =  generateTreasure(known_rwd2[0],known_rwd2[1],known_rwd2[2])
            if w:
                self.wealth += w
            self.items.extend(i)
            self.gems += g
            self.jewelry += j
        
    def __str__(self):
        output = '{}, {}'.format(self.description,self.m_type)

        output += ('\n  {}\n  {} gems, {} jewelry'.format(self.wealth,
            self.gems,self.jewelry))
            
        for item in self.items:
            output += '\n  '+str(item)
        
        for map in self.maps:
            output += '\n  '+str(map)

        return output  
        
        return self.description

def generateTreasure(m_type=None,low=1,high=20):
    wealth = Wealth()
    maps = []
    items = []
    gems = 0
    jewelry = 0

    #determine treasure type
    if not m_type:
        r = roll(100)
        if r < 6:
            m_type = 'False Map'
        elif r < 71:
            m_type = 'Monetary'
        elif r < 91:
            m_type = 'Magic' 
        else:
            m_type = 'Combined Hoard'
       
    if m_type == 'Monetary':
        wealth,gems,jewelry = monetaryTreasure(low,high)
    elif m_type == 'Magic':
        items = magicTreasure(low,high)
    elif m_type == 'Combined Hoard':
        wealth,maps,items,gems,jewelry = combinedHoard()
        
    return [m_type,wealth,maps,items,gems,jewelry]
    
  
#maps should never list treasure to the player
def generateMap(m_type=None):
        
    #determine treasure location
    r = roll(100)
    if r < 21:
        loc = 'labyrinth of caves found in the lair'
    elif r < 61:
        loc = 'outdoors, ' + str(randint(5,8)) + ' miles distant'
    elif r < 91:
        loc = 'outdoors, ' + str(randint(10,40)) + ' miles distant'
    else:
        loc = 'outdoors, ' + str(randint(50,500)) + ' miles distant'

    if r > 20:
        r = roll(100)
        if r < 11:
            loc = 'Buried and unguarded ' + loc
        elif r < 21:
            loc = 'Hidden in water ' + loc
        elif r < 71:
            loc = 'Guarded in a lair ' + loc
        elif r < 81:
            loc = 'Somewhere in a ruins ' + loc
        elif r < 91:
            loc = 'In a burial crypt ' + loc
        else:
            loc = 'Secreted in a town ' + loc
            
    output = 'Map: {}'.format(loc)
    return output
    
def monetaryTreasure(low=1,high=20):
    wealth = None
    gems = 0
    jewelry = 0

    min_roll = low
    max_roll = high
    rolls_left = 1
    while (rolls_left > 0):
        r = randint(min_roll,max_roll)
        rolls_left -= 1
        
        if r < 3:
            wealth = Wealth(cp=(roll(4,2)*10000),sp=(roll(4,1,1)*10000))
        elif r < 6:
            wealth = Wealth(ep=(roll(6,5)*1000))
        elif r < 11:
            wealth = Wealth(gp=(roll(6,3)*1000))
        elif r < 13:
            wealth = Wealth(pp=(roll(4,5)*100))
        elif r < 16:
            gems = (roll(10)*10)
        elif r < 18:
            jewelry = (roll(10,5))
        elif r == 18:
            rolls_left = 2
            min_roll = 1
            max_roll = 17
        elif r == 19:
            rolls_left = 3
            min_roll = 1
            max_roll = 17
        else:
            wealth = Wealth(cp=(roll(4,2)*10000),sp=(roll(4,1,1)*10000),
                ep=(roll(6,5)*1000),gp=(roll(6,3)*1000),pp=(roll(4,5)*100))
            gems = (roll(10)*10)
            jewelry = (roll(10,5))
            
    return [wealth,gems,jewelry]

def magicTreasure(min_roll=1, max_roll=20):
    items = []
    

    r = randint(min_roll, max_roll)
    if r < 6:
        items.append(generateMagicItem())
        for i in range(4):
            items.append(generatePotion())
    elif r < 9:
        for i in range(2):
            items.append(generateMagicItem())
    elif r < 13:
        items.append(generateSword())
        items.append(generateArmorShield())
        items.append(generateMiscWeapon())
    elif r < 15:
        for i in range(3):
            items.append(generateMagicItem(restrict_sword=True,
                                          restrict_potion=True))
    elif r < 19:
        for i in range(6):
            items.append(generatePotion())
        for i in range(6):
            items.append(generateScroll())
    elif r == 19:
        items.append(generateRing())
        items.append(generateRod())
        for i in range(2):
            items.append(generateMagicItem())
    else:
        items.append(generateRod())
        items.append(generateMiscMagic())
        for i in range(3):
            items.append(generateMagicItem())
            
    return items
            
def combinedHoard():  
    w = Wealth()
    maps = []
    items = []
    g=0; j=0
    
    t = [None,None,None]
    
    
    r = roll(100)
    if r < 21:
        w,g,j = monetaryTreasure(1,2)
        items = magicTreasure(1,5)
    elif r < 41:
        w,g,j = monetaryTreasure(6,10)
        items = magicTreasure(1,5)
    elif r < 56:
        w,g,j = monetaryTreasure(3,5)
        t = monetaryTreasure(6,10)
        w += t[0]
        g += t[1]
        j += t[2]
        
        items = magicTreasure(1,5)
        items.extend(magicTreasure(15,18))
    elif r < 66:
        w,g,j = monetaryTreasure(1,2)
        t = monetaryTreasure(3,5)
        w += t[0]
        g += t[1]
        j += t[2]
        t = monetaryTreasure(6,10)
        w += t[0]
        g += t[1]
        j += t[2]

        items = magicTreasure(9,12)
        items.extend(magicTreasure(13,14))
    elif r < 76:
        w,g,j = monetaryTreasure(6,10)
        t = monetaryTreasure(11,12)
        w += t[0]
        g += t[1]
        j += t[2]        
        items = magicTreasure(6,8)
        items.extend(magicTreasure(15,18))
    elif r < 86:
        w,g,j = monetaryTreasure(20,20)
        
        maps.append(Map(('Magic',1,5)))
    elif r < 91:
        w,g,j = monetaryTreasure(20,20)

        maps.append(Map(('Magic',19,19)))
    elif r < 97:
        items = magicTreasure(20,20)
        maps.append(Map(('Monetary,1,2'),('Monetary',3,5)))
    else:
        items = magicTreasure(20,20)
        maps.append(Map(('Monetary',11,12),('Monetary',13,15)))
        maps.append(Map(('Magic',15,18)))
        
    return [w,maps,items,g,j]
    