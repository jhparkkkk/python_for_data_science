from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

try:
    student = Student(name="Edward", surname="agle", id="toto")
except TypeError as error:
    print(f"TypeError: {error}")

try:
    student = Student(name="Edward", surname="agle", active=True)
except TypeError as error:
    print(f"TypeError: {error}")

try:
    student = Student(name="Edward", surname="agle", plop="plop")
except TypeError as error:
    print(f"TypeError: {error}")

try:
    student = Student(name=2313, surname="agle")
except TypeError as error:
    print(f"TypeError: {error}")

try:
    student = Student(name="toto", surname=True)
except TypeError as error:
    print(f"TypeError: {error}")
