import pyray as p
from raylib import *
import time as t

class Player:
    def __init__(self, posx, posy, width, height, c):
        self.rec = p.Rectangle(posx, posy, width, height)
        self.color = c

        self.currentTime = int(t.time())

        self.frames = 0
        self.ticks = 0
        self.tickTimer = 0
        self.hasJumped = False
        self.stopIncrementingTickTimer = False
        self.hasStartedJumping = False
         
        self.xvelocity = 0
        self.yvelocity = 0 

    def Draw(self):
        DrawRectangleRec(self.rec, self.color)

    def Update(self, floorHeight):
        self.frames += 1
        if self.frames % 6 == 0:
            self.ticks += 1

        if floorHeight is None:
            floorHeight = 800


        # collision
        if self.rec.x < 20:
            self.xvelocity = 0
            self.rec.x = 20
        if self.rec.x > 1540:
            self.xvelocity = 0
            self.rec.x = 1540
        if self.rec.y > 800:
            self.rec.y = floorHeight

        if self.rec.y < 20:
            self.yvelocity = 0.1
            self.rec.y = 20

        # fall
        if self.rec.y <= floorHeight:
            self.yvelocity += 0.68
        if self.rec.y >= floorHeight:
            self.yvelocity = 0
            self.hasJumped = False

        # controls
        if IsKeyDown(KEY_RIGHT):
            self.xvelocity += 0.3
        if IsKeyDown(KEY_LEFT):
            self.xvelocity -= 0.3
        if IsKeyDown(KEY_SPACE):
            if self.frames % 6 == 0 and self.stopIncrementingTickTimer == False:
                self.tickTimer += 1
            if self.tickTimer < 4:
                self.yvelocity -= 1.5
            elif self.tickTimer > 15 and self.rec.y > 795:
                self.yvelocity = 4
                self.stopIncrementingTickTimer = True
                
                

        
        if IsKeyReleased(KEY_RIGHT):
            self.xvelocity = 0
        if IsKeyReleased(KEY_LEFT):
            self.xvelocity = 0
        if IsKeyReleased(KEY_SPACE):
            self.yvelocity = 4 
            self.tickTimer = 0
            self.stopIncrementingTickTimer = False

        # velocity
        if self.xvelocity != 0:
            self.rec.x += self.xvelocity
        if self.yvelocity != 0:
            self.rec.y += self.yvelocity
