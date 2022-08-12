import os
import time
import threading

class Game:
    def __init__(self, path):
        self.path = path
os.system("cls")
title = """
                                                                                                      
,--.  ,--.,--. ,---.,--------.,-----. ,------. ,--.  ,---.  ,--.  ,--.    ,------. ,------. ,----.    
|  '--'  ||  |'   .-'--.  .--'  .-.  '|  .--. '|  | /  O  \ |  ,'.|  |    |  .--. '|  .--. '  .-./    
|  .--.  ||  |`.  `-.  |  |  |  | |  ||  '--'.'|  ||  .-.  ||  |' '  |    |  '--'.'|  '--' |  | .---. 
|  |  |  ||  |.-'    | |  |  '  '-'  '|  |\  \ |  ||  | |  ||  | `   |    |  |\  \ |  | --''  '--'  | 
`--'  `--'`--'`-----'  `--'   `-----' `--' '--'`--'`--' `--'`--'  `--'    `--' '--'`--'     `------'  
                                                                                                      
"""    

enter_to_play = """
    ____                         _______   __________________     __                __             __ 
   / __ \________  __________   / ____/ | / /_  __/ ____/ __ \   / /_____     _____/ /_____ ______/ /_
  / /_/ / ___/ _ \/ ___/ ___/  / __/ /  |/ / / / / __/ / /_/ /  / __/ __ \   / ___/ __/ __ `/ ___/ __/
 / ____/ /  /  __(__  |__  )  / /___/ /|  / / / / /___/ _, _/  / /_/ /_/ /  (__  ) /_/ /_/ / /  / /_  
/_/   /_/   \___/____/____/  /_____/_/ |_/ /_/ /_____/_/ |_|   \__/\____/  /____/\__/\__,_/_/   \__/  
"""
print(title)
def show_msg():
    counter=0
    while getattr(threading.currentThread(), "do_run", True):
        os.system("cls" if os.name == "nt" else "clear")
        print(title)
        if counter == 0:
            print(enter_to_play)
        counter = 1 if counter == 0 else 0
        time.sleep(.5)
show_msg_thread = threading.Thread(target=show_msg)
show_msg_thread.start()
input()
os.system("cls" if os.name == "nt" else "clear")
show_msg_thread.do_run = False
print("Historian Rpg: copyright (c) 2022")
print("ABSOLUTELY NO WARRANTY")
time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")

while True:
    choice = input("Please select load game(l), or new game(n), or quit(q)")
    while choice not in ("l", "n", "q"):
        choice = input("Please select load game(l), or new game(n), or quit(q)") 
    if choice == "q":
        exit()
    elif choice == "n":
        game_name = input("What is the game's name(e.g My_Game)? ")
        game_name = game_name.replace(" ", "_")
        choice = input("Do you want the name "+game_name+" for your game(y/n)")
        while choice not in ("y", "n"):
            choice = input("Do you want the name "+game_name+" for your game(y/n)")
        if choice == "y":
            game = Game(game_name)
            print("Game created! (Name: "+game.path + ")")
        else:
            game_name = input("What is the game's name(e.g My_Game)? ")
            game_name.replace(" ", "_")
            game = Game(game_name)
            print("Game created! (Name: "+game.path + ")")
