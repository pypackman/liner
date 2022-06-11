#!/usr/local/bin/python3
# macos .command executable 

from game.game import Game
from palettedemo import ColorPaletteDemo
import tkinter as ttk
from tkinter import BOTTOM,TOP,LEFT,RIGHT

version = "alpha 0.5"

class Commands:
    def launchMainGame():
        Game(1152,648,60,version).main()
    
class Window(ttk.Tk):
    def __init__(self):
        super().__init__()
        self.frame = ttk.Frame(self)
        
        self.widgets = self.addWidgets()
        for widget in self.widgets.values():
            widget[0].pack(
                side=widget[1],
                ipadx=widget[2],
                ipady=widget[3],
                padx=widget[4],
                pady=widget[5]
            )

        self.frame.pack(padx=10,pady=10)
    
    def addWidgets(self) -> dict:
        wid = {}
        wid['titletext'] = [ttk.Label(self.frame, text="Liner Launcher"),TOP,2,2,5,5] # widget, side, ipadx, ipady, padx, pady
        wid['launchbutton'] = [ttk.Button(self.frame, text="Launch Game", command=Commands.launchMainGame), LEFT,1,1,3,3]
        wid['exitbutton'] = [ttk.Button(self.frame,text="Exit Launcher",command=exit), RIGHT,1,1,3,3]

        return wid 

if __name__ == "__main__": 
    w=Window()
    w.title="Liner Launcher"
    w.mainloop()