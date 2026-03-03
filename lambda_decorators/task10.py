def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*** {result} ***"
    return wrapper

@make_bold
def student_note():
    return "Ali is a top student"

print(student_note())