#kivy 1.9.1

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from colorlabel import ColorLabel

from dnd.treasure import Treasure, gemsValue

class GemScreen(Screen):
    gem_data = ObjectProperty(None)
    gem_count = ObjectProperty(None)
    gem_value = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(GemScreen, self).__init__(**kwargs)
            
    def requestRoll(self):
        count = self.gem_count.toNumber()

        val = self.gem_data.rollGems(count)
        self.gem_value.text = 'Total Value: {}'.format(val)
        

class GemData(GridLayout):
    def __init__(self, **kwargs):
        super(GemData, self).__init__(**kwargs)
        self.treasure = Treasure()
        
    def rollGems(self, count):
        #Clear any existing gems
        self.clear_widgets()
        
        self.treasure.addGems(count)
        
        #Roll new gems
        for gem in self.treasure.gem_list:
            l = ColorLabel(
                    text=str(gem),
                    bcolor=(0,0,0.8,1))
            self.add_widget(l)
        
        val = gemsValue(self.treasure.gem_list)
        self.treasure.clear()
        
        return str(val)
      
class GemDisplay(ScrollView): 
    def __init__(self, **kwargs):
        super(GemDisplay, self).__init__(**kwargs)

