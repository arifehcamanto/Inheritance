class Person:

    def __init__(self, first_name, last_name, middle_name, id , type):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.id = id
        self.type = type


    def getName(self):
        return (f'{self.last_name}, {self.first_name} {self.middle_name}.')

    def getID(self):
        return self.id

    def getType(self):
        return self.type