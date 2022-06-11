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
    var player = Player(X: 0, Y: 30, Width: 40, Height: 100, Color: .gold)
    var camera = Camera2D()
    
    init(DisplayWidth w: Int,DisplayHeight h: Int,FPSClock f: Int32) {
        self.screenWidth = w
        self.screenHeight = h
        self.FPS = f
        self.camera.zoom = 1.1
        self.camera.rotation = 0.0
        self.camera.offset = Vector2(x: Float(self.screenWidth / 2) + player.xvelocity, y: Float(self.screenHeight / 2))
        
    }
    
    func Update() {
        
        player.Update()
        
        Raylib.beginDrawing()
        // non camera
        Raylib.clearBackground(.rayWhite)
        Raylib.drawText("Ticks: \(player.ticks)", 20, 20, 15, .red)
        Raylib.drawText("by easontek2398", 20, 40, 15, .skyBlue)
        Raylib.drawText("x: \(player.rec!.x), y: \(player.rec!.y)", 20, 60, 15, .green)
        Raylib.drawText("xvelocity: \(player.xvelocity), yvelocity: \(player.yvelocity)", 20, 80, 15, .darkGreen)
        Raylib.drawText("camera offset x: \(self.camera.offset.x), camera offset y: \(self.camera.offset.y), camera target x: \(self.camera.target.x), camera target y: \(self.camera.target.y)", 20, 100, 15, .lime)
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
            self.camera.target = Vector2(x: player.rec!.x + player.rec!.width / 2 + player.xvelocity, y: player.rec!.y + player.rec!.width)
            self.Update()
        }
            
    }
}
