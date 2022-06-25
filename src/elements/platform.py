from raylib import *
from pyray import Rectangle

class Platform:
    def __init__(self, posx: int, posy: int, width: int, height: int, color: list[int]):
        self.platform = Rectangle(posx,posy,width,height)
        self.color = color
    
    def draw(self):
        DrawRectangleRec(self.platform, self.color)

    def collision(self, player) -> bool:
        if CheckCollisionRecs(self.platform, player):
            return True
        else:
            return False