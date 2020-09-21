import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import *


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
           # Color(0.1, 0.4, 0.5, 0.8, mode='rgba')
           # Line(points=(20, 30, 600, 100, 400, 500))
            Color(0.4, 0.5, 0.7, 1, mode='rgba')
            self.rect = Rectangle(pos=(300,300), size=(60,60))


    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse down", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse move", touch)



class MyApp(App):
    def build(self):
        return Touch()
        
        
if __name__ == "__main__":
    MyApp().run()