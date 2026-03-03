class Matrix2x2:

    def __init__(self, a, b, c, d):
        self.data = [[a, b], [c, d]]

    def __str__(self):
        r0 = f"|{self.data[0][0]} {self.data[0][1]}|"
        r1 = f"|{self.data[1][0]} {self.data[1][1]}|"
        return f"{r0}\n{r1}"

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        return Matrix2x2(
            self.data[0][0] + other.data[0][0],
            self.data[0][1] + other.data[0][1],
            self.data[1][0] + other.data[1][0],
            self.data[1][1] + other.data[1][1]
        )

    def __getitem__(self, row):
        return self.data[row]


m1 = Matrix2x2(1, 2, 3, 4)
m2 = Matrix2x2(5, 6, 7, 8)

print(m1)
print(m1 == Matrix2x2(1, 2, 3, 4))
print(m1[0])
print(m1[1][0])

m3 = m1 + m2
print(m3)