from game import Game

def main():
    version = "0.1a1"

    while True:
        print(f"version: {version}")
        c = input("[startgame] [exit]\n: ")
        if c == "startgame":
            G = Game(1600,900,60)
            G.main()
            exit()
        elif c == "exit":
            exit()
        else:
            print("please enter a valid choice!")


if __name__ == "__main__": main()
