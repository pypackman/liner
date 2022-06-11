from game.solids.platforms.platform import Platform

class UnstablePlatform(Platform):
    def __init__(self, posx, posy, width, height, color):
        super().__init__(posx, posy, width, height, color)