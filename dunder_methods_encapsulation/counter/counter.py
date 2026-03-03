class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def __add__(self, other):
        return Counter(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f"Counter({self.value})"

    def __bool__(self):
        return self.value != 0


c1 = Counter()
c1.increment()
c1.increment()
c1.increment()
print(c1)

c2 = Counter(7)
c3 = c1 + c2
print(c3)

print(c1 == Counter(3))

empty = Counter()
if not empty:
    print("Counter is zero!")