

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        text = "Name={0} ({1}) : ${2}".format(self.name, self.year, self.cost)
        return text

    def get_age(self):
        """Add amount to the car's fuel."""
        age = 2018 - self.year
        return age

    def is_vintage(self):

        if self.get_age() >= 50:
            return True
        else:
            return False
