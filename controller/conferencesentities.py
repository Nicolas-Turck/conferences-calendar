from model.manage_conferences import*
class Hydrate():
    """class for hydrate attribut before print them"""
    def __init__(self, datta = False):
        """method for initialise atrributs """
        self.name= None
        self.lastname = None
        self.title = None
        self.date = None
        self.hour = None
        self.summary = None
        self.hydrate(datta)

    def hydrate(self, datta):
        """method for add elem in attribus"""
        for key_name, value_name in datta.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)

    def __str__(self):
        """method for display elem of two tables in bdd"""
        return "\033[34mspeakers {}, {}\ntitle: {}\ndate: {}, hour: {}\nsummary: {}\033[0m" \
            .format(self.name, self.lastname, self.title, self.date, self.hour, self.summary)