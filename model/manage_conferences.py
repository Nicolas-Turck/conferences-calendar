import datetime
from model.connection import *
from model.conferencesentities import *
class Managesconferences():
    def __init__(self):
        self.db = Connection()
        self.title = None
        self.summary = None
        self.date = None
        self.hour = None
        self.creation_date = datetime.date.today()

    def create_conferences(self, title, summary, date, hour, speaker):
        """method for add conferences in bdd"""
        self.db.initialize_connection()
        sql = "INSERT INTO conferences(title, summary, date, hour, " \
              "creation_date, personid) VALUES (%s, %s, %s, %s, %s, %s);"
        arguments = (title, summary, date, hour, self.creation_date, speaker,)
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_conferences(self, id):
        """method for delete conferences in bdd with this personal id"""
        self.db.initialize_connection()
        sql = "DELETE FROM conferences WHERE personid = %s;"
        arguments = (id,)
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def show_conferences(self):
        """method for display all conferences and auto with join sql"""
        sql = "SELECT speakers.name, speakers.lastname, title, date, hour, summary " \
              "FROM conferences INNER JOIN speakers " \
              "ON conferences.speaker_id = speakers.id;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,)
        datta = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(datta):
            datta[key] = Hydrate(value)
        return datta