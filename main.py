#qpy: kivy
#kivy 1.9.1

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from ui.menu import MenuScreen
from ui.random_encounters import RandomEncounterScreen
from ui.gem import GemScreen
from ui.jewelry import JewelryScreen
from ui.treasure import TreasureScreen
from ui.combat import CombatScreen
from ui.text_input import AlphaInput, NumericInput
    
class DmApp(App):

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen())
        self.sm.add_widget(RandomEncounterScreen())
        self.sm.add_widget(GemScreen())
        self.sm.add_widget(JewelryScreen())
        self.sm.add_widget(TreasureScreen())
        self.sm.add_widget(CombatScreen())
             
        return self.sm

if __name__ == '__main__':
    DmApp().run()
    
