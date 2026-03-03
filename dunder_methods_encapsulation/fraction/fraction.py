from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator


a = Fraction(1, 2)
b = Fraction(1, 3)
c = Fraction(2, 4)

print(a)
print(a == c)
print(a < b)

d = a + b
print(d)