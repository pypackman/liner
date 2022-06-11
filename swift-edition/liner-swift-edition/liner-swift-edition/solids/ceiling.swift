//
//  ceiling.swift
//  liner-swift-edition
//
//  Created by easontek2398 on 8/6/22.
//

import Foundation
import Raylib

class Ceiling {
    var ceiling: Rectangle = Rectangle()
    init(x posx: Float, y posy: Float, width Width: Float, height Height: Float) {
        self.ceiling = Rectangle(x: posx, y: posy, width: Width, height: Height)
    }
    
    func Draw() {
        
    }
    func IsPlayerUnder(_ player: Player) -> Bool {
        if player.rec!.x < self.ceiling.x + self.ceiling.width && player.rec!.x + player.rec!.width > self.ceiling.x && player.rec!.y > self.ceiling.y {
            return true
        } else {
            return false
        }
    }
}
