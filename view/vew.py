from model.manage_speakers import *
class Display():
    speakers = Managespeakers()
    def __init__(self):
        self.choice = None

    def speakers_choice(self):
        user = Managespeakers()
        while self.choice != "q":
            self.choice = input("\033[36m(c) for create \n (d) for delete \n (s) for see\033[0m")
            if self.choice == "c":
                name = input("\033[32menter name:\033[0m")
                lastname = input("\033[32menter lastname:\033[0m")
                description = input("\033[32menter decription:\033[0m")
                job = input("\033[32menter job:\033[0M")
                user.create_speakers(name, lastname, description, job)

            if self.choice == "d":
                id = input("\033[32menter speakers ID :\033[0m")
                user.delete_speakers(id)


            if self.choice == "s":
                #speakers = Managespeakers()
                datta = self.speakers.show_speakers()
                if datta:
                    for elem in datta:
                        print(elem)

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