import tkinter as tk
from tkinter import *
from math import floor

from PIL import ImageTk, Image
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

        self.frames = {}
        page_name = StartPage.__name__
        frame = StartPage(parent=self.container, controller=self)
        self.add_frame(frame, page_name)
        self.show_frame("StartPage")

    def add_frame(self, new_frame, page_name):
        self.frames[page_name] = new_frame
        #stack all frames on top of each other
        new_frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        print("in init for startpage")
        self.controller = controller
        self.showImg()

    def showImg(self):
        print("in showImg")
        raw_image = Image.open("/home/cynthia/project/mymahjong/butterfly640.jpg")
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        width_org, height_org = raw_image.size
        factor = floor(screen_height/height_org)
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
