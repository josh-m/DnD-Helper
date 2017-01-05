from dnd.roll import roll
from dnd.spells import randomSpellScroll, randomSpell
from dnd.magic_weapon import generateSword, generateMiscWeapon
from dnd.relic import generateRelic

from random import randint

def generateMagicWeapon():
    return generateMagicItem(76)

#Using UA tables
def generateMagicItem(min_roll=1, restrict_weapons=False, restrict_sword=False,
                      restrict_potion=False):
    item = None
    valid = False
    while valid == False:
        valid = True
        r = randint(min_roll,100)
        if r < 21:
            if restrict_potion: valid = False
            else: item = generatePotion()
        elif r < 36:
            item = generateScroll()
        elif r < 41:
            item = generateRing()
        elif r < 46:
            item = generateRodStaffWand()
        elif r < 61:
            item = generateMiscMagic()
        elif r < 76:
            item = generateArmorShield()
        elif r < 87:
            if restrict_weapons or restrict_sword: valid = False
            else: item = generateSword()
        else:
            if restrict_weapons: valid = False
            else: item = generateMiscWeapon()
        
    return item
    
def generatePotion():
    pot = None
    table_roll = roll(100)
    
    if table_roll < 66:
        r = roll(100)
        if r < 4: pot = 'Animal Control'
        elif r < 7: pot = 'Clairaudience'
        elif r < 10: pot = 'Clairvoyance'
        elif r < 13: pot = 'Climbing'
        elif r < 16: pot = 'Delusion'
        elif r < 19: pot = 'Diminution'
        elif r < 21: pot = 'Dragon Control'
        elif r < 24: pot = 'ESP'
        elif r < 27: pot = 'Extra-Healing'
        elif r < 30: pot = 'Fire Resistance'
        elif r < 33: pot = 'Flying'
        elif r < 35: pot = 'Gaseous Form'
        elif r < 37: pot = 'Giant Control'
        elif r < 40: pot = 'Giant Strength'
        elif r < 42: pot = 'Growth'
        elif r < 48: pot = 'Healing'
        elif r < 50: pot = 'Heroism'
        elif r < 52: pot = 'Human Control'
        elif r < 55: pot = 'Invisibility'
        elif r < 58: pot = 'Invulnerability'
        elif r < 61: pot = 'Levitation'
        elif r < 64: pot = 'Longevity'
        elif r < 67: pot = 'Oil of Etherealness'
        elif r < 70: pot = 'Oil of Slipperiness'
        elif r < 73: pot = 'Philter of Love'
        elif r < 76: pot = 'Philter of Persuasiveness'
        elif r < 79: pot = 'Plant Control'
        elif r < 82: pot = 'Polymorph Self'
        elif r < 85: pot = 'Poison'
        elif r < 88: pot = 'Speed'
        elif r < 91: pot = 'Super-Heroism'
        elif r < 94: pot = 'Sweet Water'
        elif r < 97: pot = 'Treasure Finding'
        elif r == 97: pot = 'Undead Control'
        else: pot = 'Water Breathing'
    else:
        r = roll(100)
        if r < 6: pot = 'Elixir of Health'
        elif r < 16: pot = 'Elixir of Life'
        elif r < 21: pot = 'Elixir of Madness'
        elif r < 26: pot = 'Elixir of Youth'
        elif r < 31: pot = 'Fire Breath'
        elif r < 36: pot = 'Oil of Acid Resistance'
        elif r < 41: pot = 'Oil of Disenchantment'
        elif r < 46: pot = 'Oil of Elemental Invulnerability'
        elif r < 50: pot = 'Oil of Fiery Burning'
        elif r < 56: pot = 'Oil of Fumbling'
        elif r < 61: pot = 'Oil of Impact'
        elif r < 66: pot = 'Oil of Sharpness'
        elif r < 71: pot = 'Oil of Timelessness'
        elif r < 76: pot = 'Philter of Beauty'
        elif r < 81: pot = 'Philter of Glibness'
        elif r < 86: pot = 'Philter of Stammering & Stuttering'
        elif r < 91: pot = 'Rainbow Hues'
        elif r < 96: pot = 'Ventriloquism'
        else: pot = 'Vitality'

    if (('Philter' not in pot) and
        ('Elixir' not in pot) and
        ('Oil' not in pot)):
        pot = 'Potion of ' + pot
    
    return pot
    
class Scroll():
    def __init__(self, spell_list):
        self.spells = spell_list
    
    def __str__(self):
        ret = 'Magical Scroll'
        for spell in self.spells:
            ret += "\n  " + spell
        
        return ret
    
def generateScroll():
    spells = []
    r = roll(100)
    if r < 86:
        r = roll(100)
        if r < 11: spells.extend(randomSpellScroll(1,1,4))
        elif r < 17: spells.extend(randomSpellScroll(1,1,6))
        elif r < 20: spells.extend(randomSpellScroll(1,2,9,2,7))
        elif r < 25: spells.extend(randomSpellScroll(2,1,4))
        elif r < 28: spells.extend(randomSpellScroll(2,1,8,1,6))
        elif r < 33: spells.extend(randomSpellScroll(3,1,4))
        elif r < 36: spells.extend(randomSpellScroll(3,2,9,2,7))
        elif r < 40: spells.extend(randomSpellScroll(4,1,6))
        elif r < 43: spells.extend(randomSpellScroll(4,1,8,1,6))
        elif r < 47: spells.extend(randomSpellScroll(5,1,6))
        elif r < 50: spells.extend(randomSpellScroll(5,1,8,1,6))
        elif r < 53: spells.extend(randomSpellScroll(6,1,6))
        elif r < 55: spells.extend(randomSpellScroll(6,3,8,3,6))
        elif r < 58: spells.extend(randomSpellScroll(7,1,8))
        elif r < 60: spells.extend(randomSpellScroll(7,2,9))
        elif r == 60: spells.extend(randomSpellScroll(7,4,9,4,7))
        elif r < 63: spells.append('Protection - Demons')
        elif r < 65: spells.append('Protection - Devils')
        elif r < 71: spells.append('Protection - Elementals')
        elif r < 77: spells.append('Protection - Lycanthropes')
        elif r < 83: spells.append('Protection - Magic')
        elif r < 88: spells.append('Protection - Petrification')
        elif r < 93: spells.append('Protection - Possession')
        elif r < 98: spells.append('Protection - Undead')
        else:
            r = roll(100)
            if r < 26:
                spells.append('Curse - Polymorph to Hostile Monster')
            elif r < 31:
                spells.append('Curse - Turn to Liquid')
            elif r < 41:
                spells.append('Curse - Teleport 200-1200 miles 20\' radius')
            elif r < 51:
                spells.append('Curse - Plane Shift 20\' radius')
            elif r < 76:
                spells.append('Curse - Fatal Disease 2d4 turns')
            elif r < 91:
                spells.append('Curse - Explosive Runes')
            elif r < 100:
                spells.append('Curse - De-magick Nearby Magic Item')
            else:
                random_spell = str(randomSpell())
                spells.append('Curse - '+random_spell+' as 12th level')
    else:
        r = roll(100)
        if r < 3: spells.append('Protection - Acid')
        elif r < 8:spells.append('Protection - Breath Weapons, Dragon')
        elif r < 13: spells.append('Protection - Breath Weapons, Non-Dragon')
        elif r < 18: spells.append('Protection - Cold')
        elif r < 23: spells.append('Protection - Electricity')
        elif r < 28: spells.append('Protection - Fire')
        elif r < 33: spells.append('Protection - Gas')
        elif r < 38: spells.append('Protection - Illusions')
        elif r < 43: spells.append('Protection - Paralyzation')
        elif r < 49: spells.append('Protection - Plants')
        elif r < 55: spells.append('Protection - Poison')
        elif r < 60: spells.append('Protection - Traps')
        elif r < 65: spells.append('Protection - Water')
        elif r < 71: spells.append('Protection - Weapons, Magical Blunt')
        elif r < 77: spells.append('Protection - Weapons, Magical Edged')
        elif r < 83: spells.append('Protection - Weapons, Magical Missile')
        elif r < 89: spells.append('Protection - Weapons, Non-Magic Blunt')
        elif r < 95: spells.append('Protection - Weapons, Non-Magic Edged')
        else: spells.append('Protection - Weapons, Non-Magic Missile')
    
    return Scroll(spells)
        
def generateRing():
    ring = None
    r = roll(100)
    if r < 68:
        r = roll(100)
        if r < 7: ring = 'Contrariness'
        elif r < 13: ring = 'Delusion'
        elif r < 15: ring = 'Djinni Summoning'
        elif r == 15: ring = 'Elemental Command'
        elif r < 22: ring = 'Feather Falling'
        elif r < 28: ring = 'Fire Resistance'
        elif r < 31: ring = 'Free Action'
        elif r < 34: ring = 'Human Influence'
        elif r < 41: ring = 'Invisibility'
        elif r < 44: ring = 'Mammal Control'
        elif r == 44: ring = 'Multiple Wishes'
        elif r < 61: ring = 'Protection'
        elif r == 61: ring = 'Regeneration'
        elif r < 64: ring = 'Shooting Stars'
        elif r < 66: ring = 'Spell Storing'
        elif r < 70: ring = 'Spell Turning'
        elif r < 76: ring = 'Swimming'
        elif r < 78: ring = 'Telekinesis'
        elif r < 80: ring = 'Three Wishes'
        elif r < 86: ring = 'Warmth'
        elif r < 91: ring = 'Water Walking'
        elif r < 99: ring = 'Weakness'
        elif r == 99: ring = 'Wizardry'
        elif r == 100: ring = 'X-Ray Vision'
    else:
        r = roll(100)
        if r < 9: ring = 'Animal Friendship'
        elif r < 11: ring = 'Anything'
        elif r < 21: ring = 'Blinking'
        elif r < 23: ring = 'Boccob'
        elif r < 32: ring = 'Chameleon Power'
        elif r < 41: ring = 'Clumsiness'
        elif r < 50: ring = 'Faerie'
        elif r < 59: ring = 'Jumping'
        elif r < 68: ring = 'Mind Shielding'
        elif r < 71: ring = 'the Ram'
        elif r < 80: ring = 'Shocking Grasp'
        elif r < 93: ring = 'Sustenance'
        else: ring = 'Truth'
            
    return 'Ring of ' + ring

def generateRod():
    return generateRodStaffWand(pick_rod=True)
    
def generateRodStaffWand(pick_rod=False):
    item = None
    r = 0
    if pick_rod:
        r = 1
    else:
        r = roll(100)
        
    if r < 41:
        if pick_rod:
            r = roll(40)
        else:
            r = roll(100)
        if r < 7: item = 'Rod of Absorption'
        elif r < 11: item = 'Rod of Alertness'
        elif r == 11: item = 'Rod of Beguiling'
        elif r < 22: item = 'Rod of Cancellation'
        elif r < 27: item = 'Rod of Flailing'
        elif r == 27: item = 'Rod of Lordly Might'
        elif r < 31: item = 'Rod of Passage'
        elif r == 31: item = 'Rod of Resurrection'
        elif r == 32: item = 'Rod of Rulership'
        elif r < 37: item = 'Rod of Security'
        elif r == 37: item = 'Rod of Smiting'
        elif r < 41: item = 'Rod of Splendor'
        elif r == 41: item = 'Staff of Command'
        elif r < 49: item = 'Staff of Curing'
        elif r < 56: item = 'Staff-Mace'
        elif r == 56: item = 'Staff of the Magi'
        elif r == 57: item = 'Staff of Power'
        elif r < 64: item = 'Staff of the Serpent'
        elif r < 71: item = 'Staff of Slinging'
        elif r < 77:
            item = 'Staff-Spear'
            suffix = ''
            r = roll(20)
            if r < 7:
                suffix = ' +1'
            elif r < 11:
                suffix = ' +2'
            elif r < 14:
                suffix = ' +3'
            elif r < 17:
                suffix = ' +4'
            elif r < 20:
                suffix = ' +5'
            else:
                suffix = ' +3, (Ranseur)'
            item += suffix
        elif r < 83: item = 'Staff of Striking'
        elif r < 86: item = 'Staff of Swarming'
        elif r == 86: item = 'Staff of Thunder & Lightning'
        elif r < 91: item = 'Staff of Withering'
        else: item = 'Staff of the Woodlands'
    else:
        r = roll(100)
        if r == 1: item = 'Anything'
        elif r < 6: item = 'Buckler'
        elif r < 8: item = 'Conjuration'
        elif r < 11: item = 'Defoliation'
        elif r < 13: item = 'Earth & Stone'
        elif r < 17: item = 'Enemy Detection'
        elif r < 21: item = 'Fear'
        elif r < 23: item = 'Fire'
        elif r < 27: item = 'Fireballs'
        elif r < 31: item = 'Flame Extinguishing'
        elif r == 31: item = 'Force'
        elif r == 32: item = 'Frost'
        elif r < 36: item = 'Ice Storms'
        elif r < 40: item = 'Illumination'
        elif r < 44: item = 'Illusion'
        elif r < 46: item = 'Lightning'
        elif r < 50: item = 'Lightning Bolts'
        elif r < 54: item = 'Magic Detection'
        elif r < 62: item = 'Magic Missiles'
        elif r < 67: item = 'Metal & Mineral Detection'
        elif r < 69: item = 'Metal Command'
        elif r < 75: item = 'Negation'
        elif r < 79: item = 'Paralyzation'
        elif r < 83: item = 'Polymorphing'
        elif r < 87: item = 'Secret Door & Trap Location'
        elif r < 91: item = 'Size Alteration'
        elif r < 93: item = 'Steam & Vapor'
        else: item = 'Wonder'
        
        item += ' Wand'
    
    return item
    
def generateMiscMagic():
    item = None
    r = roll(100)
    if r < 14:
        r = roll(100)
        if r < 3: item = 'Alchemy Jug'
        elif r < 5: item = 'Amulet of Inescapable Location'
        elif r < 6: item = 'Amulet of Life Protection'
        elif r < 8: item = 'Amulet of the Planes'
        elif r < 12: item = 'Amulet of Proof Against Detection and Location'
        elif r < 14: item = 'Apparatus of Kwalish'
        elif r < 17: item = 'Arrow of Direction'
        elif r < 18: item = generateRelic()
        elif r < 21: item = 'Bag of Beans'
        elif r < 22: item = 'Bag of Devouring'
        elif r < 27: item = 'Bag of Holding'
        elif r < 28: item = 'Bag of Transmuting'
        elif r < 30: item = 'Bag of Tricks'
        elif r < 32: item = 'Beaker of Plentiful Potions'
        elif r < 33: item = 'Folding Boat'
        elif r < 34: item = 'Book of Exalted Deeds'
        elif r < 35: item = 'Book of Infinite Spells'
        elif r < 36: item = 'Book of Vile Darkness'
        elif r < 37: item = 'Boots of Dancing'
        elif r < 43: item = 'Boots of Elvenkind'
        elif r < 48: item = 'Boots of Levitation'
        elif r < 52: item = 'Boots of Speed'
        elif r < 56: item = 'Boots of Striding and Springing'
        elif r < 59: item = 'Bowl of Commanding Water Elementals'
        elif r < 60: item = 'Bowl of Watery Death'
        elif r < 80: item = 'Bracers of Defense'
        elif r < 82: item = 'Bracers of Defenselessness'
        elif r < 85: item = 'Brazier of Commanding Fire Elementals'
        elif r < 86: item = 'Brazier of Sleep Smoke'
        elif r < 93: item = 'Brooch of Shielding'
        elif r < 94: item = 'Broom of Animated Attack'
        elif r < 99: item = 'Broom of Flying'
        else: item = 'Bucknard\'s Everfull Purse'
    elif r < 29:
        r = roll(100)
        if r < 7: item = 'Candle of Invocation'
        elif r < 9: item = 'Carpet of Flying'
        elif r < 11: item = 'Censer of Controlling Air Elementals'
        elif r < 12: item = 'Censer of Summoning Hostile Air Elementals'
        elif r < 14: item = 'Chime of Opening'
        elif r < 15: item = 'Chime of Hunger'
        elif r < 19: item = 'Cloak of Displacement'
        elif r < 28: item = 'Cloak of Elvenkind'
        elif r < 31: item = 'Cloak of Manta Ray'
        elif r < 33: item = 'Cloak of Poisonousness'
        elif r < 56: item = 'Cloak of Protection'
        elif r < 61: item = 'Crystal Ball'
        elif r < 62: item = 'Crystal Hypnosis Ball'
        elif r < 64: item = 'Cube of Force'
        elif r < 66: item = 'Cube of Frost Resistance'
        elif r < 68: item = 'Cubic Gate'
        elif r < 70: item = 'Daern\'s Instant Fortress'
        elif r < 73: item = 'Decanter of Endless Water'
        elif r < 77: item = 'Deck of Many Things'
        elif r < 78: item = 'Drums of Deafening'
        elif r < 80: item = 'Drums of Panic'
        elif r < 86: item = 'Dust of Appearance'
        elif r < 92: item = 'Dust of Disappearance'
        elif r < 93: item = 'Dust of Sneezing and Choking'
        elif r < 94: item = 'Efreeti Bottle'
        elif r < 95: item = 'Eversmoking Bottle'
        elif r < 96: item = 'Eyes of Charming'
        elif r < 98: item = 'Eyes of the Eagle'
        elif r < 100: item = 'Eyes of Minute Seeing'
        elif r == 100: item = 'Eyes of Petrification'
    elif r < 43:
        r = roll(100)
        if r < 16: item = 'Figurine of Wondrous Power'
        elif r < 17: item = 'Flask of Curses'
        elif r < 19: item = 'Gauntlets of Dexterity'
        elif r < 21: item = 'Gauntlets of Fumbling'
        elif r < 23: item = 'Gauntlets of Ogre Power'
        elif r < 26: item = 'Gauntlets of Swimming and Climbing'
        elif r < 27: item = 'Gem of Brightness'
        elif r < 28: item = 'Gem of Seeing'
        elif r < 29: item = 'Girdle of Femininity/Masculinity'
        elif r < 30: item = 'Girdle of Giant Strength'
        elif r < 31: item = 'Helm of Brilliance'
        elif r < 36: item = 'Helm of Comprehending Languages & Reading Magic'
        elif r < 38: item = 'Helm of Opposite Alignment'
        elif r < 40: item = 'Helm of Telepathy'
        elif r < 41: item = 'Helm of Teleportation'
        elif r < 46: item = 'Helm of Underwater Action'
        elif r < 47: item = 'Horn of Blasting'
        elif r < 49: item = 'Horn of Bubbles'
        elif r < 50: item = 'Horn of Collapsing'
        elif r < 54: item = 'Horn of the Tritons'
        elif r < 61: item = 'Horn of Valhalla'
        elif r < 64: item = 'Horseshoes of Speed'
        elif r < 66: item = 'Horseshoes of a Zephyr'
        elif r < 71: item = 'Incense of Meditation'
        elif r < 72: item = 'Incense of Obsession'
        elif r < 73: item = 'Ioun Stones'
        elif r < 79: item = 'Instrument of the Bards'
        elif r < 81: item = 'Iron Flask'
        elif r < 86: item = 'Javelin of Lightning'
        elif r < 91: item = 'Javelin of Piercing'
        elif r < 92: item = 'Jewel of Attacks'
        elif r < 93: item = 'Jewel of Flawlessness'
        elif r < 101: item = 'Keoghtom\'s Ointment'
    elif r < 57:
        r = roll(100)
        if r == 1: item = 'Libram of Gainful Conjuration'
        elif r == 2: item = 'Libram of Ineffable Damnation'
        elif r == 3: item = 'Libram of Silver Magic'
        elif r == 4: item = 'Lyre of Building'
        elif r == 5: item = 'Manual of Bodily Health'
        elif r == 6: item = 'Manual of Gainful Excercise'
        elif r == 7: item = 'Manual of Golems'
        elif r == 8: item = 'Manual of Puissant Skill at Arms'
        elif r == 9: item = 'Manual of Quickness of Action'
        elif r == 10: item = 'Manual of Stealthy Pilfering'
        elif r == 11: item = 'Mattock of the Titans'
        elif r == 12: item = 'Maul of the Titans'
        elif r < 16: item = 'Medallion of ESP'
        elif r < 18: item = 'Medallion of Thought Projection'
        elif r == 18: item = 'Mirror of Life Trapping'
        elif r == 19: item = 'Mirror of Mental Prowess'
        elif r == 20: item = 'Mirror of Opposition'
        elif r < 24: item = 'Necklace of Adaptation'
        elif r < 28: item = 'Necklace of Missiles'
        elif r < 34: item = 'Necklace of Prayer Beads'
        elif r < 36: item = 'Necklace of Strangulation'
        elif r < 39: item = 'Net of Entrapment'
        elif r < 43: item = 'Net of Snaring'
        elif r < 45: item = 'Nolzur\'s Marvelous Pigments'
        elif r < 47: item = 'Pearl of Power'
        elif r < 49: item = 'Pearl of Wisdom'
        elif r < 51: item = 'Periapt of Foul Rotting'
        elif r < 54: item = 'Periapt of Health'
        elif r < 61: item = 'Periapt of Proof Against Poison'
        elif r < 65: item = 'Periapt of Wound Closure'
        elif r < 71: item = 'Phylactery of Faithfulness'
        elif r < 75: item = 'Phylactery of Long Years'
        elif r < 77: item = 'Phylactery of Monstrous Attention'
        elif r < 85: item = 'Pipes of the Sewers'
        elif r == 85: item = 'Portable Hole'
        else: item = 'Quaal\'s Feather Token'
    elif r < 71:
        r = roll(100)
        if r == 1: item = 'Robe of the Archmagi'
        elif r < 9: item = 'Robe of Bending'
        elif r == 9: item = 'Robe of Eyes'
        elif r == 10: item = 'Robe of Powerlessness'
        elif r == 11: item = 'Robe of Scintillating Colors'
        elif r < 20: item = 'Robe of Useful Items'
        elif r < 26: item = 'Robe of Climbing'
        elif r < 28: item = 'Robe of Constriction'
        elif r < 32: item = 'Robe of Entanglement'
        elif r == 32: item = 'Rug of Smothering'
        elif r == 33: item = 'Rug of Welcome'
        elif r == 34: item = 'Saw of Mighty Cutting'
        elif r == 35: item = 'Scarab of Death'
        elif r < 39: item = 'Scarab of Enraging Enemies'
        elif r < 41: item = 'Scarab of Insanity'
        elif r < 47: item = 'Scarab of Protection'
        elif r == 47: item = 'Spade of Colossal Excavation'
        elif r == 48: item = 'Sphere of Annihilation'
        elif r < 51: item = 'Stone of Controlling Earth Elementals'
        elif r < 53: item = 'Stone of Good Luck'
        elif r < 55: item = 'Stone of Weight'
        elif r < 58: item = 'Talisman of Pure Good'
        elif r == 58: item = 'Talisman of the Sphere'
        elif r < 61: item = 'Talisman of Ultimate Evil'
        elif r < 67: item = 'Talisman of Zagy'
        elif r == 67: item = 'Tome of Clear Thought'
        elif r == 68: item = 'Tome of Leadership and Influence'
        elif r == 69: item = 'Tome of Understanding'
        elif r < 77: item = 'Trident of Fish Command'
        elif r < 79: item = 'Trident of Submission'
        elif r < 84: item = 'Trident of Warning'
        elif r < 86: item = 'Trident of Yearning'
        elif r < 88: item = 'Vacuous Grimoire'
        elif r < 91: item = 'Well of Many Worlds'
        else: item = 'Wings of Flying'
    elif r < 86:
        r = roll(100)
        if r < 5: item = 'Amulet Versus Undead'
        elif r == 5: item = 'Anything Item'
        elif r < 8: item = 'Beads of Force'
        elif r < 15: item = 'Boccob\'s Blessed Book'
        elif r < 17: item = 'Boots of the North'
        elif r < 20: item = 'Boots of Varied Tracks'
        elif r == 20: item = 'Winged Boots'
        elif r < 25: item = 'Bracers of Archery'
        elif r < 27: item = 'Bracers of Brachiation'
        elif r < 29: item = 'Chime of Interruption'
        elif r < 31: item = 'Cloak of Arachnidia'
        elif r < 35: item = 'Cloak of the Bat'
        elif r < 37: item = 'Cyclocone'
        elif r < 41: item = 'Dart of the Hornets\' Nest'
        elif r < 43: item = 'Deck of Illusions'
        elif r < 45: item = 'Dicerion of Light & Darkness'
        elif r < 48: item = 'Dust of Dryness'
        elif r < 51: item = 'Dust of Illusion'
        elif r < 55: item = 'Dust of Tracelessness'
        elif r < 57: item = 'Egg of Desire'
        elif r < 61: item = 'Egg of Reason'
        elif r < 63: item = 'Egg of Shattering'
        elif r < 66: item = 'Gem of Insight'
        elif r < 69: item = 'Girdle of Dwarvenkind'
        elif r < 77: item = 'Girdle of Many Pouches'
        elif r < 80: item = 'Gloves of Missile Snaring'
        elif r < 84: item = 'Gloves of Thievery'
        elif r < 89: item = 'Hat of Difference'
        elif r < 96: item = 'Hat of Disguise'
        else: item = 'Hat of Stupidity'
    else:
        r = roll(100)
        if r < 6: item = 'Heward\'s Handy Haversack'
        elif r < 11: item = 'Horn of Fog'
        elif r < 13: item = 'Horn of Goodness (Evil)'
        elif r < 15: item = 'Iron Bands of Bilarro'
        elif r < 19: item = 'Lens of Detection'
        elif r < 22: item = 'Lens of Ultravision'
        elif r < 24: item = 'Mantle of Clestian'
        elif r < 28: item = 'Murlyn\'s Spoon'
        elif r < 30: item = 'Pearl of the Sirines'
        elif r < 32: item = 'Philosopher\'s Stone'
        elif r < 38: item = 'Pouch of Accessibility'
        elif r == 38: item = 'Prison of Zagyg'
        elif r < 41: item = 'Quiver of Ehlonna'
        elif r < 43: item = 'Robe of Stars'
        elif r < 49: item = 'Robe of Vermin'
        elif r < 51: item = 'Scarab Versus Golems'
        elif r < 55: item = 'Shadow Lanthorn'
        elif r < 58: item = 'Sheet of Smallness'
        elif r < 60: item = 'Shoes of Fharlanghn'
        elif r < 65: item = 'Slippers of Kicking'
        elif r < 71: item = 'Slippers of Spider Climbing'
        elif r < 73: item = 'Sovereign Glue'
        elif r < 78: item = 'Spoon of Stirring'
        elif r < 82: item = 'Stone Horse'
        elif r < 85: item = 'Ultimate Solution'
        elif r < 89: item = 'Wind Fan'
        elif r < 93: item = 'Zagyg\'s Flowing Flagon'
        else: item = 'Zagyg\'s Spell Component Case'
    
    return item
    
def generateArmorShield():
    item = ''
    
    if roll(100) < 51:
        r = roll(100)
        if r < 6: item = 'Chain Mail +1'
        elif r < 10: item = 'Chain Mail +2'
        elif r < 12: item = 'Chain Mail +3'
        elif r < 20: item = 'Leather Armor +1'
        elif r < 27: item = 'Plate Mail +1'
        elif r < 33: item = 'Plate Mail +2'
        elif r < 36: item = 'Plate Mail +3'
        elif r < 38: item = 'Plate Mail +4'
        elif r == 38: item = 'Plate Mail +5'
        elif r == 39: item = 'Plate Mail of Etherealness'
        elif r < 45: item = 'Plate Mail of Vulnerability'
        elif r < 51: item = 'Ring Mail +1'
        elif r < 56: item = 'Scale Mail +1'
        elif r < 60: item = 'Scale Mail +2'
        elif r < 64: item = 'Splint Mail +1'
        elif r < 67: item = 'Splint Mail +2'
        elif r < 69: item = 'Splint Mail +3'
        elif r == 69: item = 'Splint Mail +4'
        elif r < 76: item = 'Studded Leather +1'
        elif r < 85: item = 'Shield +1'
        elif r < 90: item = 'Shield +2'
        elif r < 94: item = 'Shield +3'
        elif r < 96: item = 'Shield +4'
        elif r == 96: item = 'Shield +5'
        elif r == 97: item = 'Large Shield +1, +4 vs missiles'
        else: item = 'Shield -1, missile attractor'
    else:
        r = roll(100)
        if r == 1: item = 'Anything Armor'
        elif r < 8: item = 'Bronze Plate Mail +1'
        elif r < 12: item = 'Bronze Plate Mail +2'
        elif r < 18: item = 'Buckler +1'
        elif r < 22: item = 'Buckler +2'
        elif r < 24: item = 'Buckler +3'
        elif r < 26: item = 'Chain Mail +4'
        elif r < 32: item = 'Elfin Chain Mail +1'
        elif r < 36: item = 'Elfin Chain Mail +2'
        elif r < 39: item = 'Elfin Chain Mail +3'
        elif r < 41: item = 'Elfin Chain Mail +4'
        elif r == 41: item = 'Elfin Chain Mail +5'
        elif r < 51: item = 'Leather Armor +2'
        elif r < 56: item = 'Leather Armor +3'
        elif r < 63: item = 'Field Plate Armor +1'
        elif r < 69: item = 'Field Plate Armor +2'
        elif r < 72: item = 'Field Plate Armor +3'
        elif r < 74: item = 'Field Plate Armor +4'
        elif r == 74: item = 'Field Plate Armor +5'
        elif r < 81: item = 'Full Plate Armor +1'
        elif r < 85: item = 'Full Plate Armor +2'
        elif r < 88: item = 'Full Plate Armor +3'
        elif r < 90: item = 'Full Plate Armor +4'
        elif r < 94: item = 'Ring Mail +2'
        elif r < 96: item = 'Scale Mail +3'
        else: item = 'Studded Leather +2'
    
    if 'Elfin' in item:
        r = roll(100)
        if r < 6:
            item = 'Gnome-Sized ' + item
        elif r < 17:
            item = 'Dwarf-Sized ' + item
        elif r < 38:
            item = 'Human-Sized ' + item
    elif (('Shield' not in item) and 
        ('Buckler' not in item)):
        r = roll(100)
        if r < 6:
            item = 'Gnome-Sized ' + item
        elif r < 17:
            item = 'Dwarf-Sized ' + item
        elif r < 38:
            item = 'Elf-Sized ' + item
        
    return item