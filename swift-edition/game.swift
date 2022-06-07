//
//  game.swift
//  liner
//
//  Created by easontek2398 on 7/6/22.
//

import Foundation
import Raylib

class Game {
    var (screenWidth, screenHeight, FPS) = (0,0,0)
    init(_ scrwidth: Int,_ scrheight: Int, _ fps: Int) {
        self.screenWidth = scrwidth
        self.screenHeight = scrheight
        self.FPS = fps
    }
    func main() {
        Raylib.initWindow(Int32(self.screenWidth), Int32(self.screenHeight), "wow test")
        Raylib.setTargetFPS(Int32(self.FPS))
        
        while !Raylib.windowShouldClose {
            Raylib.beginDrawing()
            Raylib.clearBackground(.rayWhite)
            Raylib.endDrawing()
        }
    }
}
