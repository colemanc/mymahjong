import tkinter as tk
from tkinter import *
from tkinter.font import Font, nametofont
from mahjmath import *

class Application(Frame):

    def __init__(self, master=None):
        root = Tk()

        #root.tk.call('tk', 'scaling', 20.0)
        Frame.__init__(self, master)
        self.pack
        self.grid()
        #screen_height = root.winfo_screenheight()
        self.fixfonts()

        # myfont = nametofont('TkDefaultFont')
        #myfont.configure(size=36)
        #print(screen_height)
        self.create_board(1)

        #creeate menu
        menu = Menu(root)
        root.config(menu=menu)
        gamemenu = Menu(menu)
        menu.add_cascade(label="Game", menu=gamemenu)
        gamemenu.add_command(label="Play Game", command=self.playGame)
        gamemenu.add_command(label="Game Statistics", command=self.openStatistics)
        gamemenu.add_separator()
        gamemenu.add_command(label="Exit", command=root.quit)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.about)

    def playGame(): pass

    def about(self):
        print("This is a simple mahjong game that keeps track of board numbers.")

    def openStatistics(): pass

    def fixfonts(self):
        #screen_width = self.winfo_screenwidth()
        #screen_height = self.winfo_screenheight()
        self.default_font = nametofont('TkDefaultFont')
        self.default_font.configure(size=10)

        self.menu_font = nametofont('TkMenuFont')
        self.menu_font.configure(size=10)

    def create_board(self, board_num):
        board_array = getBoardNumbers(board_num)
        self.a_label = Label(self, text = "what")
        self.a_label.grid(row = 0, column = 1)

app = Application()

app.mainloop()
