class Course:
    def __init__(self):
        self.courses = []

    def add_courses(self, name):
        self.courses.append(name)

    def get_courses(self):
        return self.courses