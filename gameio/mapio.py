import json
from object.platform import Platform
from gameio.dataio import DataIO

class MapIO:
    def __init__(self) -> None:
        self.finalMap = []
        self.palette = DataIO().retrievePalette()
    def getMapInfo(self, infile):
        with open(infile, 'r') as raw:
            rawmap = json.loads(raw.read())
            for platform in rawmap.values():
                self.finalMap.append(Platform(platform[0],platform[1],platform[2],platform[3],self.palette[platform[4]]))
            return self.finalMap