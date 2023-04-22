from person import Person

class Teacher(Person):

    def __init__(self, first_name, last_name, middle_name, id, type, department, position):
        super().__init__(first_name, last_name, middle_name, id, type)
        self.department = department
        self.position = position


    def get_dep_pos(self):
        return (f'{self.department} {self.position}')



class Load(Teacher):

    def __init__(self, subject):
        self.subject = subject

    def get_sub(self):
        return self.subject

