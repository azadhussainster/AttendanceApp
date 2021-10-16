from kivymd.app import MDApp
from kivy.uix.label import Label

class AttendanceApp(MDApp):
    def build(self):
        return Label(text ="Hello World !")

AttendanceApp().run()