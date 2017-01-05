from dnd.treasure import Treasure
from dnd.treasure_map import Map
from dnd.magic_item import (generateMagicItem, generatePotion,
    generateScroll,generateRing, generateRod, generateArmorShield,
    generateMiscMagic,generateRodStaffWand)
from dnd.magic_weapon import generateSword, generateMiscWeapon
from dnd.currency import Wealth
from dnd.roll import roll

from random import randint,random

#The treasure tables apply to treasure found in outdoor lairs
#Dungeon treasure are meant to be handpicked by the DM
def generateLoot(t_type, num_enemies=1):
    t_type = t_type.upper()
    cp=0; sp=0; ep=0; gp=0; pp=0
    maps = []
    items = []
    gems = 0
    jewelry = 0
    
    if t_type == 'A':
        if random() < 0.25: cp = 1000 * roll(6)
        if random() < 0.3: sp = 1000 * roll(6)
        if random() < 0.35: ep = 1000 * roll(6)
        if random() < 0.4: gp = 1000 * roll(10)
        if random() < 0.25: pp = 100 * roll(4)
        
        if random() < 0.6: gems = roll(4,10)
        if random() < 0.5: jewelry = roll(3,10)

        if random() < 0.3:
            for i in range(3):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())         
    elif t_type == 'B':
        if random() < 0.5: cp = 1000 * roll(8)
        if random() < 0.25: sp = 1000 * roll(6)
        if random() < 0.25: ep = 1000 * roll(4)
        if random() < 0.25: gp = 1000 * roll(3)   
        
        if random() < 0.3: gems = roll(8)
        if random() < 0.2: jewelry = roll(4)
  
        if random() < 0.1:
            r = roll(3)
            if r == 1: items.append(generateSword())
            elif r == 2: items.append(generateArmorShield())
            else: items.append(generateMiscWeapon())          
    elif t_type == 'C':
        if random() < 0.2: cp = 1000 * roll(12)
        if random() < 0.3: sp = 1000 * roll(6)
        if random() < 0.1: ep = 1000 * roll(4)
        
        if random() < 0.25: gems = roll(6)
        if random() < 0.2: jewelry = roll(3)
        
        if random() < 0.1:
            for i in range(2):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())          
    elif t_type == 'D':
        if random() < 0.1: cp = 1000 * roll(8)
        if random() < 0.15: sp = 1000 * roll(12)
        if random() < 0.15: ep = 1000 * roll(8)
        if random() < 0.5: gp = 1000 * roll(6)
    
        if random() < 0.3: gems = roll(10)
        if random() < 0.25: jewelry = roll(6)
    
        if random() < 0.15:
            items.append(generatePotion())
            for i in range(2):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'E':
        if random() < 0.5: cp = 1000 * roll(10)
        if random() < 0.25: sp = 1000 * roll(12)
        if random() < 0.25: ep = 1000 * roll(6)
        if random() < 0.25: gp = 1000 * roll(8)
        
        if random() < 0.15: gems = roll(12)
        if random() < 0.1: jewelry = roll(8)
        
        if random() < 0.25:
            items.append(generateScroll())
            for i in range(3):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'F':
        if random() < 0.10: sp = 1000 * roll(20)
        if random() < 0.15: ep = 1000 * roll(12)
        if random() < 0.40: gp = 1000 * roll(10)
        if random() < 0.35: pp = 100 * roll(8)
        
        if random() < 0.2: gems = roll(10,3)
        if random() < 0.1: jewelry = roll(10)
        
        if random() < 0.3:
            items.append(generatePotion())
            items.append(generateScroll())
            for i in range(3):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem(restrict_weapons=True))
    elif t_type == 'G':
        if random() < 0.5: gp = 1000 * roll(4,10)
        if random() < 0.5: pp = 100 * roll(20)
        
        if random() < 0.3: gems = roll(4,5)
        if random() < 0.25: jewelry = roll(10)

        if random() < 0.35:
            items.append(generateScroll())
            for i in range(4):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'H':
        if random() < 0.25: cp = 1000 * roll(6,5)
        if random() < 0.4: sp = 1000 * roll(100)
        if random() < 0.4: ep = 1000 * roll(10,4)
        if random() < 0.55: gp = 1000 * roll(10,6)
        if random() < 0.25: pp = 100 * roll(10,5)
        
        if random() < 0.5: gems = roll(100)
        if random() < 0.5: jewelry = roll(4,10)
        
        if random() < 0.15:
            items.append(generatePotion())
            items.append(generateScroll())
            for i in range(4):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'I':
        if random() < 0.3: pp = 100 * roll(6,3)
        
        if random() < 0.55: gems = roll(10,2)
        if random() < 0.5: jewelry = roll(12)
        
        if random() < 0.15:
            if roll(100) < 11: maps.append(Map())
            else: items.append(generateMagicItem())
    elif t_type == 'J':
        for i in range(num_enemies):
            cp += roll(8,3)
    elif t_type == 'K':
        for i in range(num_enemies):
            sp += roll(6,3)
    elif t_type == 'L':
        for i in range(num_enemies):
            ep += roll(6,2)
    elif t_type == 'M':
        for i in range(num_enemies):
            gp += roll(4,2)
    elif t_type == 'N':
        for i in range(num_enemies):
            pp += roll(6)
    elif t_type == 'O':
        if random() < 0.25: cp = 1000 * roll(4)
        if random() < 0.2: sp = 1000 * roll(3)
    elif t_type == 'P':
        if random() < 0.3: sp = 1000 * roll(6)
        if random() < 0.25: ep = 1000 * roll(2)
    elif t_type == 'Q':
        if random() < 0.5: gems = roll(4)
    elif t_type == 'R':
        if random() < 0.4: gp = 1000 * roll(4,2)
        if random() < 0.5: pp = 100 * roll(10,6)
        
        if random() < 0.55: gems = roll(8,4)
        if random() < 0.45: jewelry = roll(12)
    elif t_type == 'S':
        if random() < 0.4:
            for i in range(roll(4,2)):
                items.append(generatePotion())
    elif t_type == 'T':
        if random() < 0.5:
            for i in range(roll(4)):
                items.append(generateScroll())
    elif t_type == 'U':
        if random() < 0.9: gems = roll(8,10)
        if random() < 0.8: jewelry = roll(6,5)
        
        if random() < 0.7:
            items.append(generateRing())
            items.append(generateRodStaffWand())
            items.append(generateMiscMagic())
            items.append(generateArmorShield())
            items.append(generateSword())
            items.append(generateMiscWeapon())
    elif t_type == 'V':
        if random() < 0.85:
            for i in range(2):
                items.append(generateRing())
                items.append(generateRodStaffWand())
                items.append(generateMiscMagic())
                items.append(generateArmorShield())
                items.append(generateSword())
                items.append(generateMiscWeapon())
    elif t_type == 'W':
        if random() < 0.6: gp = 1000 * roll(6,5)
        if random() < 0.15: pp = 100 * roll(8)
        
        if random() < 0.6: gems = roll(8,10)
        if random() < 0.5: jewelry = roll(8,5)
        
        if random() < 0.55:
            maps.append(Map())
    elif t_type == 'X':
        if random() < 0.6:
            items.append(generatePotion())
            items.append(generateMiscMagic())
    elif t_type == 'Y':
        if random() < 0.7: gp = 1000 * roll(6,2)
    elif t_type == 'Z':
        if random() < 0.2: cp = 1000 * roll(3)
        if random() < 0.25: sp = 1000 * roll(4)
        if random() < 0.25: ep = 1000 * roll(4)
        if random() < 0.3: gp = 1000 * roll(4)
        if random() < 0.3: pp = 100 * roll(6)
        
        if random() < 0.55: gems = roll(6,10)
        if random() < 0.5: jewelry = roll(6,5)
        
        if random() < 0.5:
            for i in range(3):
                items.append(generateMagicItem())
    
    wealth =  Wealth(cp,sp,ep,gp,pp)
    
    return Treasure(wealth,maps,items,gems,jewelry)
