import numpy as np


def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n)


def cyclic123_array(n):
    """2. Генерирует numpy массив длины  3𝑛 , заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.full((n, 3), [1, 2, 3]).flatten()


def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, 2*n, 2)


def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    one = np.ones((n, n))
    one[1:n-1, 1:n-1] = 0
    return one


def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    ar = np.zeros((n, n))
    ar[::2, ::2] = 1
    ar[1::2, 1::2] = 1
    return ar


def matrix_with_sum_index(n):
    """6. Создаёт 𝑛 × 𝑛  матрицу с (𝑖,𝑗)-элементами равным 𝑖+𝑗."""
    rows = np.arange(n).reshape(n, 1)
    cols = np.arange(n).reshape(1, n)
    matrix = rows + cols
    return matrix


def cos_sin_as_two_rows(a, b, dx):
    """7. Вычислите $cos(x)$ и $sin(x)$ на интервале [a, b) с шагом dx, 
    а затем объедините оба массива чисел как строки в один массив. """
    return np.vstack((np.cos(np.arange(a, b, dx)), np.sin(np.arange(a, b, dx))))


def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    return np.mean(A), np.sum(A, axis=0), np.sum(A, axis=1)


def sort_array_by_column(A, j):
    """ 9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    return A[np.argsort(A[:, j])]


def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a, b] с шагом dx 3-мя методами:  
    method == 'rectangular' - методом прямоугольника   
    method == 'trapezoidal' - методом трапеций   
    method == 'simpson' - методом Симпсона  
    """
    x = np.arange(a, b, dx)
    if x[-1] < b:
        x = np.hstack((x, b))

    if method == 'rectangular':
        integ = np.sum(f(x[:-1]) * dx)

    elif method == 'trapezoidal':
        integ = ((f(a) + f(b))/2) * dx + np.sum(f(x[1:(len(x) - 1)]) * dx)

    elif method == 'simpson':
        integ = (dx/3) * (f(a) + f(b) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[2:-2:2])))

    else:
        raise 'MethodError'

    return integ


f1 = lambda x: (x**2 + 3) / (x - 2)
print(compute_integral(3, 4, f1, 0.001, method='rectangular'))