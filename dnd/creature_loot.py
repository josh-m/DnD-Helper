
from dnd.loot import generateLoot
from dnd.treasure import Treasure    


def __main__():
    while True:
        creature = input('Enter creature: ')
        print(generateLairLoot(creature))
        
def generateLairLoot(creature, num=1):
    output_str = ''
    
    #check for exact match
    creature_tokens = creature.lower().split()
    
    num_tokens = len(creature_tokens)
    if num_tokens < 1:
        return
        
    #Find initial candidates
    candidates = [c for c in lair_loot
                    if creature_tokens[0] in c[0].lower()] 
    
    #check if each word is within the creature's full name
    for token in creature_tokens[1:]:
        candidates = [c for c in candidates
                        if token in c[0].lower()]
        
    if len(candidates) == 0:
        return 'No loot, or monster does not exist'
    elif len(candidates) > 1:
        #if there is an exact match, drop others
        if creature in [c[0].lower() for c in candidates]:
            found_idx = [c[0].lower() 
                              for c in candidates].index(creature)
            found_creature = candidates[found_idx]
        else:
            output_str += 'Found the following monsters, be more specific:'
            for c in candidates:
                output_str += '\n' + c[0]
            return output_str
    else:
        found_creature = candidates[0]

    t = Treasure()
    t.clear()
    _t = Treasure()
    t_types = found_creature[1]
    length = len(t_types)
    for i in range(length):

        if t_types[i] != '*':
            #print('Adding loot ' +t_types[i]) 
            t.addTreasure(generateLoot(t_types[i]))
        else:
            output_str += 'Special Loot (look up the monster)'
    
    output_str += '\n-------------------\n'
    output_str += found_creature[0] + '\n'
    if t: output_str += str(t)
    else: output_str += 'No loot in lair.'
    output_str += '\n-------------------'
    
    return output_str

#special loot, loot that doesn't conform to standard loot table
special_loot = [

]
    
#treasure on each individual regardless of location
individual_loot = [
    ('Badger','*'),
    ('Giant Badger','*'),
    ('Giant Beaver','*'),
    ('Giant Fire Beetle','*'),
    ('Bugbear','JKLM'),
    ('Bulette','*'),
    ('Centaur','MQ'),
    ('Dwarf','MMMMM'),
    ('Elf','N'),
    ('Ettin','OC'),
    ('Gargoyle','MMMMMMMMMM'),
    ('Cloud Giant','*'),
    ('Fire Giant','*'),
    ('Gnoll','LM'),
    ('Gnome','MMM'),
    ('Goblin','K'),
    ('Halfling','K'),
    ('Hobgoblin','JM'),
    ('Kobold','JO'),
    ('Bandit','M'),
    ('Berserker','K'),
    ('Buccaneer','K'),
    ('Dervish','J,L'),
    ('Ogre','MMMMMMMMMM'),
    ('Orc','L'),
    ('Manta Ray','JJJJJJJJJJKKKKKKKKKKLLLLLLLLLLMMMMMMMMMMNNNNNNNNNNQQQQQX'),
    ('Roper','*'),
    ('Sahuagin','N'),
    ('Drow (Dark Elf)','NNNNNQQ'),
    ('Fire Newt','KM'),
    ('Githyanki','N'),
    ('Grimlock','KLM'),    
    ('Jermlaine','*'),
    ('Kuo-Toa','LMN'),
    ('Mezzodaemon','QQQQQ'),
    ('Nilbog','K'),
    ('Ogrillon','M'),
    ('Svirfneblin (Deep Gnome)','KK'),
    ('Azer','*'),
    ('Crysmal','*'),
    ('Duergar','MQ'),
    ('Grugach (Wild Elf)','NQ'),
    ('Valley Elf','MN'),
    ('Firbolg','MMMMMMMMMMQ'),
    ('Verbeeg','KKKKKLLLLLMMMMM'),
    ('Margoyle','C'),
    ('Muckdweller','Q'),
    ('Sirine','LMNQ')
]

#This loot applies to creatures found in their lair
lair_loot = [
    ('Anhkheg','C'),
    ('Giant Ant','QQQS'),
    ('Carnivorous Ape','C'),
    ('Giant Beaver','C'),
    ('Giant Boring Beetle','CRST'),
    ('Blink Dog','*'),
    ('Bugbear', 'B'),
    ('Carrion Crawler','B'),
    ('Catoblepas','C'),
    ('Centaur','DIT'),
    ('Chimera','F'),
    ('Cockatrice','D'),
    ('Couatl','BI'),
    ('Demogorgon, Prince of Demons','RSTV'),
    ('Orcus, Prince of the Undead','PSTU'),
    ('Succubus','IQ'),
    ('Type I Demon (Vrock)','B'),
    ('Type II Demon (Hezrou)','C'),
    ('Type III Demon (Glabrezu)','D'),
    ('Type IV Demon (Nalfeshnee)','E'),
    ('Type V Demon (Marilith)','G'),
    ('Type VI Demon (Balor)','F'),
    ('Asmodeus, Arch-Devil','IRUV'),
    ('Baalzebul, Arch-Devil','ERV'),
    ('Dispater','QQQQQQQQQQS'),
    ('Geryon, Arch-Devil','HR'),
    ('Greater Horned Devil (Malebranche)','I'),
    ('Greater Ice Devil','QR'),
    ('Pit Fiend (Greater Devil)','JR'),
    ('Displacer Beast','D'),
    ('Doppleganger','E'),
    ('Black Dragon','H'),
    ('Blue Dragon','HS'),
    ('Brass Dragon','H'),
    ('Bronze Dragon','HST'),
    ('Tiamat, Chromatic Dragon','HSTU'),
    ('Copper Dragon','HS'),
    ('Gold Dragon','HRST'),
    ('Bahamut, Platinum Dragon','HIRSTV'),
    ('Red Dragon','HST'),
    ('Silver Dragon','HT'),
    ('White Dragon','EOS'),
    ('Dragonne','BST'),
    ('Dragon Turtle','BRSTV'),
    ('Dwarf','GQQQQQQQQQQQQQQQQQQQQR'),
    ('Dryad','MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMQQQQQQQQQQ'),
    ('Giant Eagle','QC*'),
    ('Weed Eel','OPR'),
    ('Elf','GST'),
    ('Ettin','Y'),
    ('Eye of the Deep','R'),
    ('Gargoyle','C'),
    ('Ghast','BQRST'),
    ('Ghost','ES'),
    ('Ghoul','BT'),
    ('Cloud Giant','EQQQQQ'),
    ('Fire Giant','E'),
    ('Frost Giant','E'),
    ('Hill Giant','D'),
    ('Stone Giant','D'),
    ('Storm Giant','EQQQQQQQQQQS'),
    ('Gnoll','DQQQQQS'),
    ('Gnome','CQQQQQQQQQQQQQQQQQQQQ'),
    ('Goblin','C'),
    ('Gorgon','E'),
    ('Griffon','CS'),
    ('Groaning Spirit (Banshee)','D'),
    ('Halfling','B'),
    ('Harpy','C'),
    ('Hell Hound','C'),
    ('Hippogriff','QQQQQ'),
    ('Hobgoblin','DQ'),
    ('Hydra','B'),
    ('Imp','O'),
    ('Intellect Devourer','D'),
    ('Ixitxachitl','PRSU'),
    ('Jackalwere','C'),
    ('Ki-Rin','IST'),
    ('Kobold','QQQQQ'),
    ('Lamia','D'),
    ('Lammasu','RST'),
    ('Leprechaun','F'),
    ('Leucrotta','D'),
    ('Lich','A'),
    ('Fire Lizard','BQQQQQQQQQQ'),
    ('Minotaur Lizard','JKLMNQC'),
    ('Subterranean Lizard','OPQQQQQ'),
    ('Lizard Man','D'),
    ('Locathah','A'),
    ('Lurker Above','CY'),
    ('Werebear','RTX'),
    ('Wereboar','BS'),
    ('Wererat','C'),
    ('Weretiger','DQQQQQ'),
    ('Werewolf','B'),
    ('Manticore','E'),
    ('Medusa','PQQQQQQQQQQXY'),
    ('Bandit','A'),
    ('Berserker','B'),
    ('Buccaneer','W'),
    ('Dervish','Z'),
    ('Merman','CR'),
    ('Mind Flayer','BSTX'),
    ('Minotaur','C'),
    ('Morkoth','G'),
    ('Mummy','D'),
    ('Guardian Naga','H'),
    ('Spirit Naga','BTX'),
    ('Water Naga','D'),
    ('Nixie','CQ'),
    ('Nymph','QQQQQQQQQQX'),
    ('Giant Octopus','R'),
    ('Ogre','QBS'),
    ('Ogre Mage','GRS'),
    ('Orc','COQQQQQQQQQQS'),
    ('Giant Owl','QQQQQX'),
    ('Owlbear','C'),
    ('Peryton','B'),
    ('Pixie','RSTX'),
    ('Pseudo-Dragon','QQQQQQQQQQ'),
    ('Purple Worm','BQQQQQX'),
    ('Quasit','QQQ'),
    ('Rakshasa','F'),
    ('Giant Sumatran Rat','C'),
    ('Remorhaz','F'),
    ('Roc','C'),
    ('Rust Monster','QQQQQQQQQQ'),
    ('Sahuagin','IOPQQQQQQQQQQXY'),
    ('Salamander','F'),
    ('Satyr','ISX'),
    ('Giant Scorpion','D'),
    ('Sea Hag','CY'),
    ('Sea Lion','B'),
    ('Shadow','F'),
    ('Shambling Mound','BTX'),
    ('Shedu','G'),
    #missing p.88
    ('Spectre','QQQXY'),
    ('Andro-Sphinx','U'),
    ('Crio-Sphinx','F'),
    ('Gyno-Sphinx','RX'),
    ('Hieraco-Sphinx','E'),
    ('Giant Spider','C'),
    ('Huge Spider','JKLMNQ'),
    ('Large Spider','JKLMN'),
    ('Phase Spider','E'),
    ('Giant Water Spider','JKLMNQ'),
    ('Sprite','C'),
    ('Giant Sqiud','A'),
    ('Stirge','D'),
    ('Strangle Weed','JKLMNQC'),
    ('Su-Monster','CY'),
    ('Sylph','QQQQQQQQQQX'),
    ('Titan','EQQQQQQQQQQR'),
    ('Ice Toad','C'),
    ('Trapper','G'),
    ('Treant','QQQQQS'),
    ('Triton','CRSTX'),
    ('Troglodyte','A'),
    ('Troll','D'),
    ('Umber Hulk','G'),
    ('Unicorn','X'),
    ('Vampire','F'),
    ('Giant Wasp','QQQQQQQQQQQQQQQQQQQQ'),
    ('Water Weird','IOPY'),
    ('Whale','*'),
    ('Wight','B'),
    ('Will-O-(The)-Wisp','Z'),
    ('Wind Walker','CR'),
    ('Winter Wolf','I'),
    ('Wraith','E'),
    ('Wyvern','E'),
    ('Xorn','OPQQQQQXY'),
    ('Yeti','D'),
    #Start Fiend Folio
    ('Aarakocra (Bird-Man)','D'),
    ('Achaierai','F'),
    ('Algoid','*'),
    ('Apparition','E'),
    ('Babbler','B'),
    ('Berbalang','D'),
    ('Blindheim','B'),
    ('Blood Hawk','QQ'),
    ('Giant Bloodworm','Q'),
    ('Bonesnapper','C'),
    ('Booka','J'),
    ('Bullywug','*'),
    ('Caterwaul','NRSU'),
    ('Cifal','Q'),
    ('Coffer Corpse','B'),
    ('Crabman','K'),
    ('Crypt Thing','Z'),
    ('Dakon','E'),
    ('Dark Creeper','*'),
    ('Dark Stalker','*'),
    ('Lolth, Demon Queen of Spiders','QQQQQRXXX'),
    ('Greater Styx Devil','QR'),
    ('Dire Corby','QQQQQ'),
    ('Li Lung (Earth Dragon)','H'),
    ('Lung Wang (Sea Dragon)','HH'),
    ('Pan Lung (Coiled Dragon)','*'),
    ('Shen Lung (Spirit Dragon)','H'),
    ("T'ien Lung (Celestial Dragon)",'HH'),
    ('Cryonax, Prince of Evil Cold Creatures','HVX'),
    ('Imix, Prince of Evil Fire Creatures','RU'),
    ('Ogremoch, Prince of Evil Earth Creatures','HUZ'),
    ('Olhydra, Princess of Evil Water Creatures','HSU'),
    ('Yan-C-Bin, Prince of Evil Aerial Creatures','UZ'),
    ('Enveloper','E'),
    ('Fire Newt','F'),
    ('Fire Snake','Q'),
    ('Firetoad','C'),
    ('Flind','A'),
    ('Frost Man','C'),
    ('Galltrit','*'),
    ('Gambado','PR'),
    ('Black Garbug','C'),
    ('Violet Garbug','C'),
    ('Fog Giant','E'),
    ('Mountain Giant','E'),
    ('Gibberling','D'),
    ('Githyanki','AZZ'),
    ('Githzerai','A'),
    ('Grimlock','B'),
    ('Guardian Daemon','*'),
    ('Guardian Familiar','*'),
    ('Hoar Fox','*'),
    ('Hook Horror','P'),
    ('Huecuva','C'),
    ('Ice Lizard','G'),
    ('Iron Cobra','*'),
    ('Jermlaine','CQQQQQST'),
    ('Kamadan','C'),
    ('Kelpie','D'),
    ('Kenku','F'),
    ('Khargra','*'),
    ('Killmoulis','K'),
    ('Kuo-Toa','Z'),
    ('Lamia Noble','D'),
    ('Lava Children','Q'),
    ('Lizard King','E'),
    ('Meazel','B'),
    ('Mezzodaemon','X'),
    ('Mite','C'),
    ('Needleman','G'),
    ('Nilbog','C'),
    ('Norker','E'),
    ('Nycadaemon','QQQQQQQQQQX'),
    ('Ogrillon','BS'),
    ('Osquip','D'),
    ('Pernicon','*'),
    ('Protein Polymorph','D'),
    ('Quaggoth','A'),
    ('Qullan','*'),
    ('Retriever','Z'),
    ('Sandman','*'),
    ('Screaming Devilkin','M'),
    ('Shocker','*'),
    ('Skeleton Warrior','A'),
    ('Skulk','A'),
    ('Blue Slaad','Z'),
    ('Death Slaadi','ZZZZ'),
    ('Green Slaad','CFG'),
    ('Grey Slaadi','*'),
    ('Red Slaad','F'),
    ('Ssendam, Lord of the Insane','AAAAFF'),
    ('Ygorl, Lord of Entropy','PPPPZZ'),
    ('Snyad','J'),
    ('Stunjelly','*'),
    ('Svirfneblin (Deep Gnome)','QQQ'),
    ('Tabaxi (Cat-Man)','*'),
    ('Thoqqua','*'),
    ('Thork','*'),
    ('Tiger Fly','B'),
    ('Giant Troll','C'),
    ('Giant Two-Headed Troll','DQ'),
    ('Ice Troll','*'),
    ('Umpleby','*'),
    ('Black Urchin','*'),
    ('Green Urchin','*'),
    ('Red Urchin','*'),
    ('Silver Urchin','*'),
    ('Yellow Urchin','*'),
    ('Vodyanoi','G'),
    ('Witherstench','B'),
    ('Witherweed','*'),
    ('Xill','C'),
    ('Xvart','K'),
    ('Yellow Musk Creeper','*'),
    #Monster Manual II starts here
    ('Aboleth','F'),
    ('Annis','D'),
    ('Ant Lion','*'),
    ('Aspis Drone','F'),
    ('Atomie','*'),
    ('Banderlog','*'),
    ('Barghest','*'),
    ('Barkburr','*'),
    ('Greater Basilisk','H'),
    ('Mobat','C'),
    ('Fire Bat','I'),
    ('Giant Death Watch Beetle','*'),
    ('Giant Slicer Beetle','*'),
    ('Behir','*'),
    ('Boggle','C'),
    ('Bookworm','*'),
    ('Bowler','*'),
    ('Buckawn','X'),
    ('Cat Lion','STWX'),
    ('Cloaker','C'),
    ('Cyclopskin','C'),
    ('Arcanadaemon (Greater Daemon)','H'),
    ('Charonadaemon (Lesser Daemon)','I'),
    ('Derghodaemon (Lesser Daemon)','*'),
    ('Hydrodaemon (Lesser Daemon)','IY'),
    ('Oinodaemon (Anthraxus)','RW'),
    ('Piscodaemon (Lesser Daemon)','E'),
    ('Ultrodaemon (Greater Daemon)','GR'),
    ('Yagnodaemon (Lesser Daemon)','R'),
    ('Crimson Death','Z'),
    ('Demilich','Z'),
    ('Alu-Demon (Semi-Demon)','STU'),
    ('Babau (Minor Demon)','C'),
    ('Baphomet (Demon Lord)','STWZ'),
    ('Bar-Lgura (Minor Demon)','C'),
    ('Cambion (Semi-Demon','*'),
    ('Chasme (Minor Demon)','B'),
    ('Dretch (Minor Demon)','JKLM'),
    ("Fraz-Urb'luu, Prince of Deception",'OPUZ'),
    ("Graz'zt, Demon Prince",'UZ'),
    ('Kostchtchie, Demon Lord','AIST'),
    ('Nabassu (Major Demon)','*'),
    ('Pazuzu, Prince of the Lower Aerial Kingdoms','STUVWXZ'),
    ('Rutterkin (Minor Demon)','LLLLLLLLLLMMMMMOQ'),
    ('Derro','*'),
    ('Amon, Duke of Hell','GP'),
    ('Bael, Duke of Hell','GP'),
    ('Belial, Arch-Devil','ASTY'),
    ('Glasya, Princess of Hell','IQQQQQS'),
    ('Hutijin, Duke of Hell','G'),
    ('Mammon, Arch-Devil','HR'),
    ('Mephistopheles (Arch-Devil)','RXZ'),
    ('Moloch (Arch-Devil)','IRSTX'),
    ('Titivilus, Duke of Hell','GST'),
    ('Dracolisk','CI'),
    ('Cloud Dragon','RTXZ'),
    ('Faerie Dragon','STU'),
    ('Mist Dragon','XYZ'),
    ('Shadow Dragon','*'),
    ('Drelb','*'),
    ('Duergar','*'),
    ('Eagle','*'),
    ('Eblis','*'),
    ('Valley Elf','GST'),
    ('Elfin Cat','*'),
    ('Small Falcon','*'),
    ('Large Falcon','*'),
    ('Froghemoth','*'),
    ('Galeb Duhr','QQQX'),
    ('Fomorian Giant','DQQQQQQQQQQ'),
    ('Firbolg','EY'),
    ('Verbeeg','B'),
    ('Gibbering Mouther','Q'),
    ('Gorgimera','F'),
    ('Greenhag','MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNQQQQQX'),
    ('Grippli','QQQQI'),
    ('Grig','XY'),
    ('Hybsil','I'),
    ('Mustard Jelly','*'),
    ('Kampfult','*'),
    ('Kech','B'),
    ('Korred','E'),
    ('Kraken','GRS'),
    ('Foxwoman','EQQQQQS'),
    ('Wereshark','*'),
    ('Mandragora','*'),
    ('Mihstu','I'),
    ('Miner','G'),
    ('Mantrap','JJJJJKKKKKLLLLLMMMMMNNNNNQ'),
    ('Margoyle','C'),
    ('Mongrelman','C'),
    ('Moon Dog','N'),
    ('Muckdweller','JKLMN'),
    ('Myconid','SS'),
    ('Nereid','X'),
    ('Aquatic Ogre','A'),
    ('Ophidian','*'),
    ('Opinicus','A'),
    ('Pech','*'),
    ('Large Pedipalp','MQQ'),
    ('Huge Pedipalp','QQQQT'),
    ('Giant Pedipalp','I'),
    ('Phoenix','*'),
    ('Psuedo-Undead','A'),
    ('Pyrolisk','D'),
    ('Quickling','OPQX'),
    ('Quickwood (Spy Tree)','*'),
    ('Vapor Rat','*'),
    ('Ordinary Raven (Crow)','*'),
    ('Huge Raven (Crow)','*'),
    ('Giant Raven (Crow)','*'),
    ('Rock Reptile','*'),
    ('Large Scorpion','D'),
    ('Huge Scorpion','D'),
    ('Selkie','*'),
    ('Sirine','X'),
    ('Large Solifugid','Q'),
    ('Huge Solifugid','QS'),
    ('Giant Solifugid','NNNNQQ'),
    ('Spectator','*'),
    ('Spriggan','A'),
    ('Stone Guardian','*'),
    ('Storoper','MNQQ'),
    ('Swanmay','*'),
    ('Taer','*'),
    ('Tarrasque','*'),
    ('Tasloi','QQQQQ'),
    ('Thri-Kreen (Mantis Warrior)','Q'),
    ('Fresh Water Marine Troll (Scrag)','C'),
    ('Salt Water Marine Troll (Scrag)','D'),
    ('Land Urchin','*'),
    ('Ustilagor','*'),
    ('Vagabond','*'),
    ('Vargouille','*'),
    ('Vegepygmy','OP'),
    ('Verme','*'),
    ('Vilstrak','C'),
    ('Vulchling','JKLN'),
    ('Wemic','B'),
    ('Black Willow','*'),
    ('Wolfwere','*'),
    ('Tunnel Worm','MNQ'),
    ('Xaren','*'),
    ('Yuan Ti','C'),
    ('Zorbo','PQX')
]

if __name__ == '__main__':
    __main__()
  