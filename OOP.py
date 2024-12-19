class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def medium_grade_student(self):
        list_grade = self.grades.values()
        sum_grade = 0
        for grade_student in list_grade:
            sum_grade += sum(grade_student)
            return sum_grade / len(grade_student)

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other_student):
        if isinstance(other_student, Student):
            return self.medium_grade_student() < other_student.medium_grade_student()

    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: '
            f'{self.medium_grade_student()}\nКурсы в процессе обучения: {",".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {",".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def medium_grade(self):
        list_grade = self.grades.values()
        sum_grade = 0
        for grade_lecturer in list_grade:
            sum_grade += sum(grade_lecturer)
            return sum_grade / len(grade_lecturer)

    def __lt__(self, other_lecturer):
        if isinstance(other_lecturer, Lecturer):
            return self.medium_grade() < other_lecturer.medium_grade()

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции:  {self.medium_grade()}')


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Вася', 'Пупкин', 'мужской')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Design']
student_2 = Student('Саша', 'Грей', 'женский')
student_2.courses_in_progress += ['Design']
student_2.finished_courses += ['Python']

lecturer_1 = Lecturer('Димка', 'Медведев')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Бориска', 'Моисеев')
lecturer_2.courses_attached += ['Design']

student_1.rate_hw(lecturer_1, 'Python', 7)
student_2.rate_hw(lecturer_2, 'Design', 5)

reviewer_1 = Reviewer('Анна', 'Каренина')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Саша', 'Белый')
reviewer_2.courses_attached += ['Design']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Design', 6)

print(student_1)
print(student_2)
print("___________\n")
print(reviewer_1)
print(reviewer_2)
print("___________\n")
print(lecturer_1)
print(lecturer_2)
print("___________\n")
print(f'Средняя оценка студентов: {(student_1.medium_grade_student() + student_2.medium_grade_student()) / 2}')
print(f'Средняя оценка лекторов: {(lecturer_1.medium_grade() + lecturer_2.medium_grade()) / 2}')
print("___________\n")
print(student_2.__lt__(student_1))
print(lecturer_1.__lt__(lecturer_2))
print("___________\n")

student_list = [student_1, student_2]


def medium_grade_student(student_list, course):
    sum_grade = 0
    count_grade = 0
    for student in student_list:
        if course in student.grades:
            sum_grade += sum(student.grades[course])
            count_grade += len(student.grades[course])
    return sum_grade / count_grade


print(medium_grade_student(student_list, 'Python'))

lecturer_list = [lecturer_1, lecturer_2]


def medium_grade_lecturer(lecturer_list, course):
    sum_grade = 0
    count_grade = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            sum_grade += sum(lecturer.grades[course])
            count_grade += len(lecturer.grades[course])
    return sum_grade / count_grade


print(medium_grade_lecturer(lecturer_list, 'Design'))