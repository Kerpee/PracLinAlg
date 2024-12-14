import numpy as np
import matplotlib.pyplot as plt

# Функция для построения матрицы с заданными собственными числами
def construct_matrix(eigenvalues):
    if len(eigenvalues) == 2:
        trace = sum(eigenvalues)
        determinant = np.prod(eigenvalues)
        return np.array([[trace, -determinant], [1, 0]])
    elif len(set(eigenvalues)) == 1:
        return np.array([[eigenvalues[0], 1], [0, eigenvalues[0]]])

# Визуализация собственных чисел на комплексной плоскости
def plot_eigenvalues(eigenvalues, label):
    for eig in eigenvalues:

        # Создаём векторы
        vector1 = np.array([0, eig])
        origin = np.array([0, 0])  # начало координат


        plt.plot(vector1.real, vector1.imag, 'o', label=label)

# Функция для визуализации динамической системы
def plot_trajectories(A, title):
    # Задаем сетку начальных условий
    x1 = np.linspace(-2, 2, 10)
    x2 = np.linspace(-2, 2, 10)
    initial_conditions = np.array([[x, y] for x in x1 for y in x2])

    # Количество шагов симуляции
    steps = 20

    # Построение траекторий
    plt.figure(figsize=(6, 6))
    for x0 in initial_conditions:
        trajectory = [x0]
        for _ in range(steps):
            x_next = A @ trajectory[-1]
            trajectory.append(x_next)
        trajectory = np.array(trajectory)
        plt.plot(trajectory[:, 0], trajectory[:, 1], '-o', markersize=2)

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title(title)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Пункты задания 1-5
matrices = []
labels = []

eigenvalues_list = [
    [-1,-1],
    [-1/np.sqrt(2) + 1j/np.sqrt(2), -1/np.sqrt(2) - 1j/np.sqrt(2)],
    [1j, -1j],
    [1/np.sqrt(2) + 1j/np.sqrt(2), 1/np.sqrt(2) - 1j/np.sqrt(2)],
    [1,1],
    [0,0]
]

for i, eigenvalues in enumerate(eigenvalues_list):
    matrix = construct_matrix(eigenvalues)
    matrices.append(matrix)
    labels.append(f"ℓ_{i+1}")
    plot_eigenvalues(eigenvalues, label=f"Case {i+1}")

# Пункты 6-11 (умножение на константы c и d)
constants = [0.5, 2]  # Примеры c < 1 и d > 1
for const_idx, constant in enumerate(constants):
    for i, eigenvalues in enumerate(eigenvalues_list[:-1]):  # Исключая последний случай (нулевые собственные числа)
        scaled_eigenvalues = [constant * eig for eig in eigenvalues]
        matrix = construct_matrix(scaled_eigenvalues)




        matrices.append(matrix)
        labels.append(f"Case {i+1}, constant {constant}")
        plot_eigenvalues(scaled_eigenvalues, label=f"Case {i+1}, const {constant}")

# Отображение собственных чисел на комплексной плоскости
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Eigenvalues on Complex Plane')
plt.xlabel('Re')
plt.ylabel('Im')
plt.legend()
plt.show()

# Построение траекторий для каждой матрицы
for label, matrix in zip(labels, matrices):
    print(f"Matrix for {label}:\n{matrix}\n")
    plot_trajectories(matrix, title=f"Trajectories for {label}")
