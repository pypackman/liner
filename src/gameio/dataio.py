import json, os
from elements.platform import Platform
def getPalette() -> dict: return json.loads(open(os.path.join(os.path.dirname(__file__), 'palette.json')).read())
def getMap() -> dict:
    palette = getPalette()
    rawmap = json.loads(open(os.path.join(os.path.dirname(__file__), '../maps/map.json')).read())
    finalPlatList = []
    for platform in rawmap['platform']:
        finalPlatList.append(Platform(platform[0], platform[1], platform[2], platform[3], palette[platform[4]]))
    return finalPlatList
