import numpy as np
import matplotlib.pyplot as plt

# Числа a, b, c, d
a, b, c, d = 3, 5, 4, 2

# Задаем вершины прямоугольника
fig = np.array([[1, 2], [3, -1], [-2, -2],[-2,1], [1, 2]])

# 1 задание
M_reflection = np.array([[-8/10, 6/10], [6/10, 8/10]])
rect_reflection = fig @ M_reflection.T

plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="")
plt.plot(rect_reflection[:, 0], rect_reflection[:, 1], 'r-', label="Отражение относительно y = 3x")
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.axline((0, 0), slope=3, color='green', linestyle='--', label="y = 3x")
plt.grid(True)
plt.legend()
plt.title("Отражение относительно y=3x")
#plt.show()

M_projection = np.array([[1/26, 5/26], [5/26, 25/26]])

rect_projection = fig @ M_projection.T

# Визуализация
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(rect_projection[:, 0], rect_projection[:, 1], 'r-', label="Отображение в прямую y = 5x")
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.axline((0, 0), slope=5, color='green', linestyle='--', label="y = 5x")
plt.grid(True)
plt.legend()
plt.title("Отображение в прямую y = 5x")
#plt.show()
# 3 задание
theta=40
M_rotation = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
quad_rotation = fig @ M_rotation.T
print(quad_rotation)
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(quad_rotation[:, 0], quad_rotation[:, 1], 'r-', label="Поворот на 40 градусов")
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.grid(True)
plt.legend()
plt.title("Поворот на 40 градусов")
#plt.show()

# Задание 4
M_central_symmetry = np.array([[-1, 0], [0, -1]])
quad_central_symmetry = fig @ M_central_symmetry.T
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(quad_central_symmetry[:, 0], quad_central_symmetry[:, 1], 'r-', label="Симметрия")
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("Симметрия")
#plt.show()

# Задание 5
help_M=rect_reflection
theta=10*d
M_rotation = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
ans_M=rect_reflection@M_rotation.T
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырехугольник")
plt.plot(help_M[:, 0], help_M[:, 1], 'r--', label="Отражение относительно y = 3x")
plt.plot(ans_M[:, 0], ans_M[:, 1], 'g-', label="Повернутое отражение")
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("Повернутое отражение")
#plt.show()

# Задание 6

M_6=np.array([[1,1],[a,b]])
new_fig=fig@M_6.T
print(new_fig)
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(new_fig[:, 0], new_fig[:, 1], 'r-', label="ab")
plt.xlim([-12, 12])
plt.ylim([-12, 12])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("ab")
#plt.show()

# Задание 7
M_7=(np.linalg.inv(M_6))
print(M_7)
new_fig_7=fig@M_7.T
print(new_fig_7)
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(new_fig_7[:, 0], new_fig_7[:, 1], 'r-', label="ab")
plt.xlim([-12, 12])
plt.ylim([-12, 12])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("ab")
plt.show()
# Задание 8(НАДО РАЗОБРАТЬСЯ)
M_8=M_7@M_6
print(M_8)
M_8 = np.array([[1, 0], [(b - a) / a, b / a]])
new_fig_8=fig@M_8.T
print(new_fig_8)
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(new_fig_8[:, 0], new_fig_8[:, 1], 'r-', label="ab")
plt.xlim([-12, 12])
plt.ylim([-12, 12])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("ab")
plt.show()
# Задание 9
theta = np.linspace(0, 2 * np.pi, 100)
unit_circle = np.array([np.cos(theta), np.sin(theta)]).T
M_scale = np.array([[np.sqrt(c), 0], [0, np.sqrt(c)]])
scaled_circle = unit_circle @ M_scale.T
plt.figure(figsize=(6, 6))
plt.plot(unit_circle[:, 0], unit_circle[:, 1], 'b-', label="Единичная окружность")
plt.plot(scaled_circle[:, 0], scaled_circle[:, 1], 'r-', label=f"Окружность с радиусом {c}")
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title(f"Окружность с радиусом {c}")
plt.show()

# 10 задание

theta = np.linspace(0, 2*np.pi, 100)
circle = np.array([np.cos(theta), np.sin(theta)]).T
s_x, s_y = 1, 2
M_ellipse = np.array([[s_x, 0], [0, s_y]])
ellipse = circle @ M_ellipse.T
plt.figure(figsize=(6, 6))
plt.plot(circle[:, 0], circle[:, 1], 'b-', label="Круг единичной площади")
plt.plot(ellipse[:, 0], ellipse[:, 1], 'r-', label="Некруг")
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("Отображение круга единичной площади в некруг")
plt.show()

#11 задние
M_11 = np.array([[2, 1], [1, 2]])
transformed_fig = fig @ M_11.T

plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(transformed_fig[:, 0], transformed_fig[:, 1], 'r-', label="Перпендикулярные собственные вектора")
plt.xlim([-12, 12])
plt.ylim([-12, 12])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("Отображение с перпендикулярными собственными векторами")
plt.show()

# 12 задание

# Треугольная матрица
M_12 = np.array([[2, 1], [0, 2]])

transformed_fig_single = fig @ M_12.T
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(transformed_fig_single[:, 0], transformed_fig_single[:, 1], 'r-', label="Один собственный вектор")
plt.xlim([-12, 12])
plt.ylim([-12, 12])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("Отображение без двух неколлинеарных собственных векторов")
plt.show()

# 13 задание

#14 задание
M_14 = np.array([[3, 0], [0, 3]])

# Преобразование фигуры
transformed_fig = fig @ M_14.T

# Визуализация
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(transformed_fig[:, 0], transformed_fig[:, 1], 'r-', label="Гомотетическое отображение")
plt.xlim([-12, 12])
plt.ylim([-12, 12])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("Отображение, при котором любой вектор является собственным")
plt.show()

# 15 задание
# Матрицы A и B
A = M_rotation
B = np.array([[2, 0], [0, 1]])

# AB и BA
AB = A @ B
BA = B @ A

transformed_A = fig @ A.T
transformed_B = fig @ B.T
transformed_AB = fig @ AB.T
transformed_BA = fig @ BA.T

# Визуализация
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(transformed_A[:, 0], transformed_A[:, 1], 'b-', label="A")
plt.plot(transformed_B[:, 0], transformed_B[:, 1], 'p-', label="B")
plt.plot(transformed_AB[:, 0], transformed_AB[:, 1], 'r-', label="AB")
plt.plot(transformed_BA[:, 0], transformed_BA[:, 1], 'g-', label="BA")
plt.xlim([-12, 12])
plt.ylim([-12, 12])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("Пара отображений: AB ≠ BA")
plt.show()

#16 задание
A = np.array([[2, 0], [0, 1]])
B = np.array([[1, 0], [0, 3]])
AB = A @ B
BA = B @ A
transformed_A=fig@A.T
transformed_B=fig@B.T
transformed_AB = fig @ AB.T
transformed_BA = fig @ BA.T
# Визуализация
plt.figure(figsize=(6, 6))
plt.plot(fig[:, 0], fig[:, 1], 'b-', label="Четырёхугольник")
plt.plot(transformed_AB[:, 0], transformed_AB[:, 1], 'r-', label="AB")
plt.plot(transformed_BA[:, 0], transformed_BA[:, 1], 'g-', label="BA")
plt.plot(transformed_A[:, 0], transformed_A[:, 1], 'g-', label="A")
plt.plot(transformed_B[:, 0], transformed_B[:, 1], 'g-', label="B")
plt.xlim([-12, 12])
plt.ylim([-12, 12])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.title("Пара отображений: AB = BA")
plt.show()
