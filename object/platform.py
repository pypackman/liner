from raylib import *
import pyray as p
class Platform:
    def __init__(self, posx, posy, width, height, color):
        self.rect=p.Rectangle(posx,posy,width,height)
        self.ceilingHitbox = p.Rectangle(posx,posy+5,width,30)
        self.color = color
    
    def Draw(self):
        DrawRectangleRec(self.rect, self.color)
        DrawRectangleRec(self.ceilingHitbox, p.RED)

    def Collision(self, player):
        if CheckCollisionRecs(self.rect, player.rec):
            if player.rec.x < self.rect.x + self.rect.width and player.rec.x > self.rect.x:
                player.floorHeight = self.rect.y - player.rec.height
        if not CheckCollisionRecs(self.rect, player.rec):
            player.floorHeight = 800
        
        if CheckCollisionRecs(self.ceilingHitbox, player.rec):
            player.ceilingHeight = self.ceilingHitbox.y + 30
        if not CheckCollisionRecs(self.ceilingHitbox, player.rec):
            player.ceilingHeight = 20