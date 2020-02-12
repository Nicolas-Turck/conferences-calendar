from model.speakersentities import *
from model.connection import *
class Managespeakers():
    """class for manage speakers """
    def __init__(self):
        self.status = True
        self.db = Connection()

    def create_speakers(self, name, lastname, description, job):
        """method for add speakers in bdd"""
        self.db.initialize_connection()
        sql = "INSERT INTO speakers(name, lastname, description, job, status) VALUES (%s, %s, %s, %s, %s);"
        arguments = (name, lastname, description, job, self.status)
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_speakers(self, id):
        """method for delete speaker in bdd with this personal id"""
        self.db.initialize_connection()
        sql = "DELETE  FROM speakers " \
              "WHERE personid = %s;"
        arguments = (id,)
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def show_speakers(self):
        """method for display all speakers"""
        sql = "SELECT * FROM speakers WHERE status = True;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,)
        datta = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(datta):
            datta[key] = Hydrate(value)
        return datta





