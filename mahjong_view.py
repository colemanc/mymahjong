from tkinter import *
import mahjong_controller
from guibuilder import ResizableCanvas
from PIL import ImageTk, Image

class MahjongView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.showImg
        #self.fixFonts()
        #self.grid()
        #parent.title("Mahjong")
        #self.create_board(1)

    def showImg(self):
        load = Image.open("/home/cynthia/project/mymahjong/kyodaiTileSets/real-tiles.jpg")

        #load = Image.open("chat.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def create_board(self, board_num):

        #board_array = getBoardNumbers(board_num)
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()

        load = Image.open("/home/cynthia/project/mymahjong/kyodaiTileSets/real-tiles.jpg")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=400, y=500)
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

def main(controller):
    root = Tk()
    root.title("Mahjong")
    MahjongView(root, controller)
    root.mainloop()


def init_new_game():
    game_controller = mahjong_controller.MahjongController()
    main(game_controller)

if __name__ == "__main__":
    init_new_game()
