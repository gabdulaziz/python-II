# Base Animal class
class Animal:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def move(self):
        raise NotImplementedError("Move method should be implemented by subclasses.")

    def make_sound(self):
        raise NotImplementedError("make_sound method should be implemented by subclasses.")


# Dog class
class Dog(Animal):
    def __init__(self, name: str, species: str, breed: str):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

    def move(self):
        return "Running on four legs"

    # Additional methods
    def bark(self):
        print(f"{self.name} is barking loudly!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")

    def wag_tail(self):
        print(f"{self.name} is wagging its tail.")


# Cat class
class Cat(Animal):
    def __init__(self, name: str, species: str, coat_color: str):
        super().__init__(name, species)
        self.coat_color = coat_color

    def make_sound(self):
        return "Meow! Meow!"

    def move(self):
        return "Stalking silently"

    # Additional methods
    def meow(self):
        print(f"{self.name} is meowing.")

    def purr(self):
        print(f"{self.name} is purring contentedly")

    def climb(self):
        print(f"{self.name} is climbing up the tree")


# Bird class
class Bird(Animal):
    def __init__(self, name: str, species: str, wingspan: float):
        super().__init__(name, species)
        self.wingspan = wingspan

    def make_sound(self):
        return "Tweet! Tweet!"

    def move(self):
        return "Flying with wings"

    # Additional methods
    def fly(self):
        print(f"{self.name} is flying gracefully")

    def sing(self):
        print(f"{self.name} is singing a beautiful song")

    def build_nest(self):
        print(f"{self.name} is building a nest")


# Example Usage
if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever", "Golden Retriever")
    cat = Cat("Whiskers", "Domestic Cat", "Orange")
    bird = Bird("Tweety", "Canary", 0.15)

    # Dog info
    print(f"Dog: {dog.name} ({dog.species})")
    print(f"Breed: {dog.breed}")
    print(f"Sound: {dog.make_sound()}")
    print(f"Movement: {dog.move()}")
    dog.bark()
    dog.fetch()

    # Cat info
    print(f"\nCat: {cat.name} ({cat.species})")
    print(f"Color: {cat.coat_color}")
    print(f"Sound: {cat.make_sound()}")
    print(f"Movement: {cat.move()}")
    cat.purr()
    cat.climb()

    # Bird info
    print(f"\nBird: {bird.name} ({bird.species})")
    print(f"Wingspan: {bird.wingspan}m")
    print(f"Sound: {bird.make_sound()}")
    print(f"Movement: {bird.move()}")
    bird.fly()
    bird.sing()

    # Demonstrate polymorphism
    animals = [dog, cat, bird]
    print("\nAll animals making sounds:")
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")

    print("\nAll animals moving:")
    for animal in animals:
        print(f"{animal.name}: {animal.move()}")