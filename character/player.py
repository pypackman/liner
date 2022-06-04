import pyray as p
from raylib import *
import time as t

class Player:
    def __init__(self, posx, posy, width, height, c):
        self.rec = p.Rectangle(posx, posy, width, height)
        self.color = c
        self.isOnFloor = True
        self.currentTime = int(t.time())

        self.ceilingHeight = 30
        self.floorHeight = 1000
        self.frames = 0
        self.ticks = 0
        self.tickTimer = 0
        self.stopIncrementingTickTimer = False
         
        self.xvelocity = 0
        self.yvelocity = 0 

    def Draw(self):
        DrawRectangleRec(self.rec, self.color)

    def Update(self):
        self.frames += 1
        if self.frames % 6 == 0:
            self.ticks += 1
        
        if self.rec.x <= -400:
            self.xvelocity = 0
            self.rec.x = -400

        # collision
        if self.rec.y > self.floorHeight:
            self.rec.y = self.floorHeight

        if self.rec.y < self.ceilingHeight:
            self.yvelocity = 0
            self.rec.y = self.ceilingHeight

        # fall
        if self.rec.y <= self.floorHeight:
            self.yvelocity += 0.68
        if self.rec.y >= self.floorHeight:
            self.yvelocity = 0

        # controls
        if IsKeyDown(KEY_RIGHT):
            self.xvelocity += 0.2
        if IsKeyDown(KEY_LEFT):
            self.xvelocity -= 0.2
        if IsKeyDown(KEY_SPACE):
                if self.frames % 6 == 0 and self.stopIncrementingTickTimer == False:
                    self.tickTimer += 1
                if self.tickTimer < 4:
                    self.yvelocity -= 1.5
                elif self.tickTimer > 5 and self.rec.y > 795:
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
