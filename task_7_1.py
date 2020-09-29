class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        new = []
        for i in range(len(self.matrix)):
            a = str(self.matrix[i])
            a_1 = a.replace(",", "   ")
            a_2 = a_1.replace("[", "")
            a_3 = a_2.replace("]", "")
            new.append(a_3)
        new = str(new)
        new_1 = new.replace(",", "\n")
        new_2 = new_1.replace("[", "")
        new_3 = new_2.replace("]", "")
        return new_3

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return 'матрицы разного размера складывать нельзя'
        new = []
        new_i = None
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return 'матрицы разного размера складывать нельзя'
            new.append(new_i)
            new_i = []
            for j in range(len(self.matrix[i])):
                new_i.append(self.matrix[i][j] + other.matrix[i][j])
        new.append(new_i)
        new.pop(0)
        return Matrix(new)


m_1 = Matrix([[2, 2], [5, 6], [4, 1]])
m_2 = Matrix([[4, 8], [6, 11], [0, -1]])
print(type(m_2.matrix))
print(m_1 + m_2)
