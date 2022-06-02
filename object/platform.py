from raylib import *
import pyray as p
import random
class Platform:
    def __init__(self, posx, posy, width, height, color):
        self.rect=p.Rectangle(posx,posy,width,height)
        self.color = color
    
    def Draw(self):
        DrawRectangleRec(self.rect, self.color)

    def Collision(self, player):
        if CheckCollisionRecs(self.rect, player.rec):
            if player.rec.x < self.rect.x + self.rect.width and player.rec.x > self.rect.x:
                player.rec.x = random.randint(0,1600)
                player.rec.y = random.randint(0,900)
        if not CheckCollisionRecs(self.rect, player.rec):
            player.floorHeight = 800
    