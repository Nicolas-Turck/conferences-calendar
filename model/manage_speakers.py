
from model.connection import *
class Managespeakers():
    def __init__(self, name, lastname, description, job):
        self.name = name
        self.lastname = lastname
        self.description = description
        self.job = job
        self.status = True
        self.db = Connection()

    def create_speakers(self):
        self.db.initialize_connection()
        sql = "INSERT INTO speakers(name, lastname, description, job, status) VALUES (%s, %s, %s, %s, %s);"
        arguments = (self.name, self.lastname,  self.description, self.job, self.status)
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()




