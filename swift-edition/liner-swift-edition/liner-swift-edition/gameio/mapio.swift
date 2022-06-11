//
//  mapio.swift
//  liner-swift-edition
//
//  Created by easontek2398 on 9/6/22.
//

import Foundation

struct MapIO {
    var map = [
        "platform" : [
            [-800, 800, 30000, 400, [200,200,200,255]],
            [200, 650, 150, 20, [0,0,0,255]],
            [450, 450, 150, 20, [0,0,0,255]],
            [650, 250, 150, 20, [0,0,0,255]],
            [900, 500, 350, 20, [0,0,0,255]]
        ],
        "wall" : [
            [-800,40,100,760,[60,60,60,255]],
            [1300,40,100,760,[60,60,60,255]]
        ]
    ]
    var finalPlatformList = [] as! Array<Any>
    var finalCeilingList = [] as! Array<Any>
    
    
    mutating func structurizseMap() {
        for plat in self.map["platform"]! {
            self.finalPlatformList.append([plat[0],plat[1],plat[2],plat[3], plat[4]])
        }
        for wall in self.map["wall"]! {
                self.finalPlatformList.append([wall[0],wall[1],wall[2],wall[3], wall[4]])
        }
    }
}
