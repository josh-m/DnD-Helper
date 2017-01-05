hp_values = {0:1,1:1,2:2,3:3,4:4,5:5,6:6,7:8,8:10,9:12,10:14,11:16,
            12:18,13:20,14:25,15:30,16:35}
special_values = {0:2,1:4,2:8,3:15,4:25,5:40,6:75,7:125,8:175,9:300,
                 10:450,11:700,12:950,13:1250,14:1550,15:2100, 16:2600}
exceptional_values = {0:25,1:35,2:45,3:55,4:65,5:75,6:125,7:175,8:275,
                      9:400,10:600,11:850,12:1200,13:1600,14:2000,15:2500,16:3000}

                      

def determineXPperHP(hd, xp_mod):
    effective_hd = hd + (xp_mod // 8)
    
    if effective_hd <= 0: xp = 5; bracket = 0
    elif effective_hd == 1: xp = 10; bracket = 1
    elif effective_hd == 2: xp = 20; bracket = 2
    elif effective_hd == 3: xp = 35; bracket = 3
    elif effective_hd == 4: xp = 60; bracket = 4
    elif effective_hd == 5: xp = 90; bracket = 5
    elif effective_hd == 6: xp = 150; bracket = 6
    elif effective_hd == 7: xp = 225; bracket = 7
    elif effective_hd == 8: xp = 375; bracket = 8
    elif effective_hd == 9: xp = 600; bracket = 9
    elif effective_hd < 11: xp = 900; bracket = 10
    elif effective_hd < 13: xp = 1300; bracket = 11
    elif effective_hd < 15 : xp = 1800; bracket = 12
    elif effective_hd < 17: xp = 2400; bracket = 13
    elif effective_hd < 19: xp = 3000; bracket = 14
    elif effective_hd < 21 : xp = 4000; bracket = 15
    else: xp = 5000; bracket = 16
    
    return hp_values[bracket]
    
    
                      
#Manual XP determination (largely obsolete with xp tables)
#Set up to be used with CreatureType instances 
def determineXP(creature):

    xp_per_hp = determineXPperHP(
        creature.hit_die[0],
        creature.hit_die[1])
    
    xp = xp_per_hp * creature.hp
    
    special_count = len(creature.c_type.special)
    if creature.c_type.AC < 1:
        special_count += 1
    if len(creature.c_type.attacks) > 3:
        special_count += 1
    if creature.intelligence > 14:
        special_count += 1
    
    exceptional_count = len(creature.c_type.exceptional)
    dmg = []
    for att in creature.c_type.attacks:
        max_dmg = att[0] * att[1] + att[2]
        dmg.append(max_dmg)
        
    if len(dmg) == 1:
        if dmg[0] > 23: exceptional_count += 1
    elif len(dmg) == 2:
        if sum(dmg) > 29: exceptional_count += 1
    elif len(dmg) == 3:
        if sum(dmg) > 35: exceptional_count += 1
    elif len(dmg) > 3:
        if sum(dmg) > 41: exceptional_count += 1

    if creature.c_type.magic_resist > 0:
        exceptional_count += 1
        if creature.c_type.magic_resist > 0.5:
            exceptional_count += 1
        
    xp += special_count * special_values[bracket]
    xp += exceptional_count * exceptional_values[bracket]

    return xp