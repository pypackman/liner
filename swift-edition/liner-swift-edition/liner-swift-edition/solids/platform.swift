//
//  File.swift
//  liner-swift-edition
//
//  Created by easontek2398 on 8/6/22.
//

import Foundation
import Raylib

class Platform {
    var rect: Rectangle? = nil
    init(x posx: Float, y posy: Float, width Width: Float, height Height: Float) {
        self.rect = Rectangle(x: posx, y: posy, width: Width, height: Height)
    }
    func Draw() {
        
    }
    func Collision() {
        
    }
    func CeilingCollision() {
        
    }
}
