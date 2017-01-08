#kivy 1.9.1

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner, SpinnerOption

from dnd.player_char import rollScoreSet, rollSocialClass, determineAge, determineAgeBracket



class PlayerCharacterCreatorScreen(Screen):
    score_set1 = ObjectProperty(None)
    score_set2 = ObjectProperty(None)
    score_set3 = ObjectProperty(None)

    social = ObjectProperty(None)

    stat_bonus_data = ObjectProperty(None)

    str_text = ObjectProperty(None)
    int_text = ObjectProperty(None)
    wis_text = ObjectProperty(None)
    dex_text = ObjectProperty(None)
    con_text = ObjectProperty(None)
    chr_text = ObjectProperty(None)
    com_text = ObjectProperty(None)

    #Underscore to avoid builtin conflicts
    str_ = ObjectProperty(None)
    int_ = ObjectProperty(None)
    wis_ = ObjectProperty(None)
    dex_ = ObjectProperty(None)
    con_ = ObjectProperty(None)
    chr_ = ObjectProperty(None)
    com_ = ObjectProperty(None)

    dwarf = ObjectProperty(None)
    elf = ObjectProperty(None)
    gnome = ObjectProperty(None)
    halfling = ObjectProperty(None)
    halforc = ObjectProperty(None)
    halfelf = ObjectProperty(None)

    cleric = ObjectProperty(None)
    druid = ObjectProperty(None)
    fighter = ObjectProperty(None)
    paladin = ObjectProperty(None)
    ranger = ObjectProperty(None)
    mu = ObjectProperty(None)
    illusionist = ObjectProperty(None)
    thief = ObjectProperty(None)
    assassin = ObjectProperty(None)
    monk = ObjectProperty(None)
    cavalier = ObjectProperty(None)
    barbarian = ObjectProperty(None)

    confirm = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(PlayerCharacterCreatorScreen, self).__init__(**kwargs)
        self.abil_spinners = [self.str_, self.int_, self.wis_, 
            self.dex_, self.con_, self.chr_, self.com_]

        self.selected_score_set = None
        self.populateScoreSets()

        self.setSocialClass()

        self.selected_race = None

        self.selected_class = None

    def populateScoreSets(self):
        for score_set_text in [self.score_set1, self.score_set2, self.score_set3]:
            score_set = rollScoreSet()
            score_str = str(score_set[0])
            for score in score_set[1:]:
                score_str += (' ' + str(score))

            score_set_text.text = score_str

    def setSocialClass(self):
        self.social.text = rollSocialClass()   

    def highlightScoreSet(self, button):
        if (self.selected_score_set):
            self.selected_score_set.background_color = (1,1,1,1)
        if button:
            self.selected_score_set = button
            button.background_color = (0,0,1,1)
        else:
            self.selected_score_set = None

    def populateSelectionSpinners(self):
        if not self.selected_score_set:
            return
        
        for spinner in self.abil_spinners:
            spinner.text = ''
            vals = [''] * (len(self.abil_spinners) + 1)
            vals[1:] = self.selected_score_set.text.split()

            spinner.values = vals
        
    def selectScoreSet(self, button):
        self.highlightScoreSet(button)
        self.populateSelectionSpinners()

    def updateSpinners(self, cur_spinner):
        if not self.selected_score_set:
            return

        remaining_scores = self.selected_score_set.text.split()
        
        for spinner in self.abil_spinners:
            if spinner.text in remaining_scores:
                remaining_scores.remove(spinner.text)
        
        for spinner in self.abil_spinners:
            vals = ['']
            vals += remaining_scores
            spinner.values = vals

    def resetSpinners(self):
        print('resetSpinners()')
        for spinner in self.abil_spinners:
            spinner.text = ''
            spinner.values = ()

    def resetRaceAvailability(self):
        dwarf.disabled = True
        gnome.disabled = True
        elf.disabled = True
        halfling.disabled = True
        halforc.disabled = True
        halfelf.disabled = True

    def checkDwarf(self):
        if (self.str_.text 
            and self.con_.text 
            and self.chr_.text
            and int(self.str_.text) > 7 
            and int(self.con_.text) > 10
            and int(self.chr_.text) > 3):
            self.dwarf.disabled = False;
        else:
            self.dwarf.disabled = True

    def checkElf(self):
        if (self.int_.text
            and self.dex_.text
            and self.con_.text
            and self.chr_.text
            and int(self.int_.text) > 7
            and int(self.dex_.text) > 5
            and int(self.con_.text) > 6
            and int(self.chr_.text) > 7):
            self.elf.disabled = False
        else:
            self.elf.disabled = True

    def checkGnome(self):
        if (self.gnome.disabled
            and self.str_.text
            and self.con_.text
            and self.int_.text
            and int(self.str_.text) > 5
            and int(self.con_.text) > 6
            and int(self.int_.text) > 7):
            self.gnome.disabled = False;
        else:
            self.gnome.disabled = True

    def checkHalfling(self):
        if (self.str_.text
            and self.con_.text
            and int(self.str_.text) > 6
            and int(self.con_.text) > 9):
            self.halfling.disabled = False
        else:
            self.halfling.disabled = True

    def checkHalfElf(self):
        if (self.int_.text
            and self.dex_.text
            and self.con_.text
            and int(self.int_.text) > 3
            and int(self.dex_.text) > 5
            and int(self.con_.text) > 5):
            self.halfelf.disabled = False
        else:
            self.halfelf.disabled = True

    def checkHalfOrc(self):
        if (self.str_.text
            and self.chr_.text
            and int(self.str_.text) > 4
            and int(self.chr_.text) > 4):
            self.halforc.disabled = False
        else:
            self.halforc.disabled = True

    def selectRace(self, race_button):
        self.highlightRace(race_button)
        
        if not race_button:
            self.selected_race = None
        else:
            self.updateRacialAttributes(race_button)
            self.checkClassesAffectedByRace()
            self.checkCompleteCharacter()
        

            
    def checkClassesAffectedByRace(self):
        #every class except cleric
        self.checkDruid()
        self.checkFighter()
        self.checkPaladin()
        self.checkRanger()
        self.checkMagicUser()
        self.checkIllusionist()
        self.checkThief()
        self.checkAssassin()
        self.checkMonk()
        self.checkCavalier()
        self.checkBarbarian()

    def highlightRace(self, button):
        if (self.selected_race):
            self.selected_race.background_color = (1,1,1,1)
        if button:
            self.selected_race = button
            button.background_color = (0,0,1,1)

    def updateRacialAttributes(self, race_button):
        self.str_text.text = self.str_.text
        self.str_text.color = (1,1,1,1)       
        self.con_text.text = self.con_.text
        self.con_text.color = (1,1,1,1) 
        self.dex_text.text = self.dex_.text
        self.dex_text.color = (1,1,1,1) 
        self.chr_text.text = self.chr_.text
        self.chr_text.color = (1,1,1,1)
        
        if race_button.text == 'Dwarf':
            if self.con_.text:
                score = int(self.con_.text)
                score += 1
                self.con_text.color = (0,1,0,1)
                self.con_text.text = str(score)
            if self.chr_text:
                score = int(self.chr_.text)
                score -= 1
                self.chr_text.color = (1,0,0,1)
                self.chr_text.text = str(score)
                print(self.chr_text.text)

        elif race_button.text == 'Elf':
            if self.dex_.text:
                score = int(self.dex_.text)
                score += 1
                self.dex_text.color = (0,1,0,1)
                self.dex_text.text = str(score)
            if self.con_.text:
                score = int(self.con_.text)
                score -= 1
                self.con_text.color = (1,0,0,1)
                self.con_text.text = str(score)

        elif race_button.text == 'Half-Orc':
            if self.str_.text:
                score = int(self.str_.text)
                score += 1
                self.str_text.color = (0,1,0,1)
                self.str_text.text = str(score)
            if self.con_.text:
                score = int(self.con_.text)
                score += 1
                self.con_text.color = (0,1,0,1)
                self.con_text.text = str(score) 
            if self.chr_.text:
                score = int(self.chr_.text)
                score -= 2
                self.chr_text.color = (1,0,0,1)
                self.chr_text.text = str(score)

        elif race_button.text == 'Halfling':
            if self.str_.text:            
                score = int(self.str_.text)
                score -= 1
                self.str_text.color = (1,0,0,1)
                self.str_text.text = str(score)
            if self.dex_.text:
                score = int(self.dex_.text)
                score += 1
                self.dex_text.color = (0,1,0,1)
                self.dex_text.text = str(score)          
            

    def resetClassAvailability(self):
        self.cleric.disabled = True
        self.druid.disabled = True
        self.fighter.disabled = True
        self.ranger.disabled = True
        self.paladin.disabled = True
        self.mu.disabled = True
        self.illusionist.disabled = True
        self.thief.disabled = True
        self.assassin.disabled = True
        self.monk.disabled = True
        self.cavalier.disabled = True
        self.barbarian.disabled = True

    def checkCleric(self):
        if (self.wis_text.text
            and int(self.wis_text.text) > 8):
            self.cleric.disabled =  False
        else:
            self.cleric.disabled = True

    def checkDruid(self):
        if (self.wis_text.text
            and self.chr_text.text
            and int(self.wis_text.text) > 11
            and int(self.chr_text.text) > 14):
            print(self.chr_text.text)
            self.druid.disabled = False
        else:
            self.druid.disabled = True

    def checkFighter(self):
        if (self.str_text.text
            and self.con_text.text
            and int(self.str_text.text) > 8
            and int(self.con_text.text) > 6):
            self.fighter.disabled = False
        else:
            self.fighter.disabled = True
    
    def checkPaladin(self):
        if (self.str_text.text
            and self.dex_text.text
            and self.con_text.text
            and self.int_text.text
            and self.wis_text.text
            and self.chr_text.text
            and int(self.str_text.text) > 14
            and int(self.dex_text.text) > 14
            and int(self.con_text.text) > 14
            and int(self.int_text.text) > 9
            and int(self.wis_text.text) > 12
            and int(self.chr_text.text) > 16):
            self.paladin.disabled = False
        else:
            self.paladin.disabled = True

    def checkRanger(self):
        if (self.str_text.text
            and self.int_text.text
            and self.wis_text.text
            and self.con_text.text
            and int(self.str_text.text) > 12
            and int(self.int_text.text) > 12
            and int(self.con_text.text) > 13
            and int(self.wis_text.text) > 13):
            self.ranger.disabled = False
        else:
            self.ranger.disabled = True

    def checkMagicUser(self):
        if (self.int_text.text
            and self.dex_text.text
            and int(self.int_text.text) > 8
            and int(self.dex_text.text) > 5):
            self.mu.disabled = False
        else:
            self.mu.disabled = True

    def checkIllusionist(self):
        if (self.int_text.text
            and self.dex_text.text
            and int(self.int_text.text) > 14
            and int(self.dex_text.text) > 15):
            self.illusionist.disabled = False
        else:
            self.illusionist.disabled = True

    def checkThief(self):
        if (self.dex_text.text
            and int(self.dex_text.text) > 8):
            self.thief.disabled = False
        else:
            self.thief.disabled = True

    def checkAssassin(self):
        if (self.str_text.text
            and self.int_text.text
            and self.dex_text.text
            and int(self.str_text.text) > 11
            and int(self.int_text.text) > 10
            and int(self.dex_text.text) > 11):
            self.assassin.disabled = False
        else:
            self.assassin.disabled = True

    def checkMonk(self):
        if (self.str_text.text
            and self.wis_text.text
            and self.dex_text.text
            and self.con_text.text
            and int(self.str_text.text) > 14
            and int(self.wis_text.text) > 14
            and int(self.dex_text.text) > 14
            and int(self.con_text.text) > 10):
            self.monk.disabled = False
        else:
            self.monk.disabled = True

    def checkCavalier(self):
        if (self.str_text.text
            and self.dex_text.text
            and self.con_text.text
            and self.int_text.text
            and self.wis_text.text
            and int(self.str_text.text) > 14
            and int(self.dex_text.text) > 14
            and int(self.con_text.text) > 14
            and int(self.int_text.text) > 9
            and int(self.wis_text.text) > 9):
            self.cavalier.disabled = False
        else:
            self.cavalier.disabled = True

    def checkBarbarian(self):
        if (self.str_text.text
            and self.dex_text.text
            and self.con_text.text
            and self.wis_text.text
            and int(self.str_text.text) > 14
            and int(self.con_text.text) > 14
            and int(self.dex_text.text) > 13
            and int(self.wis_text.text) < 17):
            self.barbarian.disabled = False
        else:
            self.barbarian.disabled = True

    def selectClass(self, class_button):
        self.highlightClass(class_button)
        
        if not class_button:
            self.selected_class = None
        else:
            self.checkCompleteCharacter()

            

    def highlightClass(self, button):
        if (self.selected_class):
            self.selected_class.background_color = (1,1,1,1)
        if button:
            self.selected_class = button
            button.background_color = (0,0,1,1)

    def setAge(self):
        age = determineAge(self.selected_race.text, self.selected_class.text)
        print('Age: ' + str(age))
        print('Age Bracket: ' + determineAgeBracket(self.selected_race.text, age))

    def confirmCharacter(self):
        self.setAge()

    def checkCompleteAttributes(self):
        for spinner in self.abil_spinners:
            if not spinner.text:
                return False
        return True

    def checkCompleteCharacter(self):
        if (self.selected_score_set
            and self.selected_race and self.selected_class
            and self.checkCompleteAttributes()):
            self.confirm.disabled = False
        else:
            self.confirm.disabled = True

class StatBonusData(BoxLayout):
    def __init__(self, **kwargs):
        super(StatBonusData, self).__init__(**kwargs)         
        

                
                
        
        
    
