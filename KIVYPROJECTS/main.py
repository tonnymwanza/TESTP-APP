from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid():

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
    
        self.cols = 2
        # self.lab = Label(text='enter username')
        self.username = TextInput(multiline=False)
        # self.lab2 = (Label(text='your password'))
        self.password = TextInput(password=True, multiline=False)

class Myapp(App):
    
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    Myapp().run()