from raylib import *
import pyray as p
from gameio.mapio import MapIO

class ColorPaletteDemo:
    def __init__(self) -> None:
        self.palette = MapIO().retrievePalette()
    def demo(self):
        width,height = 1600,150
        InitWindow(width,height,b"liner palette demo")
        SetTargetFPS(60)

        camera = p.Camera2D()
        camera.offset = width/2, height/2
        camera.rotation = 0.0
        camera.zoom = 1.1
        camera.target = (655,75)

        while not WindowShouldClose():
            if IsKeyPressed(KEY_LEFT):
                camera.target.x -= 100
            if IsKeyPressed(KEY_RIGHT):
                camera.target.x += 100
                print(camera.target.x)
    
            BeginDrawing()
            ClearBackground(self.palette['white'])
            BeginMode2D(camera)
            for i,k in enumerate(self.palette):
                DrawText(bytes(k, 'utf-8'),i*100+i*30+10-75,10,15,self.palette['black'])
                DrawRectangle(i*100+i*30+10-75,35,100,100,self.palette[k])
            EndMode2D()
            EndDrawing()