from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except TypeError as error:
    print(f"TypeError: {error}")
