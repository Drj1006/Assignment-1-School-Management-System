from Course import Course


class Student:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self._password = password
        self.course = Course()

    def get_password(self):
        return self._password

    def write_to_file(self):
        with open('Student.txt', 'a') as file:
            file.write(f" Students_name = {self.name} || Students_roll = {self.roll}  || Password = {self._password} || Enrolled_courses = {', ' .join(self.course.get_courses())}\n")
