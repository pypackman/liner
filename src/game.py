from raylib import *
from character.player import Player
from pyray import Camera2D
from config.fetch import loadConfig
from elements.platform import Platform
from gameio.dataio import getPalette

class Game:
    def __init__(self) -> None:
        self.version = 'alpha 1.0 bringup 2'
        self.palette = getPalette()
        self.config = loadConfig()
        self.width, self.height, self.fps, self.title = self.config['screen_width'], self.config['screen_height'], self.config['fps_clock'], bytes(self.config['title'], 'utf-8')
        self.player = Player()
        self.camera = Camera2D()
        self.camera.offset = self.width/2, self.height/2
        self.camera.rotation = 0.0
        self.camera.zoom = self.config['camera_zoom']
        self.testPlatform = Platform(200, 700, 300, 30, self.palette['orange'])

        InitWindow(self.width, self.height, self.title)
        SetTargetFPS(self.fps)
        while not WindowShouldClose(): self.update()

    def update(self):
        self.player.update()
        BeginDrawing()
        self.camera.target = self.player.rect.x + self.player.rect.width/2, self.player.rect.y + self.player.rect.height/2
        self.draw()
        EndDrawing()

    def draw(self):
        ClearBackground([240,240,240,255])
        DrawText(bytes(self.version, 'utf-8'), 20, 20, 20, self.palette['navy'])
        if self.config['debug_enable']:
            DrawText(bytes(f"XY: {round(self.player.rect.x,2)},{round(self.player.rect.y,2)}",'utf-8'), 20, 45, 15, self.palette['gray'])
            DrawText(bytes(f'XY Velocity: {round(self.player.velocity.x,1)},{round(self.player.velocity.y,1)}','utf-8'), 20, 60, 15, self.palette['gray'])
        if self.config['show_meow_in_credits']:
            DrawText(b"by easontek2398 and meowscripty",20,80,15,self.palette["lightblue"])
        BeginMode2D(self.camera)
        self.player.draw()
        self.testPlatform.draw()
        EndMode2D()



    