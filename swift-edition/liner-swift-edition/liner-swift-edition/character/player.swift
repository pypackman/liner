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
    var xvelocity:Float = 0
    var yvelocity:Float = 0
    var floorHeight: Float = 1000
    var currentFrame = 0
    
    var timer = 0
    
    init(X posx:Float, Y posy:Float, Width width:Float, Height height:Float, Color color:Color) {
        self.rec = Rectangle(x: posx, y: posy, width: width, height: height)
    }
    
    func Physics() {
        if self.rec!.y <= self.floorHeight {
            self.yvelocity += 0.68
        } else {
            self.yvelocity = 0
            self.rec!.y = self.floorHeight
        }
    }
    
    func Controls() {
        if Raylib.isKeyDown(.left) {
            self.xvelocity -= 0.5
        }
        if Raylib.isKeyDown(.right) {
            self.xvelocity += 0.5
        }
        if Raylib.isKeyReleased(.right) || Raylib.isKeyReleased(.left) {
            self.xvelocity = 0
        }
    }
    
    func Update() {
        self.Controls()
        self.Physics()
        self.frames += 1
        if self.frames % 6 == 0 {
            self.ticks += 1
        }
        self.rec!.x += Float(Int(self.xvelocity))
        self.rec!.y += Float(Int(self.yvelocity))
    }
    
    func Draw() {
        Raylib.drawRectangleRec(self.rec!, .gold)
    }
}
