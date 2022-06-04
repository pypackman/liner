from raylib import *
import pyray as p
from sqlalchemy import true
class Platform:
    def __init__(self, posx, posy, width, height, color):
        self.rect=p.Rectangle(posx,posy,width,height)
        self.color = color
    
    def Draw(self):
        DrawRectangleRec(self.rect, self.color)
    def Collision(self, player):
        if CheckCollisionRecs(self.rect, player.rec):
            return True
        elif not CheckCollisionRecs(self.rect,player.rec):
            return False
        
