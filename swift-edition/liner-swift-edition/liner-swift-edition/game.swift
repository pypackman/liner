//
//  game.swift
//  liner-swift-edition
//
//  Created by easontek2398 on 8/6/22.
//

import Foundation
import Raylib

class Game {
    var screenWidth = 0
    var screenHeight = 0
    
    var windowTitle: String = "Wow Liner"
    var FPS:Int32? = nil
    var player = Player(X: 0, Y: 0, Width: 40, Height: 100, Color: .gold)
    var camera = Camera2D()
    
    init(DisplayWidth w: Int,DisplayHeight h: Int,FPSClock f: Int32) {
        self.screenWidth = w
        self.screenHeight = h
        self.FPS = f
        self.camera.offset = Vector2(x: Float(self.screenWidth/2), y: Float(self.screenHeight/2))
        self.camera.rotation = 0.0
        self.camera.zoom = 1.0
    }
    
    func Update() {
        self.camera.target = Vector2(x: Float(self.player.rec!.x + self.player.rec!.width / 2), y: Float(self.player.rec!.y + self.player.rec!.width))
        
        
        player.Update()
        
        Raylib.beginDrawing()
        // non camera
        Raylib.clearBackground(.rayWhite)
        Raylib.drawText("Ticks: \(player.ticks)", 20, 20, 15, .red)
        // -----
        Raylib.beginMode2D(self.camera)
        // camera
        Raylib.drawRectangle(134,234,34,34,.magenta)
        // external calls
        player.Draw()
        // -----
        // -----
        Raylib.endMode2D()
        Raylib.endDrawing()
    }
    
    func main() {
        Raylib.initWindow(Int32(self.screenWidth), Int32(self.screenHeight), self.windowTitle)
        Raylib.setTargetFPS(self.FPS ?? 60)

        while !Raylib.windowShouldClose {
            self.Update()
            
        }
            
    }
}
