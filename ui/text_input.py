#kivy 1.9.1

import re

from kivy.uix.textinput import TextInput

class NumericInput(TextInput):
    pat = re.compile('[^0-9]')
    
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = re.sub(pat, '', substring)
        
        s = s[:3 - len(self.text)]
        
        return super(NumericInput, self).insert_text(s,from_undo=False)
        
    def toNumber(self):
        if self.text:
            return int(self.text)
        else:
            return 1

class AlphaInput(TextInput):
    pat = re.compile('[^A-Za-z]')
    
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = re.sub(pat, '', substring)
        
        return super(AlphaInput, self).insert_text(s,from_undo=False)
