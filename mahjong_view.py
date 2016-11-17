from tkinter import *

import mahjong_controller

from PIL import ImageTk, Image

class MahjongView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        #parent.title("My Mahjong")
        #self.fixFonts()
        self.grid()
        #parent.title("Mahjong")
        #self.create_board(1)


    def create_board(self, board_num):

        #board_array = getBoardNumbers(board_num)
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()

        #print(screen_height)
        #print(screen_width)
        #self_class = self.__class__
        #print(self_class.__bases__)
        self.a_label = Label(self, text = "Game Board " + str(board_num))
        self.a_label.grid(row = 0, column = 0)
        #tiles_image = Image(file="../kyodaiTileSets/real-tiles.jpg", imgtype="jpg")
        tiles_image = Image.open("/home/cynthia/project/mymahjong/kyodaiTileSets/real-tiles.jpg")
        print(tiles_image.format, tiles_image.size, tiles_image.mode)
        #self.image_label = Label(self, image=tiles_image)
        #self.image_label.grid(row=1,column=0)

        #im = Image.open('test_image.jpg')
# Put the image into a canvas compatible class, and stick in an
# arbitrary variable to the garbage collector doesn't destroy it
        self.canvas = Canvas(self, width=(screen_width*.8),height=(screen_height*.8))

        self.canvas.image = ImageTk.PhotoImage(tiles_image)
# Add the image to the canvas, and set the anchor to the top left / north west corner
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')



        self.canvas.grid(row=0, column=0)
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
