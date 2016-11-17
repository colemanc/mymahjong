from tkinter import *
from tkinter.font import Font, nametofont
#from PIL import Image, ImageTk
from mahjong_view import *
import mahjong_controller
from math import floor
# class Menubar(Menu):
#     def __init__(self, parent):
#         Menu.__init__(self, parent)
#
#         #self.menu_font = nametofont('TkMenuFont')
#         #self.menu_font.configure(size=30)
#
#         gamemenu = Menu(self)
#         self.add_cascade(label="Game", menu=gamemenu)
#         gamemenu.add_command(label="Play Game", command=controller.playMahjongGame)
#         #gamemenu.add_command(label="Game Statistics", command=self.openStatistics)
#         gamemenu.add_separator()
#         gamemenu.add_command(label="Exit", command=self.quit)
#
#         helpmenu = Menu(self)
#         self.add_cascade(label="Help", menu=helpmenu)
#         helpmenu.add_command(label="About...", command=self.about)
#
#     def quit(self):
#        sys.exit(0)
#
#     def about(self):
#         print("This is a simple mahjong game that keeps track of board numbers.")




class Application(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.fixFonts()
        self.grid()
        parent.title("My Mahjong")
        self.add_main_menu()
        # menubar = Menubar(parent)
        # parent.config(menu=menubar)
        # self.playMahjongGame()
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        raw_image = Image.open("/home/cynthia/project/mymahjong/kyodaiTileSets/real-tiles.jpg")
        width_org, height_org = raw_image.size
        factor = floor(screen_height/height_org)
        print(width_org, height_org, factor)

        background_image = raw_image.resize((width_org*factor, height_org*factor), Image.ANTIALIAS)
        print(background_image.size)
        self.canvas = Canvas(self, width=(screen_width),height=(screen_height))
        self.canvas.image = ImageTk.PhotoImage(background_image)
# Add the image to the canvas, and set the anchor to the top left / north west corner
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')
        self.canvas.grid(row=0, column=0)

    def fixFonts(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        print(screen_height)
        print(screen_width)
        self.default_font = nametofont('TkDefaultFont')
        print(self.default_font.actual())
        self.default_font.configure(size=16)
        print(self.default_font.actual())

        self.menu_font = nametofont('TkMenuFont')
        print(self.menu_font.actual())

        self.menu_font.configure(size=36)
        print(self.menu_font.actual())


    def add_main_menu(self):
        self.main_menu = Menu(self.parent)
        self.add_game_menu()
        self.add_help_menu()

    def add_game_menu(self):
        self.game_menu = Menu(self.main_menu, tearoff=0)
        self.game_menu.add_command(
            label="New Mahjong Game", command=self.playMahjongGame)
        self.main_menu.add_cascade(label="Games", menu=self.game_menu)
        self.parent.config(menu=self.main_menu)

    def add_help_menu(self):
        self.help_menu = Menu(self.main_menu, tearoff=1)
        self.help_menu.add_command(
            label="New Mahjong Game", command=self.playMahjongGame)
        self.help_menu.add_command(label="About...", command=self.about)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)
        self.parent.config(menu=self.main_menu)

    def playMahjongGame(self):
        controller = mahjong_controller.MahjongController()
        self.mahjong = MahjongView(self, controller)
        self.mahjong.create_board(1)
        self.mahjong.grid(row=0,column=0)

    def quit(self):
       sys.exit(0)

    def about(self):
        print("This is a simple mahjong game that keeps track of board numbers.")

root = Tk()
app = Application(parent=root)

app.mainloop()
