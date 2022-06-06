from solids import ceiling,wall
from gameio.dataio import DataIO
from raylib import *
import pyray as p
class Platform:
    def __init__(self, posx, posy, width, height, color):
        self.palette = DataIO().retrievePalette()
        self.rect=p.Rectangle(posx,posy,width,height)
        self.ceilingHitbox = ceiling.Ceiling(posx,posy+height/2,width,height/2)
        self.wall = wall.Wall(posx,posy+height/2+5,width,height/2-10,self.palette['navy'])
        self.color = color
    
    def Draw(self): 
        self.ceilingHitbox.Draw()
        self.wall.Draw()
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
    def WallCollision(self,player):
        self.wall.Collision(player)
    
        
