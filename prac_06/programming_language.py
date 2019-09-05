

class ProgrammingLanguage():

    def __init__(self, field, typing, reflection, year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        text = "{0}, {1} Typing, Reflection={2}, First appeared in {3}".format(self.field, self.typing, self.reflection, self.year)
        return text

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False



