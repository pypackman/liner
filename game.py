import pyray as p
from raylib import *
import time as t
from object.platform import Platform
from character.player import Player
class Game:
    def __init__(self, w, h, f): 
        self.width, self.height = w,h
        self.fps = f
        self.title = b"wow liner"
    
    def main(self):
        player = Player(60, 60, 35, 90, p.RED)
        plat = Platform(500, 400, 200, 35, p.LIGHTGRAY)
        InitWindow(self.width, self.height, self.title)
        SetTargetFPS(self.fps)

        while not WindowShouldClose():
            # update
            player.Update()
            plat.Collision(player)
            BeginDrawing()
            ClearBackground(p.RAYWHITE) 
            player.Draw()
            plat.Draw()
            
            DrawText(bytes(f"xvelocity: {round(player.xvelocity, 2)}, yvelocity: {round(player.yvelocity, 2)}, x: {round(player.rec.x, 2)}, y: {round(player.rec.y,2)}", 'utf-8'), 30,30,15,p.LIGHTGRAY)
            DrawText(bytes(f"jump tick timer: {player.tickTimer} ticks: {player.ticks}",'utf-8'), 30,46,15,p.RED)
            DrawText(b"by easontek2398 and meowscripty", 30,62,15,p.BLUE)
            EndDrawing()
 