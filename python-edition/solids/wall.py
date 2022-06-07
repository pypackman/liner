import pyray as p
from raylib import *
from gameio.dataio import DataIO
class Wall:
    def __init__(self,posx,posy,width,height,color)->None:
        self.palette = DataIO().retrievePalette()
        self.rect = p.Rectangle(posx,posy,width,height)
        self.leftHitbox = p.Rectangle(posx,posy,width/2,height)
        self.rightHitBox = p.Rectangle(posx+width/2,posy,width/2,height)
        self.color = color
    def Draw(self):
        DrawRectangleRec(self.leftHitbox,self.palette['red'])
        DrawRectangleRec(self.rightHitBox,self.palette['brickred'])
        DrawRectangleRec(self.rect,self.color)
    def Collision(self,player):
        if CheckCollisionRecs(self.rightHitBox,player.rec):
            player.rec.x = self.rect.x + self.rect.width
            player.xvelocity = 0
        if CheckCollisionRecs(self.leftHitbox,player.rec):
            player.rec.x = self.rect.x - player.rec.width
            player.xvelocity = 0