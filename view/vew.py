from model.manage_speakers import *
from model.manage_conferences import *
import os
import time
class Display():
    """class for display menu of speakers and conference and purpose choice"""
    speakers = Managespeakers()
    conf = Managesconferences()
    def __init__(self):
        self.choice = None
        self.user = Managespeakers()
        self.users = Managesconferences()
        column = ""


    def speakers_choice(self):
        """method for ask user choice and got to method machingchoice """
        while self.choice != "q":
            self.choice = input("\033[35m(c) for create \n(d) for delete \n(s) for see \n(r) for return start page \n(q) for exit:\033[0m")
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(1)
            if self.choice == "c":
                name = input("\033[32menter name:\033[0m")
                lastname = input("\033[32menter lastname:\033[0m")
                description = input("\033[32menter decription:\033[0m")
                job = input("\033[32menter job:\033[0M")
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                self.user.create_speakers(name, lastname, description, job)

            if self.choice == "d":
                id = input("\033[32menter speakers ID :\033[0m")
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                self.user.delete_speakers(id)

            if self.choice == "s":
                datta = self.speakers.show_speakers()
                if datta:
                    for elem in datta:
                        print(elem)
            if self.choice == "r":
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                return

            if self.choice == "q":
                exit()
    def conferences_choice(self):
        """method for ask user choice and got to method machingchoice """
        while self.choice != "q":
            self.choice = input("\033[35m(c) for create \n(m) for modify \n"
                                "(d) for delete \n(s) for see \n"
                                "(q) for exit \n(r) for return start page:\033[0m")
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(1)
            if self.choice == "c":
                title = input("\033[33menter title:\033[0m")
                summary = input("\033[33menter summary:\033[0m")
                date = input("\033[33menter date:\033[0m")
                hour = input("\033[33menter hour \033[0m")
                speaker = input("\033[33menter speaker ID: \033[0m")
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                self.users.create_conferences(title, summary, date, hour, speaker)


            if self.choice == "m":
                while column not in ['title', 'resume', 'date', 'hour', 'personid']:
                    id = input("\033[33menter confernces id :\033[0m")
                    column = input(
                        "\033[33mwhat do you want to modify \n [title, resume, date, hour, personid] :\033[0m")
                    datta = input("\033[33menter new datta:\033[0m")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(1)
                    self.users.update_confernces(id, column, datta)


            if self.choice == "d":
                id = input("\033[33menter conferences ID :\033[0m")
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                self.users.delete_conferences(id)


            if self.choice == "s":
                datta = self.conf.show_conferences()
                if datta:
                    for elem in datta:
                        print(elem)
            if self.choice == "r":
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                return
            if self.choice == "q":
                exit()