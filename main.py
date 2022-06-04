from game import Game
from sys import argv
from palettedemo import ColorPaletteDemo

def main():
    version = "alpha 0.3"
    print("\n"+version)
    try:
        if argv[1] == "game":
            G = Game(1600,900,60)
            try: 
                G.main() 
            except KeyboardInterrupt: 
                print("exit with esc") 
            exit()
        elif argv[1] == "palette":
            ColorPaletteDemo().demo()
        elif argv[1] == "exit":
            exit()
    except IndexError:
        print(
            "USAGE:\n"+
            "game: run game\n"+
            "palette: run palette demo\n"+
            "exit: exit\n"
        )
        exit()
    

if __name__ == "__main__": 
    main()