class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = self.name[0] + self.last_name + str(self.birth_year)

    def get_id(self):
        print(self.id)


name_input = input()
last_name_input = input()
year_input = input()
student_ivan = Student(name_input, last_name_input, year_input)
student_ivan.get_id()
