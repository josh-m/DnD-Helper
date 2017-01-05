from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<ColorLabel>:
  bcolor: 1, 1, 1, 1
  size_hint_y: None
  text_size: self.width, None
  height: self.texture_size[1]
  font_size: "14sp"
  
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")

class ColorLabel(Label):
  bcolor = ListProperty([1,1,1,1])

Factory.register('KivyB', module='ColorLabel')