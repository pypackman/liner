from raylib import *
from pyray import Rectangle, Vector2
from config.fetch import loadConfig
from gameio.dataio import getPalette

class Player:
    def __init__(self):
        self.rect = Rectangle(-20,60,50,100)
        self.color = getPalette()['lightblue']
        self.velocity = Vector2(0,0)
        self.controlset = loadConfig()['controls']

        self.frames = 0
        self.fallSpeed = 3.5
        self.ticks = 0
        self.jumpTickTimer = 0
        self.stopIncrementingJumpTickTimer = False
        self.floorHeight = 900

    def draw(self):
        DrawRectangleRec(self.rect, self.color)
    
    def controls(self):
        self.rect.x = round(self.rect.x, 1)
        self.rect.y = round(self.rect.y, 1)
        if IsKeyDown(self.controlset['move_forward']):
            self.velocity.x += 0.3
        if IsKeyDown(self.controlset['move_backward']):
            self.velocity.x -= 0.3
        if IsKeyReleased(self.controlset['move_forward']) or IsKeyReleased(self.controlset['move_backward']):
            self.velocity.x = 0
        
        if IsKeyDown(self.controlset['jump']):
            if self.frames % 6 == 0 and self.stopIncrementingJumpTickTimer is False:
                self.jumpTickTimer += 1
            if self.jumpTickTimer < 3:
                self.velocity.y -= 1.5
            elif self.jumpTickTimer > 4 and self.rect.y > self.floorHeight - 5:
                self.yvelocity = self.fallSpeed
                self.stopIncrementingJumpTickTimer = False



        self.rect.x += self.velocity.x 
        self.rect.y += self.velocity.y


    def update(self):
        self.frames += 1
        if self.frames % 6 == 0:
            self.ticks += 1
        if self.rect.y < self.floorHeight:
            self.velocity.y += 1
        elif self.rect.y >= self.floorHeight:
            self.velocity.y = 0
        

        self.controls()