#qpy: kivy
#kivy 1.9.1

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from ui.menu import MenuScreen
from ui.random_encounters import RandomEncounterScreen
from ui.gem import GemScreen
from ui.jewelry import JewelryScreen
from ui.treasure import TreasureScreen
from ui.combat import CombatScreen
from ui.pc_creator import PlayerCharacterCreatorScreen
from ui.text_input import AlphaInput, NumericInput

from kivy.lang import Builder

    
class DmApp(App):

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen())
        self.sm.add_widget(RandomEncounterScreen())
        self.sm.add_widget(GemScreen())
        self.sm.add_widget(JewelryScreen())
        self.sm.add_widget(TreasureScreen())
        self.sm.add_widget(CombatScreen())
        self.sm.add_widget(PlayerCharacterCreatorScreen())
             
        return self.sm

if __name__ == '__main__':
    Builder.load_file('./ui/gem.kv')
    Builder.load_file('./ui/jewelry.kv')
    Builder.load_file('./ui/treasure.kv')
    Builder.load_file('./ui/random_encounter.kv')
    DmApp().run()
    
