from object.platform import Platform
import pyray as p
from raylib import *
from gameio.mapio import MapIO
import time as t
from character.player import Player

class Game:
    def __init__(self, w, h, f): 
        m = MapIO()
        self.width, self.height = w,h
        self.fps = 60
        self.frames = 0
        self.ticks = 0
        self.tps = 10
        self.platforms = m.getMapInfo("map.json")
        self.title = b"wow liner"
    
    def CheckCollisionPlatforms(self, platform, player):
        if platform.Collision(player):
            if player.rec.x < platform.rect.x + platform.rect.width and player.rec.x + player.rec.width > platform.rect.x:
                player.floorHeight = platform.rect.y - player.rec.height
        else:
            for plat in self.platforms:
                if player.rec.x < plat.rect.x + plat.rect.width and player.rec.x + player.rec.width > plat.rect.x:
                    player.floorHeight = plat.rect.y - player.rec.height                
    
    def main(self):
        InitWindow(self.width, self.height, self.title)
        SetTargetFPS(self.fps)
        
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
            player.Update()

            for platform in self.platforms:
                self.CheckCollisionPlatforms(platform, player)

            BeginDrawing()
            camera.target = player.rec.x+player.rec.width/2,player.rec.y+player.rec.width
            ClearBackground(p.RAYWHITE) 
            DrawText(bytes(f"Ticks: {self.ticks}, TPS: {self.tps}",'utf-8'), 30, 32, 15 , p.SKYBLUE)
            DrawText(b"by easontek2398 and meowscripty", 30,52,15,p.BLUE)
            DrawText(bytes(f"x: {round(player.rec.x,2)}, y: {round(player.rec.y,2)}",'utf-8'), 30, 72, 15, p.RED)
            DrawText(bytes(f"xvelocity: {round(player.xvelocity,2)}, yvelocity: {round(player.yvelocity,2)}",'utf-8'), 30, 92, 15, p.PINK)
            DrawText(bytes(f"currentfloorheight: {round(player.floorHeight,1)}, jumpticktimer: {player.tickTimer}",'utf-8'), 30, 112, 15, p.GREEN)
            #cam
            BeginMode2D(camera)

            DrawRectangle(234,356,23,23,p.RED)
            player.Draw()
            for platform in self.platforms:
                platform.Draw()

            EndMode2D()
            #endcam
            EndDrawing()
 