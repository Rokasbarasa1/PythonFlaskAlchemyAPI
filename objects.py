class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

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
        self.students = []
        self.is_active = True

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

class Pet:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def show(self):
        print(f"I am {self.name} and i am {self.age} yaers old")

    def speak(self):
        print("I dont know what i say")
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def show(self):
        print(f"I am {self.name} and i am {self.age} yaers old and i am {self.color}")

    def speak(self):
        print("Meow")

class DogSecond(Pet):
    def speak(self):
        print("Bark")

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

class Math:
    @staticmethod
    def add5(x):
        return x+5

    @staticmethod
    def pr(x):
        print("run")





































