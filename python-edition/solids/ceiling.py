from raylib import *
import pyray as p
from gameio.dataio import DataIO

class Ceiling:
    def __init__(self, x,y,w,h) -> None:
        self.palette = DataIO().retrievePalette()
        self.ceiling = p.Rectangle(x,y,w,h)
    def Draw(self):
        DrawRectangleRec(self.ceiling, self.palette['brickred'])
    def IsPlayerUnder(self,player):
        if player.rec.x < self.ceiling.x + self.ceiling.width and player.rec.x + player.rec.width > self.ceiling.x and player.rec.y > self.ceiling.y:
            return True #player is under ceiling
        else:
            return False