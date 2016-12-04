import tkinter as tk
from tkinter import *
import mahjong_controller
from guibuilder import ResizableCanvas
from PIL import ImageTk, Image

class MahjongView(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.pack(fill=BOTH, expand=YES)
        self.update_idletasks()
        self.create_board(1)


    def create_board(self, board_num):

        #board_array = getBoardNumbers(board_num)

        frame_width = self.parent.winfo_width()
        frame_height = self.parent.winfo_height()
       # self.update_idletasks()
        print(frame_height, frame_width)

        image = Image.open("/home/cynthia/project/mymahjong/kyodaiTileSets/real-tiles.jpg")
        mycanvas = ResizableCanvas(self, width=(frame_width),height=(frame_height), bg="blue", highlightthickness=0)
        #mycanvas.pack(fill=BOTH, expand=YES)
        mycanvas.grid(row=0, column=0, sticky='nesw')
        mycanvas.columnconfigure(0, weight=1)
        mycanvas.rowconfigure(0, weight=1)

        # fill the canvas
        self.tile = {}
        self.tilesize = tilesize = 32
        xsize, ysize = image.size
        for x in range(0, round(xsize / 10), tilesize):
            for y in range(0, ysize, tilesize):
                box = x, y, min(xsize, x + tilesize), min(ysize, y + tilesize)
                tile = ImageTk.PhotoImage(image.crop(box))
                mycanvas.create_image(x * 2, y * 6, image=tile, anchor=NW)
                self.tile[(x, y)] = box, tile

        self.image = image

        # # labels can be text or images
        # img = Label(self, image=render)
        # img.image = render
        # img.place(x=400, y=500)
                #self.a_label = Label(self, text = "Game Board " + str(board_num))
    #elf.a_label.grid(row = 0, column = 0)

        #width_org, height_org = raw_image.size
        #factor = floor(screen_height/height_org)
        #print(width_org, height_org, factor)

        #background_image = raw_image.resize((width_org*factor, height_org*factor), Image.ANTIALIAS)
        #print(background_image.size)
        #mycanvas = Canvas(self, width=(screen_width),height=(screen_height), bg="blue", highlightthickness=0)
        #mycanvas = Canvas(self, width=(screen_width),height=(screen_height), bg="blue", highlightthickness=0)
        #mycanvas.pack(fill=BOTH, expand=YES)
        # raw_image = Image.open("/home/cynthia/project/mymahjong/kyodaiTileSets/real-tiles.jpg")
        # tiles_image = ImageTk.PhotoImage(raw_image)
        # widget = Label(self, image=tiles_image)
        # #widget.pack(side = "bottom", fill = "both", expand = "yes")
        # widget.place(x=0, y=0)
        #             #    crop_rectangle = (50, 50, 200, 200)
    #    cropped_im = tiles_image.crop(crop_rectangle)
    #    print(cropped_im.size)
        #background = self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')
        #mycanvas.create_window(400, 400, window=widget)


        #self.canvas.create_rectangle(0,0,150,150, fill="blue")

    def getBoardNumbers(board_num):
        pass

####################################################################
#these only are used if you want to just run this game straight up
####################################################################

def main():
    root = Tk()
    root.title("Mahjong")
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    root.geometry("%dx%d+%d+%d" % (screen_width * .8, screen_height * .8, screen_width * .05, screen_height * .05))
    MahjongView(root, mahjong_controller.MahjongController())
    root.mainloop()


def init_new_game():
    game_controller = mahjong_controller.MahjongController()
    main(game_controller)

if __name__ == "__main__":
    #init_new_game()
    main()
