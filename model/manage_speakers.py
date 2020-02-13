from controller.speakersentities import *
from model.connection import *
import os
import time
class Managespeakers():
    """class for manage speakers create read delete CRUD """
    def __init__(self):
        self.status = True
        self.db = Connection()
        self.sql = ""
        self.arguments = ""
    def create_speakers(self, name, lastname, description, job):
        """method for add speakers in bdd"""
        self.db.initialize_connection()
        self.sql = "INSERT INTO speakers(name, lastname, description, job, status) VALUES (%s, %s, %s, %s, %s);"
        self.arguments = (name, lastname, description, job, self.status)
        self.db.cursor.execute(self.sql, self.arguments)
        self.db.connection.commit()
        self.db.close_connection()
        print("\033[31mnew speakers create\033[0m")
        return

    def delete_speakers(self, id):
        """method for delete speaker in bdd with this personal id"""
        self.db.initialize_connection()
        self.sql = "DELETE  FROM speakers " \
              "WHERE personid = %s;"
        self.arguments = (id,)
        self.db.cursor.execute(self.sql, self.arguments)
        self.db.connection.commit()
        self.db.close_connection()
        print("\033[31mspeakers deletted\033[0m")

    def show_speakers(self):
        """method for display all speakers if status is True"""
        self.sql = "SELECT * FROM speakers WHERE status = True;"
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql,)
        datta = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(datta):
            datta[key] = Hydrate(value)
        return datta





