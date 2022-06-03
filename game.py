from object.platform import Platform
import pyray as p
from raylib import *
import time as t
from character.player import Player

class Game:
    def __init__(self, w, h, f): 
        self.width, self.height = w,h
        self.fps = 60
        self.title = b"liner v1.0"
    
    def main(self):
        InitWindow(self.width, self.height, self.title)
        SetTargetFPS(self.fps)
        player = Player(60,60,40,100,p.GOLD)
        floor = Platform(-350,900,2750,400,p.LIGHTGRAY)
        platform = Platform(200, 650, 150, 20, p.BLACK)
        platform2 = Platform(450, 450, 150, 20, p.BLACK)
        platform3 = Platform(600, 250, 150, 20, p.BLACK)
        camera = p.Camera2D()
        camera.offset = self.width/2, self.height/2
        camera.rotation = 0.0
        camera.zoom = 1.1

        while not WindowShouldClose():
            player.Update()
            floor.Collision(player)
            platform.Collision(player)
            platform2.Collision(player)
            platform3.Collision(player)


            BeginDrawing()
            camera.target = player.rec.x+player.rec.width/2,player.rec.y+player.rec.width
            ClearBackground(p.RAYWHITE) 
            DrawText(b"by easontek2398 and meowscripty", 30,32,15,p.BLUE)
            DrawText(bytes(f"x: {round(player.rec.x,2)}, y: {round(player.rec.y,2)}",'utf-8'), 30, 52, 15, p.RED)
            #cam
            BeginMode2D(camera)

            DrawRectangle(234,356,23,23,p.RED)
            player.Draw()
            floor.Draw()
            platform.Draw()
            platform2.Draw()
            platform3.Draw()

            EndMode2D()
            #endcam
            EndDrawing()
 