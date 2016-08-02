#random number
import random

def getBoardNumbers(board_num):
    random.seed(board_num)
    x=[i for i in range(0, 144)]
    random.shuffle(x)
    print(x)
    return x
