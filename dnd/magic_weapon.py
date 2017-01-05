from dnd.roll import roll
from dnd.int_sword import IntelligentSword

from random import choice

class MagicWeapon():
    #bonus is the bonus to ego rating
    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
        
    def __str__(self):
        return self.name

def generateSword():
    sword = None

    if roll(100) < 96:
        r = roll(100)
        if r < 26: sword = MagicWeapon('Sword +1',1)
        elif r < 31: sword = MagicWeapon('Sword +1, +2 vs magic-using & enchanted creatures',3)
        elif r < 36: sword = MagicWeapon('Sword +1, +3 vs lycanthropes & shape-changers',4)
        elif r < 41: sword = MagicWeapon('Sword +1, +3 vs regenerating creatures',4)
        elif r < 46: sword = MagicWeapon('Sword +1, +4 vs reptiles',5)
        elif r < 50: sword = MagicWeapon(('Sword +1, Flame Tongue:\n+2 vs regenerating' +
            ' creatures\n+3 vs cold-using, inflammable, or avian ' +
            'creatures\n+4 vs undead'),5)
        elif r == 50: sword = MagicWeapon('Sword +1, Luck Blade',2)
        elif r < 59: sword = MagicWeapon('Sword +2',2)
        elif r < 63: sword = MagicWeapon('Sword +2, Giant Slayer +3',5)
        elif r < 67: sword = MagicWeapon('Sword +2, Dragon Slayer +4',6)
        elif r < 71: sword = MagicWeapon('Short Sword, Quickness +2',4)
        elif r < 77: sword = MagicWeapon('Sword +3',3)
        elif r < 80: sword = MagicWeapon(('Sword +3, Frost Brand:\n'+
            '+6 vs fire using/dwelling creatures'),9)
        elif r < 82: sword = MagicWeapon('Sword of the Planes',2)
        elif r < 85: sword = MagicWeapon('Sword +4',4)
        elif r < 87: sword = MagicWeapon('Sword +4, Defender',8)
        elif r < 89: sword = MagicWeapon('Sword +5',5)
        elif r < 95: sword = MagicWeapon('Sword +1, Cursed',1)
        elif r < 99: sword = MagicWeapon('Sword -2, Cursed',-2)
        else: sword = MagicWeapon('Sword, Cursed Berserking',4)
    else:
        r = roll(100)
        if r < 16: sword = MagicWeapon('Sun Blade',4)
        elif r == 16: sword = MagicWeapon('Sword, Anything',2)
        elif r < 33: sword = MagicWeapon('Broad Sword, Final Word',0)
        elif r < 46: sword = MagicWeapon('Sword of Dancing',5)
        elif r < 62: sword = MagicWeapon('Sword +5, Defender',10)
        elif r < 70: sword = MagicWeapon('Sword +6, Defender',12)
        elif r < 85: sword = MagicWeapon('Sword +5, Holy Avenger',10)
        elif r < 92: sword = MagicWeapon('Sword +6, Holy Avenger',12)
        elif r < 94: sword = MagicWeapon('Sword of Life Stealing',4)
        elif r < 96: sword = MagicWeapon('Sword +2, Nine Lives Stealer',4)
        elif r < 98: sword = MagicWeapon('Sword of Sharpness',6)
        elif r == 98: sword = MagicWeapon('Sword, Vorpal Weapon',6)
        else: sword = MagicWeapon('Sword of Wounding',2)

    if (('Short' not in sword.name) and
        ('Sun' not in sword.name) and
        ('Broad' not in sword.name)):
        r = roll(100)
        if r == 1:
            sword.name = 'Two-Handed ' + sword.name
        elif r < 6:
            sword.name = 'Bastard ' + sword.name
        elif r < 11:
            sword.name = 'Short ' + sword.name
        elif r < 16:
            sword.name = 'Falchion ' + sword.name
        elif r < 36:
            sword.name = 'Broad ' + sword.name
        else:
            sword.name = 'Long ' + sword.name

    #Determine if intelligent
    r = roll(100)
    if r > 75:
        int_sword = IntelligentSword(sword,r)
        return int_sword
        
    return sword


def generateMiscWeapon():
    wpn = None

    if roll(100) < 51:
        r = roll(100)
        if r < 9: wpn = MagicWeapon('Arrow +1 ('+str(roll(12,2))+')',1)
        elif r < 13: wpn = MagicWeapon('Arrow +2 ('+str(roll(8,2))+')',2)
        elif r < 15: wpn = MagicWeapon('Arrow +3 ('+str(roll(6,2))+')',3)
        elif r == 15:
            creatures = ['Arachnid','Avian','Bard','Cleric','Demon','Devil',
                'Dragon','Druid','Elemental','Fighter','Giant','Golem','Illusionist',
                'Ki-Rin','Magic-User','Mammal','Monk','Paladin','Ranger','Reptile',
                'Sea Monster','Thief','Titan','Undead']
            wpn = MagicWeapon('Arrow of ' + choice(creatures) + ' Slaying +3',3)
        elif r < 21: wpn = MagicWeapon('Axe +1',1)
        elif r < 23: wpn = MagicWeapon('Axe +2',2)
        elif r == 23: wpn = MagicWeapon('Throwing Axe +2',2)
        elif r == 24: wpn = MagicWeapon('Axe +3',3)
        elif r < 28: wpn = MagicWeapon('Battle Axe +1',1)
        elif r < 33: wpn = MagicWeapon('Bolt +2 ('+str(roll(10,2))+')',2)
        elif r < 36: wpn = MagicWeapon('Bow +1',1)
        elif r == 36: wpn = MagicWeapon('Crossbow of Accuracy +3',3)
        elif r == 37: wpn = MagicWeapon('Crossbow of Distance',1)
        elif r == 38: wpn = MagicWeapon('Crossbow of Speed',1)
        elif r < 47: wpn = MagicWeapon('Dagger +1, +2 vs creatures smaller than man-sized',1)
        elif r < 51: wpn = MagicWeapon('Dagger +2, +3 vs creaturse larger than man-sized',2)
        elif r == 51: wpn = MagicWeapon('Dagger of Venom',1)
        elif r < 57: wpn = MagicWeapon('Flail +1',1)
        elif r < 61: wpn = MagicWeapon('Hammer +1',1)
        elif r < 63: wpn = MagicWeapon('Hammer +2',2)
        elif r < 64: wpn = MagicWeapon('Hammer +3, Dwarven Thrower',3)
        elif r < 65: wpn = MagicWeapon('Hammer of Thunderbolts',3)
        elif r < 68: wpn = MagicWeapon('Javelin +2',2)
        elif r < 73: wpn = MagicWeapon('Mace +1',1)
        elif r < 76: wpn = MagicWeapon('Mace +2',2)
        elif r == 76: wpn = MagicWeapon('Mace of Disruption',1)
        elif r == 77: wpn = MagicWeapon('Mace +4',4)
        elif r < 81: wpn = MagicWeapon('Military Pick +1',1)
        elif r < 83: wpn = MagicWeapon('Morning Star +1',1)
        elif r < 89: wpn = MagicWeapon('Scimitar +2',2)
        elif r == 89: wpn = MagicWeapon('Sling of Seeking +2',2)
        elif r < 95: wpn = MagicWeapon('Spear +1',1)
        elif r < 97: wpn = MagicWeapon('Spear +2',2)
        elif r == 97: wpn = MagicWeapon('Spear +3',3)
        elif r < 100: wpn = MagicWeapon('Spear, Cursed Backbiter',1)
        else: wpn = MagicWeapon('Trident (Military Fork) +3',3)
    else:
        r = roll(100)
        if r < 3: wpn = MagicWeapon('Arrow +4 ('+str(roll(4,2))+')',4)
        elif r == 3: wpn = MagicWeapon('Axe +4',4)
        elif r == 4:
            r = roll(20)
            if r < 6: bonus = 1
            elif r < 11: bonus = 2
            elif r < 16:  bonus = 3
            elif r < 20: bonus = 4
            else: bonus = 5
            wpn = MagicWeapon('Axe of Hurling +'+str(bonus),bonus)
        elif r < 11: wpn = MagicWeapon('Battle Axe +2',2)
        elif r < 14: wpn = MagicWeapon('Battle Axe +3',3)
        elif r < 21: wpn = MagicWeapon('Bolt +1, ('+str(roll(6,6))+')',1)
        elif r < 23: wpn = MagicWeapon('Bolt +3, ('+str(roll(4,3))+')',3)
        elif r < 28: wpn = MagicWeapon('Sling Bullet +1, ('+str(roll(4,5))+')',1)
        elif r < 32: wpn = MagicWeapon('Sling Bullet +2, ('+str(roll(4,3))+')',2)
        elif r < 35: wpn = MagicWeapon('Sling Bullet +3, ('+str(roll(4,2))+')',3)
        elif r == 35: wpn = MagicWeapon('Sling Bullet of Impact, ('+str(roll(4))+')',1)
        elif r < 41: wpn = MagicWeapon('Dagger +1',1)
        elif r < 44: wpn = MagicWeapon('Dagger +2',2)
        elif r == 44: wpn = MagicWeapon('Dagger +2, Longtooth',2)
        elif r < 47: wpn = MagicWeapon('Dagger +3',3)
        elif r == 47:
            r = roll(100)
            if r < 36: bonus = 1
            elif r < 66: bonus = 2
            elif r < 91: bonus = 3
            else: bonus = 4
            wpn = MagicWeapon('Dagger of Throwing +'+str(bonus),bonus)
        elif r < 52: wpn = MagicWeapon('Dart +1, ('+str(roll(4,3))+')',1)
        elif r < 55: wpn = MagicWeapon('Dart +2, ('+str(roll(4,2))+')',2)
        elif r < 57: wpn = MagicWeapon('Dart +3, ('+str(roll(4,1))+')',3)
        elif r == 57: wpn = MagicWeapon('Dart of Homing, ('+str(roll(2))+')',3)
        elif r < 11: wpn = MagicWeapon('Flail +2',2)
        elif r == 62: wpn = MagicWeapon('Hammer +4',4)
        elif r == 63:
            r = roll(100)
            if r < 21: bonus = 1; suffix = ', Knife'
            elif r < 36: bonus = 2; suffix = ', Knife'
            elif r < 51: bonus = 1; suffix = ', Dagger'
            elif r < 71: bonus = 2; suffix = ', Dagger'
            elif r < 91: bonus  = 2; suffix = ', Scimitar'
            else: bonus = 3; suffix = ', Scimitar'
            wpn = MagicWeapon('Hornblade'+suffix+' +'+str(bonus),bonus)
        elif r < 69: wpn = MagicWeapon('Javelin +1',1)
        elif r < 71: wpn = MagicWeapon('Javelin +3',3)
        elif r < 76: wpn = MagicWeapon('Knife +1',1)
        elif r < 79: wpn = MagicWeapon('Knife +2',2)
        elif r == 79:
            r = roll(10)
            if r < 5: bonus = 1
            elif r < 8: bonus = 2
            elif r < 10: bonus = 3
            else: bonus = 4
            wpn = MagicWeapon('Knife, Buckle +'+str(bonus),bonus)
        elif r < 82: wpn = MagicWeapon('Lance +1',1)
        elif r < 84: wpn = MagicWeapon('Mace +3',3)
        elif r < 87: wpn = MagicWeapon('Morning Star +2',2)
        elif r == 87: wpn = MagicWeapon('Pole Arm +1',1)
        elif r < 90:
            r = roll(20)
            if r < 6: bonus = 1
            elif r < 10: bonus = 2
            elif r < 14: bonus = 3
            elif r < 18: bonus = 4
            else: bonus = 5
            wpn = MagicWeapon('Magic Quarterstaff +'+str(bonus), bonus)
        elif r < 93: wpn = MagicWeapon('Scimitar +1',1)
        elif r < 95: wpn = MagicWeapon('Scimitar +3',3)
        elif r == 95:
            r = roll(4)
            if r < 4:
                bonus = 2
            else:
                r = roll(100)
                if r < 51: bonus = 1
                elif r < 76: bonus = 3
                elif r < 91: bonus = 4
                else: bonus = 5
            wpn = MagicWeapon('Scimitar of Speed +'+str(bonus),bonus)
        elif r == 96: wpn = MagicWeapon('Scimitar +4',4)
        elif r < 100: wpn = MagicWeapon('Spear +4',4)
        else: wpn = MagicWeapon('Spear +5',5)

    return wpn