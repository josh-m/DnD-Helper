#kivy 1.9.1

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import sp
from colorlabel import ColorLabel

from dnd.random_encounters import rollMultipleDays
        
class RandomEncounterScreen(Screen):
    day_count = ObjectProperty(None)
    encounter_data = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(RandomEncounterScreen, self).__init__(**kwargs)
        self.climate = 'Temperate'
        self.population = 'Wilderness'
        self.terrain = 'Plains'
        
        self.pop_density = 'Wilderness'

        
    def updatePopulation(self, pop):
        if pop == 'Wilderness':
            self.pop_density = 'Wilderness'
            self.population = 'Wilderness'
        elif pop == 'Sparsely Civilized':
            self.pop_density = 'Sparse'
            self.population = 'Civilized'
        elif pop == 'Densely Civilized':
            self.pop_density = 'Dense'
            self.population = 'Civilized'
        
    
    def rollEncounters(self):
        region_str = constructRegionString(
            self.climate,self.population,self.terrain)
        days = self.day_count.toNumber()    
        print(region_str)
        print(days)
        self.encounter_data.rollEncounters(
            days, region_str, self.pop_density)

def constructRegionString(clime,pop,terr):
    ret = '{} '.format(clime)
    ret += '{} '.format(pop)
    ret += terr
    
    return ret
        
class EncounterData(GridLayout):
    def __init__(self, **kwargs):
        super(EncounterData, self).__init__(**kwargs)
        self.days = []
        
    def rollEncounters(self, day_count, region, density):
        e = rollMultipleDays(day_count, region, density)
        
        self.clear_widgets()
        
        if not len(e):
            l = ColorLabel(
                text = 'No encounters',
                size_hint_y=None,
                height=sp(20),
                font_size=sp(16),
                bcolor=(0,0,0.8,1))
            self.add_widget(l)
            Animation(duration=0.2, font_size=72).start(l)
        else:   
            for day in e:
                for encounter in day[1]:
                    enc_str = day[0] 
                    enc_str += ', {} - {}'.format(
                        encounter[0], encounter[1])
                    l = ColorLabel(
                        text = enc_str,
                        font_size=sp(20),
                        bcolor=(0,0,0.8,1))
                    self.add_widget(l)
        
class EncounterDisplay(ScrollView):
    def __init__(self, **kwargs):
        super(EncounterDisplay, self).__init__(**kwargs)
