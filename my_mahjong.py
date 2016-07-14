import tkinter as tk
from tkinter import *
from tkinter.font import Font, nametofont

class Application(Frame):

    def __init__(self, master=None):
        root = Tk()
        root.tk.call('tk', 'scaling', 20.0)
        Frame.__init__(self, master)
        self.pack
        self.grid()
        myfont = nametofont('TkDefaultFont')
        myfont.configure(size=36)
        print(dir(myfont))
        self.create_board()

    def create_board(self):
        self.a_label = Label(self, text = "what")
        self.a_label.grid(row = 0, column = 1)

app = Application()

app.mainloop()
