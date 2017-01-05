#kivy 1.9.1

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import sp
from colorlabel import ColorLabel

from dnd.treasure import Treasure, gemsValue, jewelryValue
from dnd.loot import generateLoot

class TreasureScreen(Screen):
    treasure_data = ObjectProperty(None)
    treasure_type = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(TreasureScreen, self).__init__(**kwargs)
    
    def requestRoll(self):
        if len(self.treasure_type.text):
            self.treasure_data.rollTreasure(self.treasure_type.text)

class TreasureData(GridLayout):
    def __init__(self, **kwargs):
        super(TreasureData, self).__init__(**kwargs)
        self.treasure = Treasure()
    def rollTreasure(self, treasure_str):
        self.clear_widgets()
        self.treasure.clear()
        
        for char in treasure_str:
            self.treasure.addTreasure(
                generateLoot(char))
        
        if self.treasure.wealth:
            l = ColorLabel(
                text = str(self.treasure.wealth),
                font_size=sp(20),
                bcolor=(1.00,0.7,0,1))
            self.add_widget(l)
        
        #display total values of gems and jewelry
        if len(self.treasure.gem_list):
            val = gemsValue(self.treasure.gem_list)
            l = ColorLabel(
                text = str('{} gems with total value {}'.format(
                    len(self.treasure.gem_list), val)),
                font_size=sp(20),
                bcolor=(0,0,1,1))
            self.add_widget(l)
        
        if len(self.treasure.jewelry_list):
            val = jewelryValue(self.treasure.jewelry_list)
            l = ColorLabel(
                text = str('{} jewelry with total value {}'.format(
                    len(self.treasure.jewelry_list), val)),
                font_size=sp(20),
                bcolor=(0.8,0,1.0,1))
            self.add_widget(l)
        
        if len(self.treasure.items):
            for item in self.treasure.items:
                l = ColorLabel(
                    text = str(item),
                    font_size=sp(16),
                    bcolor=(0,0.6,0,1))
                self.add_widget(l)      
            
        if len(self.treasure.maps):
            for map in self.treasure.maps:
                l = ColorLabel(
                    text = str(map),
                    font_size=sp(16),
                    bcolor=(1.0,0,0,1))
                self.add_widget(l)  
                
        print(self.treasure.gem_count)    
        if len(self.treasure.gem_list):
            print(len(self.treasure.gem_list))
            
            for gem in self.treasure.gem_list:
                l = ColorLabel(
                    text = str(gem),
                    bcolor=(0,0,1.0,1))
                self.add_widget(l)

        if len(self.treasure.jewelry_list):
            for jewelry in self.treasure.jewelry_list:
                l = ColorLabel(
                    text = str(jewelry),
                    bcolor=(0.8,0,1.0,1))
                self.add_widget(l)
