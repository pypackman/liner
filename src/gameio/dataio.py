import json,os
def getPalette() -> dict: return json.loads(open(os.path.join(os.path.dirname(__file__), 'palette.json')).read())
def getMap() -> dict: return json.loads(open(os.path.join(os.path.dirname(__file__), '../maps/map.json')).read())