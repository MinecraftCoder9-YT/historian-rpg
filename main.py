import os
import time
import threading
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

choice = input("Please select load game(l), or new game(n), or quit(q)")
while choice not in ("l", "n", "\n"):
    choice = input("Please select load game(l), or new game(n), or quit(q)") 
if choice == "q":
    exit()