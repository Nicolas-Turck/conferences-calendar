import psycopg2
import psycopg2.extras

class Connection():
    """class for connect and close the database
    and addinf user port and database in attributes of classe"""
    USER = "eder"
    PORT = "5432"
    DATABASE = "user_account"

    def __init__(self):
        """"""
        self.connection = None
        self.cursor = None

    def initialize_connection(self):
        """method for initialyse the connection to the database """
        try:
            self.connection = psycopg2.connect(user = Connection.USER, port = Connection.PORT, database = Connection.DATABASE)
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        except (Exception, psycopg2.Error) as error:
            print("error no connecting PostgreSQL", error)

    def close_connection(self):
        """method for closed the database"""
        if(self.connection):
            self.cursor.close()
            self.connection.close()