class Student:
    pass

class Marks:
    pass

student1 = Student()
student2 = Student()
marks1 = Marks()
marks2 = Marks()

print(isinstance(student1, Student))
print(isinstance(student2, Student))
print(isinstance(marks1, Marks))
print(isinstance(marks2, Marks))

print(issubclass(Student, object))
print(issubclass(Marks, object))
