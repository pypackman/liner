import pyray as p
from raylib import *
import math
from character.player import Player

class Game:
    def __init__(self, w, h, f): 
        self.width, self.height = w,h
        self.fps = f
        self.title = b"wow liner"
    
    def main(self):
        player = Player(60, 60, 35, 90, p.RED)

        InitWindow(self.width, self.height, self.title)
        SetTargetFPS(self.fps)

        while not WindowShouldClose():
            # update
            player.Update(800)

            BeginDrawing()
            ClearBackground(p.RAYWHITE) 
            player.Draw()
            DrawText(bytes(f"xvelocity: {round(player.xvelocity, 2)}, yvelocity: {round(player.yvelocity, 2)}", 'utf-8'), 30,30,15,p.LIGHTGRAY)
            DrawText(bytes(f"jump tick timer: {player.tickTimer} ticks: {player.ticks}",'utf-8'), 30,46,15,p.RED)
            DrawText(bytes(f"hasJumped: {player.hasJumped}, hasStartedJumping: {player.hasStartedJumping}", 'utf-8'),30,62,15,p.GOLD)
            EndDrawing()