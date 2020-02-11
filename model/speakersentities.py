from model.manage_speakers import*
class Hydrate():
    """class for hydrate attribut before print them"""
    def __init__(self, datta = False):
        """method for initialise atrributs """
        self.name= None
        self.lastname = None
        self.job = None
        self.hydrate(datta)

    def hydrate(self, datta):
        """method for add elem in attribus"""
        for key_name, value_name in datta.items():
            if hasattr(self, key_name):
                setattr(self, key_name, value_name)

    def __str__(self):
        """method for display elem of city"""
        return "name: {}, lastname: {}, job: {}  " .format(self.name, self.lastname, self.job,)