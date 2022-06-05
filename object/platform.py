from object.ceiling import Ceiling
from gameio.dataio import DataIO
from raylib import *
import pyray as p
class Platform:
    def __init__(self, posx, posy, width, height, color):
        self.palette = DataIO().retrievePalette()
        self.rect=p.Rectangle(posx,posy,width,height)
        self.ceilingHitbox = Ceiling(posx,posy+height/2,width,height/2)
        self.color = color
    
    def Draw(self):
        self.ceilingHitbox.Draw()
        DrawRectangleRec(self.rect, self.color)
    def Collision(self, player):
        if CheckCollisionRecs(self.rect, player.rec):
            return True
        elif not CheckCollisionRecs(self.rect,player.rec):
            return False
    def CeilingCollision(self,player):
        if self.ceilingHitbox.Collision(player):
            return True
        else:
            return False

    
        
