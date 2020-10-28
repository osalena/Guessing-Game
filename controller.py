try:
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk # python 3

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.range=0
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root, self.model)

    def run(self):
        self.root.title("Guessing Game")
        #self.root.mainloop()
        self.view.run()
