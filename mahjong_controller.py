import mahjong_model

class MahjongController():
    def __init__(self):
            self.init_model()
    def init_model(self):
        self.model = mahjong_model.MahjongModel()
