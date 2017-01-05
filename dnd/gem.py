from dnd.roll import roll
from dnd.currency import Coin
from dnd.util import roundDownToNearest

from random import randint, choice
from copy import copy

BASE_VALUES = (Coin(1,'s'),Coin(5,'s'),Coin(10,'s'),Coin(1,'g'),
    Coin(5,'g'),Coin(10,'g'),Coin(50,'g'),Coin(100,'g'),Coin(500,'g'),
    Coin(1000,'g'),Coin(5000,'g'),Coin(10000,'g'),Coin(25000,'g'),
    Coin(50000,'g'),Coin(100000,'g'),Coin(250000,'g'),
    Coin(500000,'g'),Coin(1000000,'g'))
BV_MAX_IDX = 17 #length-12

class Gem():
    def __init__(self):
        base_idx = generateBaseValueIdx()
        base_idx, value_mod = modifyBaseValue(base_idx)

        self.value = copy(BASE_VALUES[base_idx])
        
        #determine type of gem
        self.name, self.group = gemType(self.value)
        
        #modified value
        self.value.quantity = roundDownToNearest(self.value.quantity * value_mod, 1)
        
    def __str__(self):
        return '{} {} ({})'.format(self.value,self.name,self.group)
        
    def __lt__(self,other):
        return self.value < other.value
    
def gemType(base_value):
    name = None
    group = None
    
    if (base_value.coin == 's' or
        base_value.quantity < 50):
        group = 'Ornamental Stone'
        name = choice(['Azurite','Banded Agate','Blue Quartz','Eye Agate',
            'Hematite','Lapis Lazuli','Malachite','Moss Agate','Obsidian',
            'Rhodochrosite','Tiger Eye','Turquoise'])
    elif base_value.quantity < 100:
        group = 'Semi-precious Stone'
        name = choice(['Bloodstone','Carnelian','Chalcedony','Chrysoprase',
            'Citrine','Jasper','Moonstone','Onyx','Rock Crystal','Sardonyx',
            'Smoky Quartz','Star Rose Quartz','Zircon'])
    elif base_value.quantity < 500:
        group = 'Fancy Stone'
        name = choice(['Amber','Alexandrite','Amethyst','Chrysoberyl',
            'Coral','Garnet','Jade','Jet','Pearl','Spinel','Tourmaline'])
    elif base_value.quantity < 1000:
        group = 'Fancy Stone'
        name = choice(['Aquamarine','Violet Garnet','Black Pearl',
            'Peridot','Deep Blue Spinel','Topaz'])
    elif base_value.quantity < 5000:
        group = 'Gem Stone'
        name = choice(['Black Opal','Emerald','Fire Opal','Opal',
            'Oriental Amethyst','Oriental Topaz','Sapphire',
            'Star Ruby','Star Sapphire'])
    else:
        group = 'Gem Stone'
        name = choice(['Black Sapphire','Diamond','Jacinth',
            'Oriental Emerald','Ruby'])
            
    return [name,group]
    
def generateBaseValueIdx():
    r = roll(100)
    if r < 26:
        val_idx = 5
    elif r < 51:
        val_idx = 6
    elif r < 71:
        val_idx = 7
    elif r < 91:
        val_idx = 8
    elif r < 100:
        val_idx = 9
    else:
        val_idx = 10
        
    return int(val_idx)
    
def modifyBaseValue(bv):
    value_mod = 1.0
    value_idx = bv
    max_idx = min(value_idx+7, BV_MAX_IDX)
    min_idx = max(value_idx-5, 0)
    
    
    min_roll = 1
    max_roll = 10
    rolls_left = 1
    while rolls_left > 0:
        rolls_left -= 1
        r = randint(min_roll, max_roll)
        if r == 1:
            value_idx = min(value_idx+1, max_idx)
            rolls_left += 1
            max_roll = 8
        elif r == 2:
            value_mod = 2.0
        elif r == 3:
            value_mod = 1.0 + (roll(6)*0.1)
        elif r == 9:
            value_mod = 1.0 - (roll(4)*0.1)
        elif r == 10:
            value_idx = max(0,value_idx -1)
            rolls_left += 1
            min_roll = 2
    
    return int(value_idx), float(value_mod)
        
        
        
        
        
        
        
        
        
        
        
        
        