import tkinter as tk
from tkinter import *
from math import floor
from mahjong_view import *
from mahjong_controller import *
from PIL import ImageTk, Image
from tkinter.font import Font, nametofont

TITLE_FONT = ("Helvetica", 18, "bold")
from guibuilder import ResizableCanvas


class Games(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        self.geometry("%dx%d+%d+%d" % (screen_width*.8, screen_height*.8, screen_width*.05, screen_height*.05))

        self.container = tk.Frame(self)
        #tk.geometry("%dx%d+0+0" % (screen_width, screen_height))
        #self.container.width=floor(screen_width*.8)
        #self.container.height=floor(screen_height*.8)

        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.fixFonts()
        #self.grid()
        #self.pack()
        self.title("Games")
        self.add_main_menu()

        self.frames = {}
        page_name = StartPage.__name__
        frame = StartPage(parent=self.container, controller=self)
        self.add_frame(frame, page_name)
        self.show_frame("StartPage")
        # page_name = PageOne.__name__
        # frame = PageOne(parent=self.container, controller=self)
        # self.add_frame(frame, page_name)
        # self.show_frame("PageOne")

    def play_mahjong(self):
        page_name = MahjongView.__name__
        frame = MahjongView(parent=self.container, controller=MahjongController)
        self.add_frame(frame, page_name)
        self.show_frame("MahjongView")

    def add_frame(self, new_frame, page_name):
        self.frames[page_name] = new_frame
        #stack all frames on top of each other
        new_frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
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
        self.main_menu = Menu(self)
        self.add_game_menu()
        self.add_help_menu()

    def add_game_menu(self):
        self.game_menu = Menu(self.main_menu, tearoff=0)
        self.game_menu.add_command(label="New Mahjong Game", command=self.play_mahjong)
        self.game_menu.add_command(label="Exit", command=self.quit)
        self.main_menu.add_cascade(label="Games", menu=self.game_menu)
        self.config(menu=self.main_menu)

    def add_help_menu(self):
        self.help_menu = Menu(self.main_menu, tearoff=1)
        self.help_menu.add_command(label="About...", command=self.about)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)
        self.config(menu=self.main_menu)

    def quit(self):
       sys.exit(0)

    def about(self):
        print("This is a simple mahjong game that keeps track of board numbers.")




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        print("in init for startpage")
        self.controller = controller
        self.showImg()

    def showImg(self):

        raw_image = Image.open("/home/cynthia/project/mymahjong/butterfly640.jpg")
        width_org, height_org = raw_image.size

        #factor = floor(screen_height/height_org)
        factor = 1
        #print(screen_width, screen_height)
        print(width_org, height_org, factor)

        image = raw_image.resize((width_org*factor, height_org*factor), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(image)
        #render.zoom(scale_w, scale_h)
        # labels can be text or images
        label_img = Label(self, image=photoImg)
        label_img.image = photoImg
        label_img.place(x=0, y=0)



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = Games()
    app.mainloop()
