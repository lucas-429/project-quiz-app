THEME_COLOR = "#375362"
from tkinter import *

class InterFace:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("quizzler")
        self.backgroun = Canvas(background=THEME_COLOR)
        
        self.window.mainloop()