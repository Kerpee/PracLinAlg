import numpy as np
import matplotlib.pyplot as plt

# Числа a, b, c, d
a, b, c, d = 3, 5, 4, 2

# Задаем вершины прямоугольника
rectangle = np.array([[1, 1], [1, -1], [-1, -1], [-1, 1], [1, 1]])

# 1 задание
M_reflection = np.array([[-8/10, 6/10], [6/10, 8/10]])

# Применение отражения к вершинам прямоугольника
rect_reflection = rectangle @ M_reflection.T

# Визуализация
plt.figure(figsize=(6, 6))
plt.plot(rectangle[:, 0], rectangle[:, 1], 'b-', label="Прямоугольник")
plt.plot(rect_reflection[:, 0], rect_reflection[:, 1], 'r-', label="Отражение относительно y = 3x")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.axline((0, 0), slope=3, color='green', linestyle='--', label="y = 3x")
plt.grid(True)
plt.legend()
plt.title("Отражение относительно y=3x")
plt.show()

M_projection = np.array([[1/26, 5/26], [5/26, 25/26]])

# Применение проекции к вершинам прямоугольника
rect_projection = rectangle @ M_projection.T

# Визуализация
plt.figure(figsize=(6, 6))
plt.plot(rectangle[:, 0], rectangle[:, 1], 'b-', label="Прямоугольник")
plt.plot(rect_projection[:, 0], rect_projection[:, 1], 'r-', label="Отображение в прямую y = 5x")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.axline((0, 0), slope=5, color='green', linestyle='--', label="y = 5x")
plt.grid(True)
plt.legend()
plt.title("Отображение в прямую y = 5x")
plt.show()



