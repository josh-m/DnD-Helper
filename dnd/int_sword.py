from dnd.roll import roll

from math import ceil
from random import choice

class IntelligentSword():
    def __init__(self, sword, r):
        self.sword = sword
        self.communication = None
        self.languages = 0
        self.telepathy = False
        self.read = False
        self.read_magic = False
        self.alignment = None
        self.ego = None
        self.intellect = 0
        self.alignment = None
        self.abilities = None
        self.purpose = None
        
        abilities = None
        iq = 0
        ego = 0
        num_languages = 0

        if r < 76:
            raise ValueError
        elif r < 84:
            iq = 12
            abilities,a_ego,self.purpose,self.purpose_power = generateAbilities(1)
        elif r < 90:
            iq = 13
            abilities,a_ego,self.purpose,self.purpose_power = generateAbilities(2)
        elif r < 95:
            iq = 14
            abilities,a_ego,self.purpose,self.purpose_power = generateAbilities(2)
        elif r < 98:
            iq = 15
            abilities,a_ego,self.purpose,self.purpose_power = generateAbilities(3)
        elif r < 100:
            iq = 16
            abilities,a_ego,self.purpose,self.purpose_power = generateAbilities(3)
        elif r == 100:
            iq = 17
            abilities,a_ego,self.purpose,self.purpose_power = generateAbilities(3,1)
        
        #Languages, communication
        if iq == 12:
            self.communication = 'Semi-Empathy'
        elif iq == 13:
            self.communication = 'Empathy'  
        elif iq > 13:
            self.communication = 'Speech'
            self.languages = determineLanguageCount()
            
            if iq > 15:
                self.read = True
            if iq > 16:
                self.telepathy = True
                self.communication += ' & Telepathy'
                self.read_magic = True
            
                
        self.determineEgo(a_ego)
        self.intellect = iq
        self.abilities = abilities
        self.determineAlignment(self.sword.name)
        
        
    def __str__(self):
        ret = self.alignment +' ' + str(self.sword)
       
        ret += '\n  INT: {}  Ego: {}\n  Communication: {}'.format(self.intellect,self.ego, self.communication)
        if self.languages > 0:
            ret +=', speaks alignment tongue and {} other languages'.format(self.languages)
        if self.read:
            ret +='\n  The sword can read these languages'
            if self.read_magic:
                ret += ', as well as magical writings'

        if self.purpose:
            ret += '\n  The sword\'s goal is to '+self.purpose
            ret +='\n  When fighting for this goal, the sword causes '+self.purpose_power

        ret += '\n  Abilities:'
        for abil in self.abilities:
            ret += '\n  ' + abil
  
        return ret

    def determineEgo(self, abil_ego=None):
        ego = abil_ego
        if not self.ego:
            ego += self.sword.bonus
            if self.purpose: ego += 5
            ego += ceil(0.5 * self.languages)
            if self.telepathy: ego += 2
            if self.read: ego += 1
            if self.read_magic: ego += 2
                
            self.ego = ego
            
        return self.ego
        
    def determineAlignment(self, name):
        align = None
        
        if 'Cursed' in name:
            align = 'True Neutral'
        elif 'Sharpness' in name:
            r = roll(20)
            if r < 6:
                align = 'Chaotic Good'
            elif r < 16:
                align = 'Chaotic Neutral'
            else:
                align = 'Chaotic Evil'
        elif 'Vorpal' in name:
            r = roll(35)
            if r < 6:
                align = 'Lawful Evil'
            elif r < 31:
                align = 'Lawful Good'
            else:
                align = 'Lawful Neutral'
        elif 'Holy Avenger' in name:
            align = 'Lawful Good'
        elif 'Sun Blade' in name:
            r = roll(9)
            if r == 1:
                align = 'Chaotic Good'
            elif r < 6:
                align = 'Neutral Good'
            else:
                align = 'Lawful Good'
        else:
            r = roll(100)
            if r < 6:
                align = 'Chaotic Good'
            elif r < 16:
                align = 'Chaotic Neutral'
            elif r < 21:
                align = 'Chaotic Evil'
            elif r < 26:
                align = 'Neutral Evil'
            elif r < 31:
                align = 'Lawful Evil'
            elif r < 56:
                align = 'Lawful Good'
            elif r < 61:
                align = 'Lawful Neutral'
            elif r < 81:
                align = 'True Neutral'
            else:
                align = 'Neutral Good'
                
        self.alignment = align

def determineLanguageCount():
    rolls = 1
    max_roll = 100
    bonus = False
    num_languages = 0
    
    while rolls > 0:
        rolls -= 1
        r = roll(max_roll)
        if r < 41:
            num_languages += 2
        elif r < 71:
            num_languages += 3
        elif r < 86:
            num_languages += 4
        elif r < 96:
            num_languages += 5
        elif r < 100:
            bonus = True
            rolls = 2
    if bonus:
        num_languages = max(6,num_languages)

    return num_languages
    
#returns a tuple [abilities_strings, ego]
def generateAbilities(num_primary, num_exceptional=0):
    total_primary = num_primary
    total_exceptional = num_exceptional
    
    abilities = {}
    abilities_strings = []
    purpose = None
    purpose_power = None

    bonus_roll = False
    while num_primary > 0:
        num_primary -= 1
    
        abil = ''
        range = 0
        
        #Don't allow more bonus rolls or exceptional abilities
        #after bonus rolls are granted once
        if not (bonus_roll and num_primary < 3):
            r = roll(100)
        else:
            r = roll(92)

        if r < 12:
            range = 1
            abil = 'Detect "elevator"/shifting rooms/walls'
        elif r < 23:
            range = 1
            abil = 'Detect sloping passages'
        elif r < 34:
            range = 1
            abil = 'Detect traps of large size'
        elif r < 45:
            range = 1
            abil = 'Detect evil/good'
        elif r < 56:
            range = 2
            abil = 'Detect precious metals (kind and amount)'
        elif r < 67:
            range = 0.5
            abil = 'Detect gems (kind and number)'
        elif r < 78:
            range = 1
            abil = 'Detect magic'
        elif r < 83:
            range = 0.5
            abil = 'Detect secret doors'
        elif r < 88:
            range = 1
            abil = 'Detect invisible objects'
        elif r < 93:
            range = 12
            abil = 'Locate object'
        elif r < 99:
            num_primary += 2
            total_primary += 1
            bonus_roll = True
        else:
            num_exceptional += 1
            total_exceptional += 1
            
        if abil in abilities:
            abilities[abil] += range
        elif abil != '':
            abilities[abil] = range
    
    for abil in abilities.items():
        abilities_strings.append(abil[0]+' in a {}" radius'.format(abil[1]))
    
    #Determine exceptional abilities
    abilities = {}
    bonus_roll = False
    while num_exceptional > 0:
        num_exceptional -= 1
        
        abil = ''
        uses = 0
        
        r = roll(100)

        if r < 8:
            abil = 'Charm person on contact'
            uses = 3
        elif r < 16:
            abil = 'Clairaudience 3" range 1 round per use'
            uses = 3
        elif r < 23:
            abil = 'Clairvoyance 3" range 1 round per use'
            uses = 3
        elif r < 29:
            abil = 'Determine directions and depth'
            uses = 2
        elif r < 35:
            abil = 'ESP 3" range 1 round per use'
            uses = 3
        elif r < 42:
            abil = 'Flying 12"/turn'
            uses = 1
        elif r < 48:
            abil = 'Heal'
            uses = 1
        elif r < 55:
            abil = 'Illusion 12" range (as wand)'
            uses = 2
        elif r < 62:
            abil = 'Levitation 1 turn duration (as 6th level)'
            uses = 3
        elif r < 68:
            abil = 'Strength (wielder)'
            uses = 1
        elif r < 76:
            abil = 'Telekinesis 2500gp weight 1 round per use'
            uses = 2
        elif r < 82:
            abil = 'Telepathy 6" range'
            uses = 2
        elif r < 89:
            abil = 'Teleportation 6000gp weight (2 segments)'
            uses = 1
        elif r < 95:
            abil = 'X-ray vision 4" range 1 turn per use'
            uses = 2
        elif r < 98:
            if bonus_roll:
                #reroll
                num_exceptional += 1
            else:
                bonus_roll = True
                num_exceptional = 2
                total_exceptional += 1
        else: 
            abil = 'Player choice'
            uses = 1
            
            #It is theoretically possible for 2 purposes to be rolled
            #by getting a bonus roll and then two 100s.
            #The wording of special purposes seem to not allow for this,
            #so I'm making this rare case grant 1 special purpose and 2 choices
            if r == 100 and (not purpose):
                r = roll(100)
                if r < 11:
                    purpose = 'defeat/slay diametrically opposed alignment'
                elif r < 21:
                    purpose = 'kill clerics'
                elif r < 31:
                    purpose = 'kill fighters'
                elif r < 41:
                    purpose = 'kill magic-users'
                elif r < 51:
                    purpose = 'kill thieves'
                elif r < 56:
                    purpose = 'kill bards and monks'
                elif r < 66:
                    purpose = 'overthrow law and/or chaos'
                elif r < 76:
                    purpose = 'slay good and/or evil'
                else:
                    purpose = 'slay non-human monsters'
                    
                r = roll(100)
                if r < 11:
                    purpose_power = 'blindness for 2d6 rounds on hit'
                elif r < 21:
                    purpose_power = 'confusion for 2d6 rounds on hit'
                elif r < 26:
                    purpose_power = 'disintegrate on hit'
                elif r < 56:
                    purpose_power = 'fear for 1d4 rounds on hit'
                elif r < 66:
                    purpose_power = 'insanity for 1d4 rounds on hit'
                elif r < 81:
                    purpose_power = 'paralysis for 1d4 rounds on hit'
                else:
                    purpose_power = '+2 on all saving throws, -1 on each damage die sustained for it\'s wielder'
                
        if abil in abilities:
            abilities[abil] += uses
        elif abil != '':
            abilities[abil] = uses
                
    for abil in abilities.items():
        if abil[0] == 'Player choice':
            suffix = ' - {} pick'.format(abil[1])
            if abil[1] > 1:
                suffix += 's'
            abilities_strings.append(abil[0] + suffix)
        elif abil[0] == 'Flying 12"/turn':
            abilities_strings.append(abil[0] + ' - {} hours/day'.format(abil[1]))
        else:
            abilities_strings.append(abil[0]+' - {} times/day'.format(abil[1]))
    
    ability_ego = total_primary + (2*total_exceptional)
    if purpose:
        ability_ego += 5
        
    return [abilities_strings, ability_ego, purpose, purpose_power]
            
            
    
            