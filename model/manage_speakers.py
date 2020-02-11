import os
from model.connection import *
class Managespeakers():
    def __init__(self):
        self.name = None
        self.lastname = None
        self.description = None
        self.job = None
        self.db = Connection()
        self.choice = ""

    def choice(self):
        while self.choice != "q":
            self.choice = input("(c) for create \n (d) for delete \n (s) for see")
            if self.choice == "c":
                print("create")

            if self.choice == "d":
                print("delette")

            if self.choice == "s":
                print("see speakers")

            if self.choice == "q":
                exit()

