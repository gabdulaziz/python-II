class Counter:
    def __init__(self, min_value=0, max_value=100):
        if min_value >= max_value:
            raise ValueError("min_value must be less than max_value")
        self._min = min_value
        self._max = max_value
        self._count = self._min
        self.history = []

    def increment(self, step=1):
        if step < 0:
            raise ValueError("Step must be positive")
        self._count += step
        if self._count > self._max:
            self._count = self._max
        self.history.append(f"increment({step})")

    def decrement(self, step=1):
        if step < 0:
            raise ValueError("Step must be positive")
        self._count -= step
        if self._count < self._min:
            self._count = self._min
        self.history.append(f"decrement({step})")

    def reset(self):
        self._count = self._min
        self.history.append("reset()")

    def get_value(self):
        return self._count

    def get_is_at_min(self):
        return self._count == self._min

    def get_is_at_max(self):
        return self._count == self._max

    def __str__(self):
        return f"Counter: {self._count}/{self._max} ({self._min}-{self._max})"


# Example Usage
counter = Counter()
print(counter)
print(counter.get_value())
print(counter.get_is_at_min())
print(counter.get_is_at_max())

counter.increment()
print(counter.get_value())
counter.increment(5)
print(counter.get_value())

counter.decrement()
print(counter.get_value())
counter.decrement(3)
print(counter.get_value())

counter.reset()
print(counter.get_value())

game_counter = Counter(min_value=1, max_value=10)
print(game_counter.get_value())
game_counter.increment(15)
print(game_counter.get_value())
print(game_counter.get_is_at_max())

game_counter.decrement(20)
print(game_counter.get_value())

try:
    bad_counter = Counter(min_value=10, max_value=5)
except ValueError as e:
    print(e)

print("Operation history:", counter.history)