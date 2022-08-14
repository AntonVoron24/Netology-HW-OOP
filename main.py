import numpy


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mean(self, grades):
        self.mean_grade = round(numpy.mean([grades[key] for key in grades]), 2)
        return self.mean_grade

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.mean(self.grades)}\n' \
              f'Курсы в процессе изучения: {(", ".join(self.courses_in_progress))}\n' \
              f'Завершенные курсы: {(", ".join(self.finished_courses))}'

        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не студент')
            return
        return self.mean(self.grades) < self.mean(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mean(self, grades):
        if grades:
            self.mean_grade = round(numpy.mean([grades[key] for key in grades]), 2)
            return self.mean_grade
        else:
            return 'Ошибка'

    def __str__(self):

        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.mean(self.grades)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other} не лектор')
            return
        return self.mean(self.grades) < self.mean(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


germiona = Student('Гермиона', 'Грейнджер', 'w')
germiona.courses_in_progress += ['Зельеварение']
germiona.courses_in_progress += ['Трансфигурация']
germiona.finished_courses += ['История магии']

ron = Student('Рон', 'Уизли', 'm')
ron.courses_in_progress += ['Зельеварение']
ron.courses_in_progress += ['Трансфигурация']
ron.finished_courses += ['История магии']

severus = Reviewer('Северус', 'Снегг')
severus.courses_attached += ['Зельеварение']
severus.courses_attached += ['Трансфигурация']

rimus = Reviewer('Римус', 'Люпин')
severus.courses_attached += ['Зельеварение']
severus.courses_attached += ['Трансфигурация']

dambldor = Lecturer('Альбус', 'Дамблдор')
dambldor.courses_attached += ['Зельеварение']

dolores = Lecturer('Долорес', 'Амбридж')
dolores.courses_attached += ['Зельеварение']

germiona.rate_hw(dambldor, 'Зельеварение', 10)
germiona.rate_hw(dolores, 'Зельеварение', 5)

ron.rate_hw(dambldor, 'Зельеварение', 8)
ron.rate_hw(dolores, 'Зельеварение', 6)

severus.rate_hw(germiona, 'Зельеварение', 7)
severus.rate_hw(ron, 'Зельеварение', 2)

rimus.rate_hw(germiona, 'Зельеварение', 10)
rimus.rate_hw(ron, 'Зельеварение', 4)


def mean_courses(student, course_name):
    course_grades = []
    for i in student:
        course_grades.append(i.grades[course_name])
    return numpy.mean(course_grades)


def mean_lectures(lecturers, course_name):
    course_grades = []
    for i in lecturers:
        course_grades.append(i.grades[course_name])
    return numpy.mean(course_grades)


print(germiona, ron, sep='\n')
print(severus, rimus, sep='\n')
print(dambldor, dolores, sep='\n')
print(dolores > dambldor)
print(ron < germiona)
print(f'Средняя оценка студентов по курсу "Зельеварение": {mean_courses([germiona, ron], "Зельеварение")}')
print(f'Средняя оценка лекторов по курсу "Зельеварение": {mean_lectures([dolores, dambldor], "Зельеварение")}')
