class Clock:
    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute
        self._normalize()

    def _normalize(self):
        total_minutes = self.hour * 60 + self.minute
        total_minutes %= 24 * 60
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

    def add_minutes(self, minutes: int):
        self.minute += minutes
        self._normalize()

    def subtract_minutes(self, minutes: int):
        self.minute -= minutes
        self._normalize()

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return False
        return self.hour == other.hour and self.minute == other.minute


# Example Usage
clock1 = Clock(11, 30)
clock2 = Clock(11, 30)
print(str(clock1))       # 11:30
print(repr(clock1))      # Clock(11, 30)
print(clock1 == clock2)  # True

clock3 = Clock(12, 0)
print(clock1 == clock3)  # False

clock1.add_minutes(60)
print(clock1)            # 12:30
clock1.subtract_minutes(120)
print(clock1)            # 10:30