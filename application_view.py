import tkinter as tk
from tkinter import *
from tkinter.font import Font, nametofont
#from PIL import Image, ImageTk
from mahjong_view import *
import mahjong_controller
from math import floor
from guibuilder import ResizableCanvas
#from ttk import Frame, Style
#from simplelabel import Window
#self.columnconfigure(0, weight=1)

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #for F in (Splash, Mahjong):
        page_name = Mahjong.__name__
        mahjong = MahjongView(container, mahjong_controller.MahjongController())
        self.frames["Mahjong"] = mahjong

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        mahjong.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Mahjong")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


    def fixFonts(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
    #    print(screen_height)
#        print(screen_width)
        self.default_font = nametofont('TkDefaultFont')
#        print(self.default_font.actual())
        self.default_font.configure(size=16)
#        print(self.default_font.actual())

        self.menu_font = nametofont('TkMenuFont')
#        print(self.menu_font.actual())

        self.menu_font.configure(size=36)
#        print(self.menu_font.actual())


    def add_main_menu(self):
        self.main_menu = Menu(self.parent)
        self.add_game_menu()
        self.add_help_menu()

    def add_game_menu(self):
        self.game_menu = Menu(self.main_menu, tearoff=0)
        self.game_menu.add_command(label="Show Img", command=self.runOtherClass)
        self.game_menu.add_command(label="New Mahjong Game", command=self.playMahjongGame)
        self.game_menu.add_command(label="Exit", command=self.quit)
        self.main_menu.add_cascade(label="Games", menu=self.game_menu)
        self.parent.config(menu=self.main_menu)

    def add_help_menu(self):
        self.help_menu = Menu(self.main_menu, tearoff=1)
        self.help_menu.add_command(label="About...", command=self.about)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)
        self.parent.config(menu=self.main_menu)

    def playMahjongGame(self):
        controller = mahjong_controller.MahjongController()
        self.mahjong = MahjongView(self, controller)
        self.mahjong.showImg
        self.mahjong.tkraise()
        self.grid(row=0, column=0, sticky="nsew")

        #self.mahjong.grid(row=0,column=0)

    def quit(self):
       sys.exit(0)

    def about(self):
        print("This is a simple mahjong game that keeps track of board numbers.")

    def runOtherClass(self):
        print("running run other class method")
        # self.other = Window(self)
        # self.other.showImg(self)
        # #self.mahjong.create_board(1)

class Mahjong(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


    # def showImg(self):
    #     load = Image.open("/home/cynthia/project/mymahjong/kyodaiTileSets/real-tiles.jpg")
    #
    #     #load = Image.open("chat.png")
    #     render = ImageTk.PhotoImage(load)
    #
    #     # labels can be text or images
    #     img = Label(self, image=render)
    #     img.image = render
    #     img.place(x=0, y=0)

# root = Tk()
# #root.columnconfigure(0, weight=1)
# #root.rowconfigure(0, weight=1)
# app = Application(parent=root)
# root.geometry("400x300")

# app.mainloop()
if __name__ == "__main__":
    app = Application()
    app.mainloop()
