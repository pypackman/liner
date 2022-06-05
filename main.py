from game import Game
from sys import argv
from palettedemo import ColorPaletteDemo

def main():
    version = "alpha 0.4"
    print("\n"+version)
    if argv[1] == "start":
        G = Game(1600,900,60,version)
        try: 
            G.main() 
        except KeyboardInterrupt: 
             print("exit with esc") 
    elif argv[1] == "palette":
         ColorPaletteDemo().demo()    

if __name__ == "__main__": 
    main()