def get_student(list_of_students):
    for student in list_of_students:
        yield student

students_gen = get_student(["Ali", "Vali", "Zuhra"])
print(next(students_gen))
print(next(students_gen))
print(next(students_gen))
