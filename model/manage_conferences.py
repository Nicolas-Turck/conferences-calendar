import datetime
from model.connection import *
from controller.conferencesentities import *
import os
import time
class Managesconferences():
    """class for manage confernce create read delete CRUD"""
    def __init__(self):
        self.db = Connection()
        self.creation_date = datetime.date.today()
        self.sql = ""
        self.arguments = ""

    def create_conferences(self, title, summary, date, hour, speaker):
        """method for add conferences in bdd"""
        self.db.initialize_connection()
        self.sql = "INSERT INTO conferences(title, summary, date, hour, " \
              "creation_date, personid) VALUES (%s, %s, %s, %s, %s, %s);"
        self.arguments = (title, summary, date, hour, self.creation_date, speaker,)
        self.db.cursor.execute(self.sql, self.arguments)
        self.db.connection.commit()
        self.db.close_connection()
        print("\033[31mnew conferences create\033[0m")

    def delete_conferences(self, id):
        """method for delete conferences in bdd with this personal id"""
        self.db.initialize_connection()
        self.sql = "DELETE FROM conferences WHERE id = %s;"
        self.arguments = (id,)
        self.db.cursor.execute(self.sql, self.arguments)
        self.db.connection.commit()
        self.db.close_connection()
        print("\033[31mconferences deletted\033[0m")

    def show_conferences(self):
        """method for display all conferences and auto with join sql"""
        self.sql = "SELECT c.*, s.name, s.lastname " \
              "FROM conferences AS c INNER JOIN speakers AS s " \
              "ON c.personid = s.personid;"
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql,)
        datta = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(datta):
            datta[key] = Hydrate(value)
        return datta

    def update_confernces(self, column, datta, id ):
        """"method for modify datta in bdd after connect to bdd"""
        self.choice.initialize_connection()
        self.sql = "UPDATE conf set " + column + " = %s WHERE id = %s ;"
        self.arguments = (datta, id)
        self.choice.cursor.execute(self.sql, self.arguments)
        self.choice.connection.commit()
        self.choice.close_connection()
        print("\033[31mdnew datta saved\033[0m")
