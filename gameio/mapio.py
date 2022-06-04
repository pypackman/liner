import json
from raylib import *
import pyray as p
from object.platform import Platform

class MapIO:
    def __init__(self) -> None:
        self.finalMap = []
        self.palette = self.retrievePalette()

    def retrievePalette(self): 
        with open("json/palette.json", "r") as paletteFile: return json.loads(paletteFile.read())

    def getMapInfo(self, infile):
        with open(infile, 'r') as raw:
            rawmap = json.loads(raw.read())
            for platform in rawmap.values():
                self.finalMap.append(Platform(platform[0],platform[1],platform[2],platform[3], self.palette[platform[4]]))
            return self.finalMap