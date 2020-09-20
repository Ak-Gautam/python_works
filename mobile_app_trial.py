import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Myspace(GridLayout):
    def __init__(self, **kwargs):
        super(Myspace, self).__init__(**kwargs)

        self.cols=1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        self.inside.add_widget(Label(text="Age: "))
        self.age = TextInput(multiline=False)
        self.inside.add_widget(self.age)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=30)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        age = self.age.text
        print("Name: ", name,"\t", "Age: ", age)
        self.name.text = ""
        self.age.text = ""


class MyApp(App):
    def build(self):
        return Myspace()
        
        
if __name__ == "__main__":
    MyApp().run()