# HW 13.1

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Record Book: {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Group Number: {self.number}\nStudents:\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)


assert str(gr.find_student('Jobs')) == str(st1)
assert gr.find_student('Jobs2') is None
assert isinstance(gr.find_student('Jobs'), Student)

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')

# HW 13.2

class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError("Initial value must be within the range of min and max values")
        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError("Maximum value must be greater than the minimum value")
        self.max_value = max_max

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("Minimum value must be less than the maximum value")
        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Reached maximum")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Reached minimum")
        self.current -= 1

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10
try:
    counter.step_up()
except ValueError as e:
    print(e)
assert counter.get_current() == 10

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7
try:
    counter.step_down()
except ValueError as e:
    print(e)
assert counter.get_current() == 7

# HW 14.1

class TooManyStudentsException(Exception):
    def __init__(self, message="Can't add more than 10 students to a group :("):
        self.message = message
        super().__init__(self.message)


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsException()
        self.students.append(student)

    def __str__(self):
        return ', '.join(self.students)


group = Group()

try:
    for i in range(11):
        group.add_student(f"Student {i + 1}")
except TooManyStudentsException as e:
    print(e)


