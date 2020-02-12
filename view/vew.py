from model.manage_speakers import *
from model.manage_conferences import *
class Display():
    speakers = Managespeakers()
    conf = Managesconferences()
    def __init__(self):
        self.choice = None
        self.user = Managespeakers()
        self.users = Managesconferences()
    def speakers_choice(self):
        """method for ask user choice and got to method machingchoice """
        #user = Managespeakers()
        while self.choice != "q":
            self.choice = input("\033[35m(c) for create \n(d) for delete \n(s) for see:\033[0m")
            if self.choice == "c":
                name = input("\033[32menter name:\033[0m")
                lastname = input("\033[32menter lastname:\033[0m")
                description = input("\033[32menter decription:\033[0m")
                job = input("\033[32menter job:\033[0M")
                self.user.create_speakers(name, lastname, description, job)

            if self.choice == "d":
                id = input("\033[32menter speakers ID :\033[0m")
                self.user.delete_speakers(id)

            if self.choice == "s":
                datta = self.speakers.show_speakers()
                if datta:
                    for elem in datta:
                        print(elem)

            if self.choice == "q":
                exit()
    def conferences_choice(self):
        """method for ask user choice and got to method machingchoice """
        #users = Managesconferences()
        while self.choice != "q":
            self.choice = input("\033[35m(c) for create \n(d) for delete \n(s) for see\033[0m")
            if self.choice == "c":
                title = input("\033[33menter title:\033[0m")
                summary = input("\033[33menter summary:\033[0m")
                date = input("\033[33menter date:\033[0m")
                hour = input("\033[33menter hour \033[0m")
                speaker = input("\033[33menter speaker ID: \033[0m")
                self.users.create_conferences(title, summary, date, hour, speaker)
            if self.choice == "d":
                id = input("\033[33menter speakers ID :\033[0m")
                self.users.delete_conferences(id)

            if self.choice == "s":
                datta = self.conf.show_conferences()
                if datta:
                    for elem in datta:
                        print(elem)

            if self.choice == "q":
                exit()