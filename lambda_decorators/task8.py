def check_auth(func):
    def wrapper(*args, **kwargs):
        print("Checking access to the Gradebook...")
        return func(*args, **kwargs)
    return wrapper

@check_auth
def view_grades():
    print("Viewing grades...")

view_grades()