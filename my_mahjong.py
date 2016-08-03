#import tkinter as tk
from tkinter import *
from tkinter.font import Font, nametofont
from mahjmath import *


class Menubar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        gamemenu = Menu(self)
        self.add_cascade(label="Game", menu=gamemenu)
        gamemenu.add_command(label="Play Game", command=self.playGame)
        gamemenu.add_command(label="Game Statistics", command=self.openStatistics)
        gamemenu.add_separator()
        gamemenu.add_command(label="Exit", command=self.quit)

        helpmenu = Menu(self)
        self.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.about)

    def quit(self):
       sys.exit(0)


    def playGame(): pass

    def about(self):
        print("This is a simple mahjong game that keeps track of board numbers.")

    def openStatistics(): pass


class Application(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack
        self.grid()
        #screen_height = root.winfo_screenheight()
        self.fixfonts()

        # myfont = nametofont('TkDefaultFont')
        #myfont.configure(size=36)
        #print(screen_height)
        self.create_board(1)
        menubar = Menubar(parent)
        parent.config(menu=menubar)
                #creeate menu




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



root = Tk()
app = Application(parent=root)

app.mainloop()
root.destroy()
