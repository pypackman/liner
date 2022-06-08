//
//  player.swift
//  liner-swift-edition
//
//  Created by easontek2398 on 8/6/22.
//

import Foundation
import Raylib

class Player {
    var frames = 0
    var ticks = 0
    
    var rec:Rectangle? = nil
    var xvelocity:Double = 0
    var yvelocity:Double = 0
    
    init(X posx:Float, Y posy:Float, Width width:Float, Height height:Float, Color color:Color) {
        self.rec = Rectangle(x: posx, y: posy, width: width, height: height)
    }
    
    func Controls() {
        if Raylib.isKeyDown(.left) {
            self.xvelocity += 0.5
        }
        if Raylib.isKeyDown(.right) {
            self.xvelocity -= 0.5
        }
        if Raylib.isKeyReleased(.right) || Raylib.isKeyReleased(.left) {
            self.xvelocity = 0
        }
    }
    
    func Update() {
        self.Controls()
        self.frames += 1
        if self.frames % 6 == 0 {
            self.ticks += 1
        }
        self.rec!.x += Float(self.xvelocity)
    }
    
    func Draw() {
        Raylib.drawRectangleRec(self.rec!, .gold)
    }
}
