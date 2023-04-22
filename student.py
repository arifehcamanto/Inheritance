from  person import Person


class Student(Person):

    def __init__(self, first_name, last_name, middle_name, id , type, section, year, course):
        super().__init__(first_name, last_name, middle_name, id, type)
        self.section = section
        self.year = year
        self.course = course

    def get_yr_course_sec(self):
            return (f'{self.year}/{self.course}/{self.section}')


class Grade(Student):

    def __init__(self, english, math, filipino, science ):
        self.english = english
        self.math = math
        self.filipino = filipino
        self.science = science

    def get_average(self):
        sum = self.math + self.english + self.filipino + self.science
        return sum / 4


