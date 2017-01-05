from dnd.currency import Coin

class MeleeWeapon():
    def __init__(
        self,name,weight,dmg_die,dmg_num,dmg_mod,L_dmg_die,L_dmg_num,L_dmg_mod,
        space,speed,value,ac_adjustments,
        recieve_bonus=False,L_recieve_bonus=False,mount_charge_bonus=False):
        
        self.name = name
        self.value = value
        self.weight = weight
        self.die = dmg_die
        self.num = dmg_num
        self.mod = dmg_mod
        self.die_lg = L_dmg_die
        self.num_lg = L_dmg_num
        self.mod_lg = L_dmg_mod
        self.space = space
        self.speed = speed
        self.ac_adjust = ac_adjustments
    
    def __str__(self):
        return self.name
   
fist = MeleeWeapon('Fist',0,6,1,0,6,1,0,0,1,Coin(0,'c'),
    [-7,-5,-3,-1,0,0,2,0,4])
axe_battle = MeleeWeapon('Battle Axe',75,8,1,0,8,1,0,4,7,Coin(5,'g'),
    [-3,-2,-1,-1,0,0,1,1,2])
axe_hand = MeleeWeapon('Hand Axe',50,6,1,0,4,1,0,1,4,Coin(1,'g'),
    [-3,-2,-2,-1,0,0,1,1,1])
bardiche = MeleeWeapon('Bardiche',125,4,2,0,4,3,0,5,9,Coin(7,'g'),
    [-2,-1,0,0,1,1,2,2,3])
bec_de_corbin = MeleeWeapon('Bec de Corbin',100,8,1,0,6,1,0,6,9,Coin(6,'g'),
    [2,2,2,0,0,0,0,0,-1])
bill_guisarme = MeleeWeapon('Bill-Guisarme',150,4,2,0,10,1,0,2,10,Coin(6,'g'),
    [0,0,0,0,0,0,1,0,0])
bo_stick = MeleeWeapon('Bo Stick',15,6,1,0,3,1,0,3,3,Coin(50,'s'),
    [-9,-7,-5,-3,-1,0,1,0,3])
club = MeleeWeapon('Club',30,6,1,0,3,1,0,2,4,Coin(50,'s'),
    [-5,-4,-3,-2,-1,-1,0,0,1])
dagger = MeleeWeapon('Dagger',10,4,1,0,3,1,0,1,2,Coin(2,'g'),
    [-3,-3,-2,-2,0,0,1,1,3])
fauchard = MeleeWeapon('Fauchard',60,6,1,0,8,1,0,2,8,Coin(3,'g'),
    [-2,-2,-1,-1,0,0,0,-1,-1])
fauchard_fork = MeleeWeapon('Fauchard-Fork',80,8,1,0,10,1,0,2,8,Coin(8,'g'),
    [-1,-1,-1,0,0,0,1,0,1])
flail_foot = MeleeWeapon('Footman\'s Flail',150,6,1,1,4,2,0,6,7,Coin(3,'g'),
    [2,2,1,2,1,1,1,1,-1])
flail_horse = MeleeWeapon('Horseman\'s Flail',35,4,1,1,4,1,1,4,6,Coin(8,'g'),
    [0,0,0,0,0,1,1,1,0])
fork_military = MeleeWeapon('Military Fork',75,8,1,0,4,2,0,1,7,Coin(4,'g'),
    [-2,-2,-1,0,0,1,1,0,1])
glaive = MeleeWeapon('Glaive',75,6,1,0,10,1,0,1,8,Coin(6,'g'),
    [-1,-1,0,0,0,0,0,0,0])
glaive_guisarme = MeleeWeapon('Glaive-Guisarme',100,4,2,0,6,2,0,1,9,Coin(10,'g'),
    [-1,-1,0,0,0,0,0,0,0])
guisarme = MeleeWeapon('Guisarme',80,4,2,0,8,1,0,2,8,Coin(5,'g'),
    [-2,-2,-1,-1,0,0,0,-1,-1])
guisarme_voulge = MeleeWeapon('Guisarme-Voulge',150,4,2,0,4,2,0,2,10,Coin(7,'g'),
    [-1,-1,0,1,1,1,0,0,0])  
halberd = MeleeWeapon('Halberd',175,10,1,0,6,2,0,5,9,Coin(9,'g'),
    [1,1,1,2,2,2,1,1,0])
hammer_lucern = MeleeWeapon('Lucerne Hammer',150,4,2,0,6,1,0,5,9,Coin(7,'g'),
    [1,1,2,2,2,1,1,0,0])
hammer = MeleeWeapon('Hammer',50,4,1,1,4,1,0,2,4,Coin(1,'g'),
    [0,1,0,1,0,0,0,0,0])
jo_stick = MeleeWeapon('Jo Stick',40,6,1,0,4,1,0,2,2,Coin(50,'s'),
    [-8,-6,-4,-2,-1,0,1,0,2])
lance_light = MeleeWeapon('Light Lance',50,6,1,0,8,1,0,1,6,Coin(6,'g'),
    [-2,-2,-1,0,0,0,0,0,0])
lance_med = MeleeWeapon('Medium Lance',100,6,1,1,6,2,0,1,7,Coin(6,'g'),
    [0,1,1,1,1,0,0,0,0])
lance_hvy = MeleeWeapon('Heavy Lance',150,4,2,1,6,3,0,1,8,Coin(6,'g'),
    [3,3,2,2,2,1,1,0,0])
mace_foot = MeleeWeapon('Footman\'s Mace',100,6,1,1,6,1,0,4,7,Coin(8,'g'),
    [1,1,0,0,0,0,0,1,-1])
mace_horse = MeleeWeapon('Horseman\'s Mace',50,6,1,0,4,1,0,2,6,Coin(4,'g'),
    [1,1,0,0,0,0,0,0,0])
morning_star = MeleeWeapon('Morning Star',125,4,2,0,6,1,1,5,7,Coin(5,'g'),
    [0,1,1,1,1,1,1,2,2])
partisan = MeleeWeapon('Partisan',80,6,1,0,6,1,1,3,9,Coin(10,'g'),
    [0,0,0,0,0,0,0,0,0])
pick_foot = MeleeWeapon('Footman\'s Military Pick',60,6,1,1,4,2,0,4,7,Coin(8,'g'),
    [2,2,1,1,0,-1,-1,-1,-2])
pick_horse = MeleeWeapon('Horseman\'s Military Pick',40,4,1,1,4,1,0,2,5,Coin(5,'g'),
    [1,1,1,1,0,0,-1,-1,-1])
pike = MeleeWeapon('Awl Pike',80,6,1,0,12,1,0,1,13,Coin(3,'g'),
    [-1,0,0,0,0,0,0,-1,-2])
ranseur = MeleeWeapon('Ranseur',50,4,2,0,4,2,0,1,8,Coin(4,'g'),
    [-2,-1,-1,0,0,0,0,0,1])
scimitar = MeleeWeapon('Scimitar',40,8,1,0,8,1,0,2,4,Coin(15,'g'),
    [-3,-2,-2,-1,0,0,1,1,3])
spear = MeleeWeapon('Spear',50,6,1,0,8,1,0,1,7,Coin(1,'g'),
    [-2,-1,-1,-1,0,0,0,0,0])
spetum = MeleeWeapon('Spetum',50,6,1,1,6,2,0,1,8,Coin(3,'g'),
    [-2,-1,0,0,0,0,0,1,2])
staff = MeleeWeapon('Quarter Staff',50,6,1,0,6,1,0,3,4,Coin(50,'s'),
    [-7,-5,-3,-1,0,0,1,1,1])
sword_bastard = MeleeWeapon('Bastard Sword',100,4,2,0,8,2,0,4,6,Coin(25,'g'),
    [0,0,1,1,1,1,1,1,0])
sword_broad = MeleeWeapon('Broad Sword',75,4,2,0,6,1,1,4,5,Coin(10,'g'),
    [-3,-2,-1,0,0,1,1,1,2])
sword_long = MeleeWeapon('Long Sword',60,8,1,0,12,1,0,3,5,Coin(15,'g'),
    [-2,-1,0,0,0,0,0,1,2])
sword_short = MeleeWeapon('Short Sword',35,6,1,0,8,1,0,1,3,Coin(8,'g'),
    [-3,-2,-1,0,0,0,1,0,2])
sword_2h = MeleeWeapon('Two-Handed Sword',250,10,1,0,6,3,0,6,10,Coin(30,'g'),
    [2,2,2,2,3,3,3,1,0])
trident = MeleeWeapon('Trident',50,6,1,1,4,3,0,1,7,Coin(4,'g'),
    [-3,-2,-1,-1,0,0,1,0,1])
voulge = MeleeWeapon('Voulge',125,4,2,0,4,2,0,2,10,Coin(2,'g'),
    [-1,-1,0,1,1,1,0,0,0])

all_melee = [fist,axe_battle,axe_hand,bardiche,bec_de_corbin,bill_guisarme,
    bo_stick,club,dagger,fauchard,fauchard_fork,flail_foot,flail_horse,
    fork_military,glaive,glaive_guisarme,guisarme,guisarme_voulge,
    halberd,hammer_lucern,hammer,jo_stick,lance_light,lance_med,lance_hvy,
    mace_foot,mace_horse,morning_star,partisan,pick_foot,pick_horse,
    pike,ranseur,scimitar,spear,spetum,staff,sword_bastard,sword_broad,
    sword_long,sword_short,sword_2h,trident,voulge]

def avg_dmg(die,num,mod):
    avg_die = die/2 + 0.5
    
    return ((avg_die * num) + mod)
    
def avg_weapon_dmg(weapon):
    vs_reg = avg_dmg(weapon.die, weapon.num, weapon.mod)
    vs_lg = avg_dmg(weapon.die_lg, weapon.num_lg, weapon.mod_lg)
    
    return [vs_reg, vs_lg]
    
def dmg_sorted(weapon_list=None):
    if weapon_list:
        weapons = weapon_list
    else:
        weapons = all_melee
        
    s = sorted(weapons, key=lambda weapon: avg_weapon_dmg(weapon)[0], reverse=True)
    for w in s:
        print(str(avg_weapon_dmg(w)[0]) + ' ' + str(w))
        
    return s

def dmg_lg_sorted(weapon_list=None):
    if weapon_list:
        weapons = weapon_list
    else:
        weapons = all_melee
        
    s = sorted(weapons, key=lambda weapon: avg_weapon_dmg(weapon)[1], reverse=True)
    for w in s:
        print(str(avg_weapon_dmg(w)[1]) + ' ' + str(w))
    
def speed_sorted(weapon_list=None):
    if weapon_list:
        weapons = weapon_list
    else:
        weapons = all_melee
        
    s = sorted(weapons, key=lambda weapon: weapon.speed)
    for w in s:
        print(str(w.speed) + ' ' + str(w))
        
    return s
    























