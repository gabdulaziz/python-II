class Matrix:
    def __init__(self, matrix_string):
        self._data = [
            list(map(int, row.split()))
            for row in matrix_string.strip().split('\n')
        ]

    def row(self, index):
        return self._data[index - 1][:]

    def column(self, index):
        return [row[index - 1] for row in self._data]

    def get_rows(self):
        return [r[:] for r in self._data]

    def get_columns(self):
        return [[row[i] for row in self._data] for i in range(len(self._data[0]))]


# Example Usage
matrix_string = "9 8 7\n5 3 2\n6 6 7"
matrix = Matrix(matrix_string)

print(matrix.row(1))       # [9, 8, 7]
print(matrix.column(2))    # [8, 3, 6]
print(matrix.get_rows())    # [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
print(matrix.get_columns()) # [[9, 5, 6], [8, 3, 6], [7, 2, 7]]