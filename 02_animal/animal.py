class Animal:
    def __init__(self, name, species):  # noqa: ANN204
        self.name = name
        self.species = species


def make_sound(self):
    print(f"{self.name} makes a sound!")

    def __repr__(self):
        return f"Animal(name='{self.name}', species='{self.species}')"


dog = Animal("Buddy", "Dog")
print(dog)

dog.make_sound()  # pyright: ignore[reportAttributeAccessIssue]
