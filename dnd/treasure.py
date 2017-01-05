from dnd.currency import Wealth
from dnd.roll import roll
from dnd.gem import Gem
from dnd.jewelry import Jewelry

from random import random, randint



def __main__():
    while True:
        inp = input('Enter gem count:')
        g_num = int(inp)
        inp = input('Enter jewelry count:')
        j_num = int(inp)
        
        t = Treasure(gems=g_num,jewelry=j_num)
        print(t)

class Treasure():
    def __init__(self, wealth=None,maps=[],items=[],gems=0,jewelry=0):
        if wealth: self.wealth=wealth
        else: self.wealth = Wealth(0,0,0,0,0)
        self.maps=maps
        self.items=items
        self.gem_count=gems
        self.jewelry_count=jewelry
        self.gem_list = []
        self.jewelry_list = []
        
    def clear(self):
        self.wealth = Wealth(0,0,0,0,0)
        self.maps = []
        self.items = []
        self.gem_count = 0
        self.jewelry_count = 0
        self.gem_list = []
        self.jewelry_list = []
    
    def addGems(self, count):
        self.gem_count += count
        self.convertGemsJewelry()
        
    def addJewelry(self, count):
        self.jewelry_count += count
        self.convertGemsJewelry()
    
    def addItem(self,item):
        self.items.extend(item)
        
    def addTreasure(self, t):
        if t.wealth: self.wealth.addWealth(t.wealth)
        self.maps.extend(t.maps)
        self.items.extend(t.items)
        self.gem_count += t.gem_count
        self.jewelry_count += t.jewelry_count
        
        self.convertGemsJewelry()

    def __bool__(self):
        if (self.wealth or self.items or self.gem_list
                or self.jewelry_list or self.maps):
            return True
        else:
            return False
        
    def __str__(self):
        output = ''
        
        if self.wealth:
            output = 'COINS:\n------\n{}\n'.format(self.wealth)

        self.convertGemsJewelry()
        
        
        
        if len(self.gem_list):
            val = gemsValue(self.gem_list)
            string = '\n{} GEMS WORTH TOTAL OF {}\n'.format(len(self.gem_list),val)
            string += '-'*(len(string)-3)
            output += string 
            
            for gem in self.gem_list:
                output += '\n'+str(gem)
        
        if len(self.jewelry_list):
            val = jewelryValue(self.jewelry_list)
            string = '\n\n{} PIECES OF JEWELRY WORTH TOTAL OF {}\n'.format(len(self.jewelry_list),val)
            string += '-'*(len(string)-4)
            output += string
            for jewelry in self.jewelry_list:
                output += '\n'+str(jewelry)
        
        if len(self.items):
            output += '\n\nITEMS:\n------'
            for item in self.items:
                output += '\n'+str(item)
        
        if len(self.maps):
            output += '\n\nMAPS:\n-----'
            for map in self.maps:
                output += '\n'+str(map)

        return output        
    
    def convertGemsJewelry(self):
        if self.jewelry_count:
            for i in range(self.jewelry_count):
                self.jewelry_list.append(Jewelry())
            self.jewelry_list = sorted(self.jewelry_list, reverse=True)
            self.jewelry_count = 0
        
        if self.gem_count:
            for i in range(self.gem_count):
                g = Gem()
              
                self.gem_list.append(g)
            self.gem_list = sorted(self.gem_list, reverse=True)
            self.gem_count = 0
        

    def rollLoot(self, t_type, num_enemies=1):
        self.clear()
        self.wealth, self.maps, self.items, self.gem_count, self.jewelry_count = generateLoot(t_type)

def gemsValue(gem_list):
    value = Wealth(0,0,0,0,0)
    for gem in gem_list:
        value.addCoins(gem.value)
    return value

def jewelryValue(jewelry_list):
    value = Wealth(0,0,0,0,0)
    for jewelry in jewelry_list:
        value.addCoins(jewelry.base_value)
    return value
        
if __name__ == '__main__':
    __main__()



    
