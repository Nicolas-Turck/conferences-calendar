import os
import time
from view.vew import *
user = Display()

choice = ""
if __name__=='__main__':
    while choice != "q":
        choice = input("\033[36menter your choice \n "
                       "(a) for manage confereces "
                       "\n (b) for manage speakers "
                       "\n (q) for exit :\033[0m \n")
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)
        if choice == "a":
            user.conferences_choice()
        if choice == "b":
            user.speakers_choice()
        if choice == "q":
            exit()
