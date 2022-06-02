from game import Game
from sys import argv

def main():
    version = "0.1a3"

    if argv[1] == "game":
        G = Game(1600,900,60)
        try: 
            G.main() 
        except KeyboardInterrupt: 
            print("exit with esc") 
        exit()
    elif argv[1] == "exit":
        exit()
    else:
        print("Usage:\n  game: start game\n  exit: exit the program\n")

if __name__ == "__main__": 
    main()