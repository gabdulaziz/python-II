def calculate_average(student_name, *grades):
    avg = sum(grades) / len(grades) if grades else 0
    return f"Student {student_name} has an average grade of {avg}"

print(calculate_average("Ali", 80, 90, 75))
