class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.student = []

    def add_students(self, student):
        if len(self.student) < self.max_students:
            self.student.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.student:
            value += student.get_grade()

        return value / len(self.student)


s1 = Student("Ajay", 19, 93)
s2 = Student("Rahul", 19, 81)
s3 = Student("Vikram", 18, 76)

course = Course('Science', 2)
course.add_students(s1)
course.add_students(s2)
print(course.get_average_grade())
