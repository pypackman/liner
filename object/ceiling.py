from raylib import *
import pyray as p
from gameio.dataio import DataIO

class Ceiling:
    def __init__(self, x,y,w,h) -> None:
        self.palette = DataIO().retrievePalette()
        self.ceiling = p.Rectangle(x,y,w,h)
    def Draw(self):
        DrawRectangleRec(self.ceiling, self.palette['brickred'])
    def Collision(self,player):
        if CheckCollisionRecs(self.ceiling,player.rec):
            return True
        else:
            return False