from random import random
from math import ceil
from roll import roll



def test_combat():
    A = Party()
    B = Party()

    surA = surprise_segments(A,B)
    surB = surprise_segments(B,A)

    distance = determine_distance_outdoor(max(surA, surB))

    print('Encounter at a distance of {} yards'.format(distance))
    if surA > surB:
        print('Party A is surprised for {} segements'.format(surA - surB))
    elif surB > surB:
        print('Party B is surprised for {} segments'.format(surB - surA))

    """surprise actions if applicable"""
    
    #loop until encounter resolved
    """pre initiative actions"""

    initiative = determine_initiative()
    if not initiative:
        print('Combat simultaneous this round')
    else:
        print('Party {} goes first'.format(initiative))
    

    

class Party():
    BASE_SURPRISE = 2.0/6

    def __init__(self):
        self.surprised_chance = Party.BASE_SURPRISE
        self.cause_surprise_mod = 0.0
        self.party_members = []
    
    def add_member(creature):
        self.party_memebers.append(creature)

    def remove_member(creature):
        self.party_members.remove(creature)

class CombatEncounter():
    def __init__(self):
        pass

#return the number of segments surprised,
#positive for A, negative for B
def resolve_surprise(A,B):
    surA = surprise_segments(A,B)
    surB = surprise_segments(B,A)

    return surA - surB

def surprise_segments(us, them):
    chance = us.surprised_chance + them.cause_surprise_mod
    r = random()
    if r < chance:
        return ceil(r / (1.0/6))
    return 0

#TODO: factor in terrain
def determine_distance_outdoor(surprise_mod):
    r = roll(6,4)

    yards_distance = r - surprise_mod

    return yards_distance

def determine_initiative():
    r1 = roll(6)
    r2 = roll(6)

    if r1 > r2:
        return 'A'
    elif r1 < r2:
        return 'B'
    return None


if __name__ == "__main__":
    test_combat()
    
    
