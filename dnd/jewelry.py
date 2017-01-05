from dnd.roll import roll
from dnd.util import roundDownToNearest
from dnd.currency import Coin

from random import randint,choice

base_values = ((100,1000),(200,1200),(300,1800),(500,3000),
    (1000,6000),(2000,8000),(2000,12000))
max_val_idx = 6

jewelry_types = ('bracelet','brooch','crown','earrings','necklace',
    'pendant','ring','tiara','medallion','chalice')

class Jewelry():
    def __init__(self):
        self.base_value, self.name = generateJewelry()
        self.base_value = Coin(self.base_value, 'g')
        
    def __str__(self):
        return '{} - {}'.format(self.base_value, self.name)
    
    def __lt__(self,other):
        return self.base_value < other.base_value
        
def generateJewelry():
    value = 0 #always in g.p.
    name = None

    #initial workmanship
    r = roll(100)
    if r < 11:
        val_idx = 0
    elif r < 21:
        val_idx = 1
    elif r < 41:
        val_idx = 2
    elif r < 51:
        val_idx = 3
    elif r < 71:
        val_idx = 4
    elif r < 91:
        val_idx = 5
    else:
        val_idx = 6
            
    #possible higher range
    to_roll = True
    while to_roll:
        to_roll = False
        if isExceptional():
            to_roll = True
            val_idx = min(val_idx+1, max_val_idx)
            
    #determine value within jewlery class
    value = randint(base_values[val_idx][0], base_values[val_idx][1])
    value = roundDownToNearest(value,100)
    
    #determine type
    materials = determineMaterials(val_idx)
    
    #if it has gems, are they exceptional?
    if val_idx > 4:
        r = roll(8)
        if r == 1:
            value += 5000

            to_roll = True
            exceptional = False
            while to_roll:
                to_roll = False
                r = roll(6)
                if r == 1:
                    value = min(640000,value*2)
                    to_roll = True
                    exceptional = True
            if exceptional:
                materials = 'exceptionally ' + materials
                
            materials = 'masterwork ' + materials
            
    return [value, '{} {}'.format(materials, choice(jewelry_types))]
       
def determineMaterials(value_idx):
    materials = None
    if value_idx == 0:
        materials = choice(['ivory','silver'])
    elif value_idx == 1:
        materials = 'silver and gold'
    elif value_idx == 2:
        materials = 'gold'
    elif value_idx == 3:
        materials = choice(['jade','coral','platinum'])
    elif value_idx == 4:
        materials = 'bejeweled silver'
    elif value_idx == 5:
        materials = 'bejeweled gold'
    elif value_idx == 6:
        materials = 'bejeweled platinum'
        
    return materials
        
def isExceptional():
    r = roll(10)
    return  r == 1