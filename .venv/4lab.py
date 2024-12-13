import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления траектории системы
def simulate_continuous_system(A, x0, t_max, dt):
    t_values = np.arange(0, t_max, dt)
    x_values = [x0]
    for _ in t_values[1:]:
        x_next = x_values[-1] + dt * (A @ x_values[-1])
        x_values.append(x_next)
    return t_values, np.array(x_values)

matrices = {
    "Случай 1: Система асимптотически устойчива": np.array([[-1, 0], [0, -2]]),
    "Случай 2: Система неустойчива с вырожденной матрицей собственных векторов": np.array([[1, 1], [0, 1]]),
    "Случай 3: Система неустойчива, x(t) стремится к 0 для определённых начальных условий": np.array([[-1, 2], [0, 1]]),
    "Случай 4: Система асимптотически устойчива с комплексными собственными числами": np.array([[-1, -2], [2, -1]]),
    "Случай 5: Неустойчивая система с теми же комплексными собственными числами": np.array([[1, -2], [2, 1]]),
    "Случай 6: Система  устойчива с комплексными собственными числами": np.array([[0, -2], [2, 0]])
}

initial_conditions = {}
for title, A in matrices.items():
    eigenvalues, eigenvectors = np.linalg.eig(A)
    v1 = eigenvectors[:, 0]
    v2 = eigenvectors[:, 1]
    v1 = v1 / np.linalg.norm(v1)
    v2 = v2 / np.linalg.norm(v2)
    additional_conditions = [
        np.array([1, 1]),
        np.array([-1, 1]),
        np.array([1, -1])
    ]
    initial_conditions[title] = [v1, v2] + additional_conditions
t_max = 5
dt = 0.01

for title, A in matrices.items():
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(f"{title}\nMatrix A:\n{A}\nEigenvalues: {eigenvalues}\nEigenvectors:\n{eigenvectors}\n")

    plt.figure(figsize=(12, 8))
    for x0 in initial_conditions[title]:
        t_values, trajectories = simulate_continuous_system(A, x0, t_max, dt)
        x1_values, x2_values = trajectories[:, 0], trajectories[:, 1]

        plt.subplot(2, 1, 1)
        plt.plot(t_values, x1_values, label=f"$x_1(t)$, $x_0$={x0}")
        plt.plot(t_values, x2_values, label=f"$x_2(t)$, $x_0$={x0}", linestyle="--")
        plt.title(f"{title}")
        plt.xlabel("t")
        plt.legend()
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(x1_values, x2_values, label=f"$x_0$={x0}")
        plt.title(f"Фазовая траектория для {title}")
        plt.xlabel("$x_1$")
        plt.ylabel("$x_2$")
        plt.legend()
        plt.grid(True)

    plt.tight_layout()
    plt.show()

