
from dnd.roll import roll

from collections import OrderedDict
from string import ascii_uppercase


class PlayerChar():

    def __init__(self, pc=None):

        if not pc:
            #abilities is the base rolled
            abilities_base = assignAbilityScores(determineAbilityScores(auto=True), auto=True)
            abilities_sub = OrderedDict([('STR',1),('INT',1),('WIS',1),('DEX',1),('CON',1),('CHR',1)])
            print(abilities_base)
            race = chooseRace(abilities_base)
            #abilities with natural modifications (race and age)
            abilities = adjustAbilitiesForRace(race,abilities_base)
            print(race)
            print(abilities)
            class_role = chooseClass(race, abilities)
            print(class_role)

            if ((class_role in ['Fighter','Paladin','Ranger'])
            and abilities['STR'] == 18):
                abilities_sub['STR'] = roll(100)
                print(abilities_sub['STR'])

            age = determineAge(race, class_role)
            print('Age: ' + str(age))

            abilities = adjustAbilitiesForAge(race,age,abilities)
            abilities = enforceRacialAbilityLimits(race, abilities)
            
            gold = determineStartingGold(class_role)
            
            hp = determineStartingHP(class_role)



        self.race = race
        self.base_abilities = abilities_base
        self.abilities = abilities
        self.abilities_sub = abilities_sub
        self.inventory = None
        self.gold = gold
        self.age = age
        self.weight = 0

#Roll scores, allow user to select a set
def determineAbilityScores(auto=False):
    sets = [None] * 3
    for i in range(3):
        ability_set = [0] * 6
        for j in range(6):
            stat = roll(6,4,drop_low=True)
            ability_set[j] = stat
        ability_set = sorted(ability_set, reverse=True)
        sets[i] = ability_set

    #For skipping/debug
    if auto:
        return sets[0]

    print('A: ' + str(sets[0]))
    print('B: ' + str(sets[1]))
    print('C: ' + str(sets[2]))



    while(True):
        choice = input('Choose a set: ').upper()
        if choice == 'A':
            return sets[0]
        elif choice == 'B':
            return sets[1]
        elif choice == 'C':
            return sets[2]

#allow user to assign ability scores to each ability
def assignAbilityScores(scores, auto=False):
    abilities = OrderedDict([('STR',0),('INT',0),('WIS',0),
        ('DEX',0),('CON',0),('CHR',0)])

    #debug
    if auto:
        i=0
        for k in abilities:
            abilities[k] = scores[i]
            i += 1
        return abilities


    print(scores)
    for k in abilities:
        valid = False
        while not valid:
            try:
                choice = int(input(k+': '))
                if choice in scores:
                    abilities[k] = choice
                    valid = True
                    scores.remove(choice)
                else:
                    print(scores)
            except ValueError:
                pass

    return abilities

#User selects a race, taking into account racial attribute minimums
def chooseRace(abils):
    races = {'Human','Dwarf','Elf','Gnome',
        'Halfling','Half-Elf','Half-Orc'}

    str = abils['STR']
    if str < 8:
        races.discard('Dwarf')
    if str < 7:
        races.discard('Halfling')
    if str < 6:
        races.discard('Gnome')
    if str < 5:
        races.discard('Half-Orc')

    intel = abils['INT']
    if intel < 8:
        races.discard('Elf')
    if intel < 7:
        races.discard('Gnome')
    if intel < 6:
        races.discard('Halfling')
    if intel < 4:
        races.discard('Half-Elf')

    dex = abils['DEX']
    if dex < 7:
        races.discard('Halfling')
    if dex < 6:
        races.discard('Elf')
        races.discard('Half-Elf')

    con = abils['CON']
    if con < 12:
        races.discard('Half-Orc')
    if con < 11:
        races.discard('Dwarf')
    if con < 10:
        races.discard('Halfling')
    if con < 8:
        races.discard('Gnome')
    if con < 7:
        races.discard('Elf')
    if con < 6:
        races.discard('Half-Elf')

    chr = abils['CHR']
    if chr < 8:
        races.discard('Elf')
    if chr < 5:
        races.discard('Half-Orc')
    if chr < 4:
        races.discard('Dwarf')

    #Convert races to sorted list
    races = sorted(races)
    print(races)

    options = OrderedDict()
    alpha = list(ascii_uppercase)[:len(races)]
    for letter in alpha:
        options[letter] = races.pop(0)


    for k in options:
        print (k + ': ' + options[k])
    choice = None
    while choice not in options.keys():
        choice = input('Choose race: ').upper()

    return options[choice]


def adjustAbilitiesForRace(race,abils):
#Note Charisma adjustments are not made here,
#as original charisma needs to be retained for same race relations
    if race == 'Dwarf':
        abils['CON'] += 1
        abils['DEX'] -= 1
    elif race == 'Elf':
        abils['DEX'] += 1
        abils['CON'] -= 1
    elif race == 'Halfling':
        abils['STR'] -= 1
        abils['DEX'] += 1
    elif race == 'Half-Orc':
        abils['STR'] += 1
        abils['CON'] += 1
        abils['CHR'] -= 2

    return abils




def chooseClass(race, abils):
    classes = {'Cleric','Druid','Fighter','Paladin','Ranger','Magic User','Illusionist',
        'Thief','Assassin','Monk'}

    if abils['STR'] < 15:
        classes.discard('Monk')
        if abils['STR'] < 13:
            classes.discard('Ranger')
            if abils['STR'] < 12:
                classes.discard('Paladin')
                classes.discard('Assassin')
                if abils['STR'] < 9:
                    classes.discard('Fighter')

    if abils['INT'] < 15:
        classes.discard('Illusionist')
        if abils['INT'] < 13:
            classes.discard('Ranger')
            if abils['INT'] < 11:
                classes.discard('Assassin')
                if abils['INT'] < 9:
                    classes.discard('Paladin')
                    classes.discard('Magic-User')

    if abils['WIS'] < 15:
        classes.discard('Monk')
        if abils['WIS'] < 14:
            classes.discard('Ranger')
            if abils['WIS'] < 13:
                classes.discard('Druid')
                classes.discard('Paladin')
                if abils['WIS'] < 9:
                    classes.discard('Cleric')

    if abils['DEX'] < 16:
        classes.discard('Illusionist')
        if abils['DEX'] < 15:
            classes.discard('Monk')
            if abils['DEX'] < 12:
                classes.discard('Assassin')
                if abils['DEX'] < 9:
                    classes.discard('Thief')
                    if abils['DEX'] < 6:
                        classes.discard('Magic-User')

    if abils['CON'] < 14:
        classes.discard('Ranger')
        if abils['CON'] < 11:
            classes.discard('Monk')
            if abils['CON'] < 9:
                classes.discard('Paladin')
                if abils['CON'] < 7:
                    classes.discard('Fighter')

    if abils['CHR'] < 17:
        classes.discard('Paladin')
        if abils['CHR'] < 15:
            classes.discard('Druid')


    if race == 'Dwarf':
        classes.discard('Druid')
        classes.discard('Paladin')
        classes.discard('Magic-User')
        classes.discard('Illusionist')
        classes.discard('Monk')
    elif race == 'Elf':
        classes.discard('Paladin')
        classes.discard('Illusionist')
    elif race == 'Gnome':
        classes.discard('Paladin')
        classes.discard('Monk')
    elif race == 'Half-Elf':
        classes.discard('Illusionist')
    elif race == 'Halfling':
        classes.discard('Paladin')
        classes.discard('Magic-User')
        classes.discard('Illusionist')
        classes.discard('Monk')
    elif race == 'Half-Orc':
        classes.discard('Druid')
        classes.discard('Paladin')
        classes.discard('Illusionist')
        classes.discard('Monk')

    #convert classes to sorted list
    classes = sorted(classes)

    options = OrderedDict()
    alpha = list(ascii_uppercase)[:len(classes)]
    for letter in alpha:
        options[letter] = classes.pop(0)

    for k in options:
        print (k + ': ' + options[k])
    choice = None
    while choice not in options.keys():
        choice = input('Choose class: ').upper()

    return options[choice]

def determineAge(race,p_class):
    age = 0
    if race == 'Human':
        if p_class == 'Cleric' or p_class == 'Druid' or p_class =='Thief':
            age = 18 + roll(4)
        elif p_class == 'Fighter':
            age = 15 + roll(4)
        elif p_class == 'Paladin':
            age = 17 + roll(4)
        elif p_class == 'Ranger' or p_class == 'Assassin':
            age = 20 + roll(4)
        elif p_class == 'Magic-User':
            age = 25 + roll(8,2)
        elif p_class == 'Illusionist':
            age = 30 + roll(6)
        elif p_class == 'Monk':
            age = 21 + roll(4)

        return age

    cleric = ['Cleric','Druid','Monk']
    fighter = ['Fighter','Paladin','Ranger']
    thief = ['Thief', 'Assassin']
    magic = ['Magic-User', 'Illusionist']

    if race == 'Dwarf':
        if p_class in cleric:
            age = 250 + roll(20,2)
        elif p_class in fighter:
            age = 40 + roll(4,5)
        elif p_class in thief:
            age = 75 + roll(6,3)
    elif race == 'Elf':
        if p_class in cleric:
            age = 500 + roll(10,10)
        elif p_class in fighter:
            age = 130 + roll(6,5)
        elif p_class in magic:
            age = 150 + roll(6,5)
        elif p_class in thief:
            age = 100 + roll(6,5)
    elif race == 'Gnome':
        if p_class == 'Cleric':
            age = 300 + roll(12,3)
        elif p_class == 'Fighter':
            age = 60 + roll(4,5)
        elif p_class == 'Magic-User':
            age = 100 + roll(12,2)
        elif p_class == 'Thief':
            age = 80 + roll(4,5)
    elif race == 'Half-Elf':
        if p_class == 'Cleric':
            age = 40 + roll(4,2)
        elif p_class == 'Fighter':
            age = 22 + roll(4,3)
        elif p_class == 'Magic-User':
            age = 30 + roll(8,2)
        elif p_class == 'Thief':
            age = 22 + roll(8,3)
    elif race == 'Halfling':
        if p_class == 'Cleric':
            age = 36 + roll(4,2)
        elif p_class == 'Fighter':
            age = 20 + roll(4,3)
        elif p_class == 'Thief':
            age = 20 + roll(4,2)
    elif race == 'Half-Orc':
        if p_class == 'Cleric':
            age = 20 + roll(4)
        elif p_class == 'Fighter':
            age = 13 + roll(4)
        elif p_class == 'Magic-User':
            age = 15 + roll(8)
        elif p_class == 'Thief':
            age = 20 + roll(4,2)

    return age

def determineAgeBracket(race, age):
    bracket = None
    if race == 'Dwarf':
        if age < 35:
            bracket = 'Child'
        elif age < 51:
            bracket = 'Young Adult'
        elif age < 151:
            bracket = 'Mature'
        elif age < 251:
            bracket = 'Middle Aged'
        elif age < 351:
            bracket = 'Old'
        else:
            bracket = 'Venerable'
    elif race == 'Elf': #using high elf ages
        if age < 100:
            bracket = 'Child'
        elif age < 176:
            bracket = 'Young Adult'
        elif age < 551:
            bracket = 'Mature'
        elif age < 876:
            bracket = 'Middle Aged'
        elif age < 1201:
            bracket = 'Old'
        else:
            bracket = 'Venerable'
    elif race == 'Gnome':
        if age < 50:
            bracket = 'Child'
        elif age < 91:
            bracket = 'Young Adult'
        elif age < 301:
            bracket = 'Mature'
        elif age < 451:
            bracket = 'Middle Aged'
        elif age < 601:
            bracket = 'Old'
        else:
            bracket = 'Venerable'
    elif race == 'Half-Elf':
        if age < 24:
            bracket = 'Child'
        elif age < 41:
            bracket = 'Young Adult'
        elif age < 101:
            bracket = 'Mature'
        elif age < 176:
            bracket = 'Middle Aged'
        elif age < 251:
            bracket = 'Old'
        else:
            bracket = 'Venerable'
    elif race == 'Halfling':
        if age < 22:
            bracket = 'Child'
        elif age < 34:
            bracket = 'Young Adult'
        elif age < 69:
            bracket = 'Mature'
        elif age < 102:
            bracket = 'Middle Aged'
        elif age < 145:
            bracket = 'Old'
        else:
            bracket = 'Venerable'
    elif race == 'Half-Orc':
        if age < 12:
            bracket = 'Child'
        elif age < 16:
            bracket = 'Young Adult'
        elif age < 31:
            bracket = 'Mature'
        elif age < 46:
            bracket = 'Middle Aged'
        elif age < 61:
            bracket = 'Old'
        else:
            bracket = 'Venerable'
    elif race == 'Human':
        if age < 14:
            bracket = 'Child'
        elif age < 21:
            bracket = 'Young Adult'
        elif age < 41:
            bracket = 'Mature'
        elif age < 61:
            bracket = 'Middle Aged'
        elif age < 91:
            bracket = 'Old'
        else:
            bracket = 'Venerable'

def adjustAbilitiesForAge(race,age,abils):
    bracket = determineAgeBracket(race,age)

    if bracket == 'Child':
        pass
    elif bracket == 'Young Adult':
        abils['WIS'] -= 1
        abils['CON'] += 1
    elif bracket == 'Mature':
        abils['STR'] += 1
        abils['CON'] += 1
    elif bracket == 'Middle Aged':
        abils['WIS'] += 1
        abils['INT'] += 1
    elif bracket == 'Old':
        abils['STR'] -= 2
        abils['DEX'] -= 2
        abils['CON'] -= 1
        abils['INT'] += 1
        abils['WIS'] += 2
    else:
        abils['STR'] -= 3
        abils['DEX'] -= 3
        abils['CON'] -= 2
        abils['INT'] += 2
        abils['WIS'] += 3

    abils = enforceRacialAbilityLimits(race, abils)

    return abils

def enforceRacialAbilityLimits(race, abils):
    #Min STR
    if race == 'Dwarf':
        if abils['STR'] < 8:
            abils['STR'] = 8
    elif race in ['Gnome','Halfling','Half-Orc']:
        if abils['STR'] < 6:
            abils['STR'] = 6
    elif race in ['Elf','Half-Elf','Human']:
        if abils['STR'] < 3:
            abils['STR'] = 3
    #Max STR
    if race == 'Halfling':
        if abils['STR'] > 17:
            abils['STR'] = 17
    else:
        if abils['STR'] > 18:
            abils['STR'] = 18

    #Min INT
    if race == 'Elf':
        if abils['INT'] < 8:
            abils['INT'] = 8
    elif race == 'Gnome':
        if abils['INT'] < 7:
            abils['INT'] = 7
    elif race == 'Halfling':
        if abils['INT'] < 6:
            abils['INT'] = 6
    elif race == 'Half-Elf':
        if abils['INT'] < 4:
            abils['INT'] = 4
    else:
        if abils['INT'] < 3:
            abils['INT'] = 3
    #Max INT
    if race == 'Half-Orc':
        if abils['INT'] > 17:
            abils['INT'] = 17
    else:
        if abils['INT'] > 18:
            abils['INT'] = 18

    #Min WIS
    if abils['WIS'] < 3:
        abils['WIS'] = 3
    #Max WIS
    if race == 'Half-Orc':
        if abils['WIS'] > 14:
            abils['WIS'] = 14
    elif race == 'Halfling':
        if abils['WIS'] > 17:
            abils['WIS'] = 17
    else:
        if abils['WIS'] > 18:
            abils['WIS'] = 18

    #Min DEX
    if race == 'Halfling':
        if abils['DEX'] < 8:
            abils['DEX'] = 8
    elif race == 'Elf':
        if abils['DEX'] < 7:
            abils['DEX'] = 7
    elif race == 'Half-Elf':
        if abils['DEX'] < 6:
            abils['DEX'] = 6
    else:
        if abils['DEX'] < 3:
            abils['DEX'] = 3
    #Max DEX
    if race in ['Halfling', 'Elf']:
        if abils['DEX'] > 19:
            abils['DEX'] = 19
    elif race in ['Dwarf','Half-Orc']:
        if abils['DEX'] > 17:
            abils['DEX'] = 17
    else:
        if abils['DEX'] > 18:
            abils['DEX'] = 18

    #Min CON
    if race == 'Half-Orc':
        if abils['CON'] < 13:
            abils['CON'] = 13
    elif race == 'Dwarf':
        if abils['CON'] < 12:
            abils['CON'] = 12
    elif race == 'Halfling':
        if abils['CON'] < 10:
            abils['CON'] = 10
    elif race == 'Gnome':
        if abils['CON'] < 8:
            abils['CON'] = 8
    elif race in ['Elf', 'Half-Elf']:
        if abils['CON'] < 6:
            abils['CON'] = 6
    else:
        if abils['CON'] < 3:
            abils['CON'] = 3

    #Max CON
    if race in ['Dwarf', 'Halfling', 'Half-Orc']:
        if abils['CON'] > 19:
            abils['CON'] = 19
    else:
        if abils['CON'] > 18:
            abils['CON'] = 18

    #Min CHR
    if race == 'Elf':
        if abils['CHR'] < 8:
            abils['CHR'] = 8
    else:
        if abils['CHR'] < 3:
            abils['CHR'] = 3
    #Max CHR
    if race == 'Half-Orc':
        if abils['CHR'] > 12:
            abils['CHR'] = 12
    elif race == 'Dwarf':
        if abils['CHR'] > 16:
            abils['CHR'] = 16
    else:
        if abils['CHR'] > 18:
            abils['CHR'] = 18


    return abils

def determineStartingGold(p_class):
    gold = 0
    if p_class in ['Cleric','Druid']:
        gold = roll(6,3)*10
    elif p_class in ['Fighter','Paladin','Ranger']:
        gold = roll(4,5)*10
    elif p_class in ['Magic-User','Illusionist']:
        gold = roll(4,2)*10
    elif p_class in ['Thief','Assassin']:
        gold = roll(6,2)*10
    elif p_class == 'Monk':
        gold = roll(4,5)
        
    return gold

#Using 1st level minimums from UA p.74
def determineStartingHP(p_class, CON):
    hp = 0
    if p_class in ['Fighter','Paladin','Ranger']:
        if p_class == 'Ranger':
            hp = max(9, roll(8,2))
        else:
            hp = max(6, roll(10))
            
        if CON >= 18:
            hp += 4
        elif CON == 17:
            hp += 3
        elif CON == 16:
            hp += 2
        elif CON == 15:
            hp += 1
        elif CON in range(4,7):
            hp -= 1
        elif CON == 3:
            hp -= 2
    else:
        if p_class in ['Cleric','Druid']:
            hp = max(5,roll(8))
        elif p_class in ['Thief','Assassin']:
            hp = max(4,roll(6))
        elif p_class == 'Monk':
            hp = max(5,roll(4,2))
        elif p_class in ['Magic-User','Illusionist']:
            hp = max(3,roll(4))
        
        if CON >= 16:
            hp += 2
        elif CON == 15:
            hp += 1
        elif CON in range(4,7):
            hp -= 1
        elif CON == 3:
            hp -= 2
        
        
        
    

