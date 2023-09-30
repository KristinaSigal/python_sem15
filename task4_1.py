"""
1. Напишите функцию для транспонирования матрицы .
"""


def matrix_trans(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20]
          ]

print(f'исходная матрица:')
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f'{matrix[i][j]:>{3}}', end=",")
    print()

trans_matrix = matrix_trans(matrix)
# print(f'транспонированная матрица: {matrix_trans(matrix)}')
print('транспонированная матрица:')
for i in range(len(trans_matrix)):
    for j in range(len(trans_matrix[0])):
        print(f'{trans_matrix[i][j]:>{3}}', end=",")
    print()

