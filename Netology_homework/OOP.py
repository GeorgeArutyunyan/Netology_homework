class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return f'Grade error, grade must be from 0 to 10, your grade {grade}'
        else:
            return 'lector did not exist'

    def _average_grade(self):
        if len(self.grades) == 0:
            return f'No grades yet'
        else:
            counter = 0
            total = 0
            for key, value in self.grades.items():
                total += sum(self.grades[key])
                counter += len(self.grades[key])
            return round(total / counter, 2)

    def __str__(self):
        return f'''Name: {self.name}
Surname: {self.surname}
Average grade for homeworks: {self._average_grade()}
Courses in process: {', '.join([i for i in self.courses_in_progress])}
Finished courses: {', '.join([i for i in self.finished_courses])}'''

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._average_grade() < other._average_grade()
        return 'Comparison is not possible'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'''Name: {self.name}
Surname: {self.surname}'''


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def _average_grade(self):
        if len(self.grades) == 0:
            return f'No grades yet'
        else:
            counter = 0
            total = 0
            for key, value in self.grades.items():
                total += sum(self.grades[key])
                counter += len(self.grades[key])
            return round(total / counter, 2)

    def __str__(self):
        return f'''Name: {self.name}
Surname: {self.surname}
Average grade per lecture: {self._average_grade()}'''

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade() < other._average_grade()
        return 'Comparison is not possible'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        return f'''Name: {self.name}
Surname: {self.surname}'''


def students_average(student_list, courses_name):
    total = 0
    counter = 0
    for student in student_list:
        if courses_name in student.courses_in_progress:
            total += sum(student.grades[courses_name])
            counter += len(student.grades[courses_name])
        else:
            return f'No students in {courses_name}'
    return f'Average grade for students at {courses_name}: {round(total / counter, 2)}'


def lecturers_average(lecturer_list, courses_name):
    total = 0
    counter = 0
    for lecturer in lecturer_list:
        if courses_name in lecturer.courses_attached:
            total += sum(lecturer.grades[courses_name])
            counter += len(lecturer.grades[courses_name])
        else:
            return f'No lecturers attached on {courses_name}'
    return f'Average grade for lecturers attached at {courses_name}: {round(total / counter, 2)}'


if __name__ == '__main__':
    leroy = Reviewer('Leroy', 'Jenkins')
    tom = Reviewer('Tom', 'Riddle')
    severus = Lecturer('Severus', 'Snape')
    lupin = Lecturer('Rimus', 'Lupin')
    albus = Mentor('Albus', 'Dumbledore')
    minerva = Mentor('Minerva', 'McGonagall')
    john = Student('John', 'Snow', 'Male')
    hermione = Student('Hermione', 'Granger', 'Female')
    roland = Student('Roland', 'Deschein', 'Gunslinger')
    leroy.courses_attached += ['Python']
    tom.courses_attached += ['Python']
    severus.courses_attached += ['Python']
    lupin.courses_attached += ['Python']
    albus.courses_attached += ['Python']
    minerva.courses_attached += ['Python']
    john.courses_in_progress += ['Python']
    hermione.courses_in_progress += ['Python']
    hermione.courses_in_progress += ['Java']
    hermione.finished_courses += ['SQL']
    john.courses_in_progress += ['Java']
    john.finished_courses += ['SQL']
    john.finished_courses += ['Django']
    roland.courses_in_progress += ['Python']
    roland.courses_in_progress += ['Java']
    leroy.rate_hw(roland, 'Python', 10)
    leroy.rate_hw(roland, 'Python', 10)
    leroy.rate_hw(john, 'Python', 5)
    leroy.rate_hw(john, 'Python', 5)
    leroy.rate_hw(john, 'Python', 3)
    leroy.rate_hw(john, 'Python', 1)
    leroy.rate_hw(john, 'Python', 2)
    tom.rate_hw(hermione, 'Python', 10)
    leroy.rate_hw(hermione, 'Python', 10)
    leroy.rate_hw(hermione, 'Python', 10)
    leroy.rate_hw(hermione, 'Python', 10)
    leroy.rate_hw(hermione, 'Python', 10)
    tom.rate_hw(john, 'Python', 8)
    john.rate_hw(severus, 'Python', 8)
    john.rate_hw(severus, 'Python', 8)
    john.rate_hw(severus, 'Python', 2)
    john.rate_hw(severus, 'Python', 3)
    john.rate_hw(lupin, 'Python', 10)
    hermione.rate_hw(lupin, 'Python', 10)
    hermione.rate_hw(severus, 'Python', 10)
    print(leroy)
    print(tom)
    print(john)
    print(hermione)
    print(hermione < john)
    print(severus < lupin)
    print(albus)
    print(minerva)
    print(hermione)
    print(john)
    print(students_average(Student.student_list, 'Python'))
    print(lecturers_average(Lecturer.lecturer_list, 'Python'))
    print(john.rate_hw(severus, 'Java', 10))