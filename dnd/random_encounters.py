
from dnd.roll import roll
from dnd.util import findNameInList
from dnd.basic_creature import creatureInfoFromName, BasicCreature
from dnd.fortress import Fortress
from dnd.region_tables import region_populations, region_names 


from random import choice, randint

def __main__():
    while True:
        region_name = input('Enter region: ')
        region = findNameInList(region_name, region_names)
        print(region)
        
        if type(region) is list:
            print('Found multiple matches:')
            for r in region:
                print(r)
        elif type(region) is str:
            encountered_name = pickEncounterInRegion(region)
            print(encountered_name)
            
            #Is it a non-creature encounter?
            if encountered_name == 'Fortress':
                print(Fortress())
                
            
            c_info = creatureInfoFromName(encountered_name)
            if c_info:
                num_encountered = randint(
                    c_info.num_appearing[0],
                    c_info.num_appearing[1])
                    
                if num_encountered < 15:
                    for i in range(num_encountered):
                        c = BasicCreature(c_info)
                        print(c)
                else:
                    print('{} {}'.format(num_encountered, c_info.name))

def rollMultipleDays(num_days, region, density):
    days = []
    for i in range(1, num_days+1):
        daily_encounters = rollDay(region, density)
        if len(daily_encounters):
            days.append( ('Day {}'.format(i), daily_encounters))
    
    return days
                    
def rollDay(region, density):
    encounters = []
    if density == 'Dense':
        die = 20
    elif density == 'Sparse':
        die = 12
    else:
        die = 10
        
    if 'Plains' in region:
        enc = checkDailyEncounters(region, die,
            ('Morning','Evening','Midnight'))
    elif 'Scrub' in region:
        reg = region.replace('Scrub', 'Plains')
        enc = checkDailyEncounters(reg, die,
            ('Morning','Evening','Night','Pre-Dawn'))
    elif 'Forest' in region:
        enc = checkDailyEncounters(region, die,
            ('Morning','Noon','Evening','Night','Midnight','Pre-Dawn'))
    elif 'Desert' in region:
        enc = checkDailyEncounters(region, die,
            ('Morning','Night','Pre-Dawn'))
    elif 'Hills' in region:
        enc = checkDailyEncounters(region, die,
            ('Noon','Night','Pre-Dawn'))
    elif 'Mountains' in region:
        enc = checkDailyEncounters(region, die,
            ('Morning','Night'))
    elif 'Marsh' in region or 'Swamp' in region:
        enc = checkDailyEncounters(region, die,
            ('Morning','Noon','Evening','Night','Midnight','Pre-Dawn'))
    else:
        raise ValueError
        
    return enc

def checkDailyEncounters(region, die, time_list):
    encounters = []
    for t in time_list:
        r = roll(die)
        if r == 1:
            e = pickEncounterInRegion(region)
            encounters.append( (t,e) )
    return encounters
           
def pickEncounterInRegion(region):
    r = roll(12) + roll(8)
    encounter_list = []
    
    if (8 < r < 14):
        encounter_list = region_populations[region].C
    elif (r == 7 or r == 8 or r == 14 or r == 15):
        encounter_list = region_populations[region].UC
    elif (r == 5 or r == 6 or r == 16 or r == 17):
        encounter_list = region_populations[region].R
    elif (r == 4) or (r == 18):
        r = roll(2)
        if r == 1: encounter_list = region_populations[region].VR
        else: encounter_list = region_populations[region].R     
    elif (r < 4) or (r > 18):
        encounter_list = region_populations[region].VR
        
    return choice(encounter_list)

def classicRandomEncounter(region):
    r = roll(12) + roll(8)
    r -= 2
    encounter_list = regions[region]
    return encounter_list[r]

if __name__ == '__main__':
    __main__()