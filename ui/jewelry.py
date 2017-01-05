#kivy 1.9.1

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from colorlabel import ColorLabel

from dnd.treasure import Treasure, jewelryValue

class JewelryScreen(Screen):
    jewelry_data = ObjectProperty(None)
    jewelry_count = ObjectProperty(None)
    jewelry_value = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(JewelryScreen, self).__init__(**kwargs)
            
    def requestRoll(self):
        count = self.jewelry_count.toNumber()

        val = self.jewelry_data.rollJewelry(count)
        self.jewelry_value.text = 'Total Value: {}'.format(val)

class JewelryData(GridLayout):
    def __init__(self, **kwargs):
        super(JewelryData, self).__init__(**kwargs)
        self.treasure = Treasure()
        
    def rollJewelry(self, count):
        #Clear any existing jewelrys
        self.clear_widgets()
        
        self.treasure.addJewelry(count)
        
        #Roll new jewelrys
        for jewelry in self.treasure.jewelry_list:
            l = ColorLabel(
                    text=str(jewelry),
                    size_hint_y=None,
                    bcolor=(0,0,0.8,1))
            self.add_widget(l)
        
        val = jewelryValue(self.treasure.jewelry_list)
        self.treasure.clear()
        
        return str(val)

class JewelryDisplay(ScrollView): 
    def __init__(self, **kwargs):
        super(JewelryDisplay, self).__init__(**kwargs)

