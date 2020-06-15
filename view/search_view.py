import kivy
from search.search import search
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
kivy.require("1.11.1")

class MainPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Search:"))

        self.search_term = TextInput(multiline=False)
        self.add_widget(self.search_term)

        self.search = Button(text="Search")
        self.search.bind(on_press=self.search_button)
        self.add_widget(Label(text=""))
        self.add_widget(self.search)

    def search_button(self, instance):
        search_term = self.search_term.text

        search(search_term)



class AppWindow(App):
    def build(self):
        return MainPage()
