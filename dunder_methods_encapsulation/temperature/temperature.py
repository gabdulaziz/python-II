class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __add__(self, other):
        return Temperature(self.celsius + other.celsius)


t1 = Temperature(25)
t2 = Temperature(30)
t3 = Temperature(25)

print(t1)
print(t1 == t3)
print(t1 < t2)

t4 = t1 + t2
print(t4)

print(sorted([t2, t1, Temperature(10)]))