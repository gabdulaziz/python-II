import re

class Password:
    def __init__(self, password: str):
        self._validate(password)
        self._password = password

    def _validate(self, password: str):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[0-9]", password):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*]", password):
            raise ValueError("Password must contain at least one special character (!@#$%^&*)")

    def get_strength(self):
        length = len(self._password)
        if length >= 12:
            return "Strong"
        else:
            return "Medium"

    def check_password(self, input_password: str):
        return input_password == self._password

    def change_password(self, old_password: str, new_password: str):
        if not self.check_password(old_password):
            raise ValueError("Old password does not match")
        self._validate(new_password)
        self._password = new_password


# Example Usage
password = Password("MyP@ssw0rd123")
print(password.get_strength())  # Strong
print(password.check_password("MyP@ssw0rd123"))  # True
print(password.check_password("wrong"))          # False

password.change_password("MyP@ssw0rd123", "NewP@ss2024!")
print(password.check_password("NewP@ss2024!"))   # True

try:
    weak_password = Password("123")
except ValueError as e:
    print(e)  # Password must be at least 8 characters long

medium = Password("Passw0rd!")
print(medium.get_strength())  # Medium
strong = Password("MyStr0ng!Pass")
print(strong.get_strength())  # Strong