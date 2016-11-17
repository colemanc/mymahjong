#random number
import random

class MahjongModel():
    def __init__(self):
            pass
            
    def getBoardNumbers(board_num):
        random.seed(board_num)
        x=[i for i in range(1, 145)]
        random.shuffle(x)
        print(x)
        return x
