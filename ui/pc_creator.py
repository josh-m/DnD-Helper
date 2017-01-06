#kivy 1.9.1

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner, SpinnerOption

from dnd.player_char import rollScoreSet



class PlayerCharacterCreatorScreen(Screen):
    score_set1 = ObjectProperty(None)
    score_set2 = ObjectProperty(None)
    score_set3 = ObjectProperty(None)

    str_select = ObjectProperty(None)
    int_select = ObjectProperty(None)
    wis_select = ObjectProperty(None)
    dex_select = ObjectProperty(None)
    con_select = ObjectProperty(None)
    chr_select = ObjectProperty(None)
    com_select = ObjectProperty(None)

    dwarf = ObjectProperty(None)
    elf = ObjectProperty(None)
    gnome = ObjectProperty(None)
    halfling = ObjectProperty(None)
    halforc = ObjectProperty(None)
    halfelf = ObjectProperty(None)
    


    def __init__(self, **kwargs):
        super(PlayerCharacterCreatorScreen, self).__init__(**kwargs)
        self.abil_spinners = [self.str_select, self.int_select, self.wis_select, 
            self.dex_select, self.con_select, self.chr_select, self.com_select]

        self.selected_score_set = None
        self.populateScoreSets()

    def populateScoreSets(self):
        for score_set_text in [self.score_set1, self.score_set2, self.score_set3]:
            score_set = rollScoreSet()
            score_str = str(score_set[0])
            for score in score_set[1:]:
                score_str += (' ' + str(score))

            score_set_text.text = score_str

    def highlightScoreSet(self, button):
        if (self.selected_score_set):
            self.selected_score_set.background_color = (1,1,1,1)
        if button:
            self.selected_score_set = button
            button.background_color = (0,0,1,1)

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

        remaining_scores = self.selected_score_set.text.split()
        
        for spinner in self.abil_spinners:
            if spinner.text in remaining_scores:
                remaining_scores.remove(spinner.text)
        
        for spinner in self.abil_spinners:
            vals = ['']
            vals += remaining_scores
            spinner.values = vals

    def checkDwarf(self):
        if (self.str_select.text 
            and self.con_select.text 
            and self.chr_select.text
            and int(self.str_select.text) > 7 
            and int(self.con_select.text) > 10
            and int(self.chr_select.text) > 3):
            self.dwarf.disabled = False;
        else:
            self.dwarf.disabled = True

    def checkElf(self):
        if (self.int_select.text
            and self.dex_select.text
            and self.con_select.text
            and self.chr_select.text
            and int(self.int_select.text) > 7
            and int(self.dex_select.text) > 5
            and int(self.con_select.text) > 6
            and int(self.chr_select.text) > 7):
            self.elf.disabled = False
        else:
            self.elf.disabled = True

    def checkGnome(self):
        if (self.gnome.disabled
            and self.str_select.text
            and self.con_select.text
            and self.int_select.text
            and int(self.str_select.text) > 5
            and int(self.con_select.text) > 6
            and int(self.int_select.text) > 7):
            self.gnome.disabled = False;
        else:
            self.gnome.disabled = True

    def checkHalfling(self):
        if (self.str_select.text
            and self.con_select.text
            and int(self.str_select.text) > 6
            and int(self.con_select.text) > 9):
            self.halfling.disabled = False
        else:
            self.halfling.disabled = True

    def checkHalfElf(self):
        if (self.int_select.text
            and self.dex_select.text
            and self.con_select.text
            and int(self.int_select.text) > 3
            and int(self.dex_select.text) > 5
            and int(self.con_select.text) > 5):
            self.halfelf.disabled = False
        else:
            self.halfelf.disabled = True

    def checkHalfOrc(self):
        if (self.str_select.text
            and self.chr_select.text
            and int(self.str_select.text) > 4
            and int(self.chr_select.text) > 4):
            self.halforc.disabled = False
        else:
            self.halforc.disabled = True

                
                
        
        
    
