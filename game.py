from tkinter import Y
from object.ceiling import Ceiling
import pyray as p
from raylib import *
from gameio.dataio import DataIO
from gameio.mapio import MapIO
from character.player import Player

class Game:
    def __init__(self, w, h,f, v): 
        self.currentScreen = "title"
        self.version = v
        self.width, self.height = w,h
        self.fps = f
        self.frames = 0
        self.ticks = 0
        self.tps = 10
        self.platforms = MapIO().getMapInfo("json/maps/map.json")
        self.ceilings = []
        self.title = b"liner"
        self.palette = DataIO().retrievePalette()
        for platform in self.platforms:
            self.ceilings.append(platform.ceilingHitbox)
    
    def CheckCollisionPlatforms(self, platform, player):
        if platform.Collision(player):
            if player.rec.x < platform.rect.x + platform.rect.width and player.rec.x + player.rec.width > platform.rect.x:
                player.floorHeight = platform.rect.y - player.rec.height
        else:
            for p in self.platforms:
                if player.rec.x < p.rect.x + p.rect.width and player.rec.x + player.rec.width > p.rect.x:
                    if p.rect.y > player.rec.y:
                        player.floorHeight = p.rect.y - player.rec.height
    def CheckCollisionPlatformCeilings(self,player):
        for c in self.ceilings:
            if c.IsPlayerUnder(player):
                player.ceilingHeight = c.ceiling.y + c.ceiling.height

                        
    
    def main(self):
        InitWindow(self.width, self.height, self.title)
        SetTargetFPS(self.fps)
        print(self.platforms)
        
        player = Player(60,60,40,100,p.GOLD)
        
        camera = p.Camera2D()
        camera.offset = self.width/2, self.height/2
        camera.rotation = 0.0
        camera.zoom = 1.1

        while not WindowShouldClose():
            self.frames+=1
            if self.frames % 6 == 0:
                self.ticks+=1
            self.tps = round(self.fps/6)

            if self.currentScreen == "title":
                if IsKeyDown(KEY_ENTER):
                    self.currentScreen = "game"

            if self.currentScreen == "game":
                player.Update()
                for platform in self.platforms:
                    self.CheckCollisionPlatforms(platform, player)    
                self.CheckCollisionPlatformCeilings(player)

            BeginDrawing()
            if self.currentScreen == "title":
                ClearBackground(self.palette['lightblue'])
                DrawText(b"Welcome to Liner!", 30,35,30,self.palette['navy'])
                DrawText(bytes(f"press [ENTER] to run game ", 'utf-8'), 30,75,40,self.palette['navy'])
                DrawText(bytes(f"version {self.version}",'utf-8'), 30,115,20,self.palette['navy'])

            if self.currentScreen == "game":
                camera.target = player.rec.x+player.rec.width/2,player.rec.y+player.rec.width
                ClearBackground(p.RAYWHITE) 
                DrawText(bytes(f"Ticks: {self.ticks}, TPS: {self.tps}",'utf-8'), 30, 32, 15 , p.SKYBLUE)
                DrawText(b"by easontek2398 and meowscripty", 30,52,15,p.BLUE)
                DrawText(bytes(f"x: {round(player.rec.x,2)}, y: {round(player.rec.y,2)}",'utf-8'), 30, 72, 15, p.RED)
                DrawText(bytes(f"xvelocity: {round(player.xvelocity,2)}, yvelocity: {round(player.yvelocity,2)}",'utf-8'), 30, 92, 15, p.PINK)
                DrawText(bytes(f"currentceilingheight: {round(player.ceilingHeight,1)}, jumpticktimer: {player.tickTimer}",'utf-8'), 30, 112, 15, p.GREEN)
                #cam
                BeginMode2D(camera)

                DrawRectangle(234,356,23,23,p.RED)
                player.Draw()
                self.ceilings[0].Draw()
                for platform in self.platforms:
                    platform.Draw()
                EndMode2D()
            #endcam
            EndDrawing()
 