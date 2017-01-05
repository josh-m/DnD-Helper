""" Contains minimal information on creatures to determine their
    starting HP and their XP values
"""

class BasicCreatureInfo():
    def __init__(self, name, hd, hp, num = (1,1), lair=0.0,
                 base_xp = 0, lvl=None):
        
        self.name = name
        self.hit_dice = hd
        self.hit_point_mod = hp
        self.num_appearing = num
        self.lair_chance = lair
        self.base_xp = base_xp
        self.level = lvl

