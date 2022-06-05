import json
import platform
from solids import platform,wall
from gameio.dataio import DataIO
class MapIO:
    def __init__(self) -> None:
        self.finalPlatList = []
        self.finalWallList = []
        self.palette = DataIO().retrievePalette()
    def getMapInfo(self, infile):
        with open(infile, 'r') as raw:
            rawmap = json.loads(raw.read())
            for plat in rawmap['platform']:
                self.finalPlatList.append(platform.Platform(plat[0],plat[1],plat[2],plat[3],self.palette[plat[4]]))
            for wal in rawmap['wall']:
                self.finalWallList.append(wall.Wall(wal[0],wal[1],wal[2],wal[3],self.palette[wal[4]]))
            return self.finalPlatList,self.finalWallList