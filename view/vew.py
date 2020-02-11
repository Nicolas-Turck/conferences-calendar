from model.manage_speakers import *
class Display():
    def __init__(self):
        self.choice = None

    def speakers_choice(self):
        while self.choice != "q":
            self.choice = input("\033[36m(c) for create \n (d) for delete \n (s) for see\033[0m")
            if self.choice == "c":
                name = input("\033[32menter name:\033[0m")
                lastname = input("\033[32menter lastname:\033[m")
                description = input("\033[32menter decription:\033[0m")
                job = input("\033[32menter job:\033[0M")
                speakers = Managespeakers(name, lastname, description, job)
                speakers.create_speakers()

            if self.choice == "d":
                print("delette")

            if self.choice == "s":
                print("see speakers")

            if self.choice == "q":
                exit()
    def conferences_choice(self):
        while self.choice != "q":
            self.choice = input("\033[33m(c) for create \n (d) for delete \n (s) for see\033[0m")
            if self.choice == "c":
                print("create")

            if self.choice == "d":
                print("delette")

            if self.choice == "s":
                print("see speakers")

            if self.choice == "q":
                exit()