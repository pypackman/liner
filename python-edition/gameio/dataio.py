import json

class DataIO:
    def __init__(self) -> None:
        self.palette = self.retrievePalette()
    def retrievePalette(self): 
        with open("json/palette.json", "r") as paletteFile: return json.loads(paletteFile.read())