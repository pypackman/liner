import json
from raylib import *
import pyray as p
from object.platform import Platform

class MapIO:
    def __init__(self) -> None:
        self.finalMap = []
    def getMapInfo(self, infile):
        rawmap = {
            "0" : [-800, 800, 30000, 400,[200,200,200,255]],
            "1" : [200, 650, 150, 20, [0,0,0,255]],
            "2" : [450, 450, 150, 20, [0,0,0,255]]
        }
        
        for m in rawmap.values():
            self.finalMap.append(Platform(m[0],m[1],m[2],m[3],m[4]))
            return self.finalMap