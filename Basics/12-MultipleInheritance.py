class Teacher:
    def action(self):
        print('I can teach')

class Student:
    def action(self):
        print('I can code')

class Youtuber:
    def action(self):
        print('I can create content')

class Person(Teacher, Student, Youtuber):
    def action(self):
        Teacher.action(self)
        Student.action(self)
        Youtuber.action(self)

obj = Person()
obj.action()
