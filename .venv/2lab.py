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
plt.plot(unit_circle[:, 0], unit_circle[:, 1], 'b-', label="Unit Circle")
plt.plot(scaled_circle[:, 0], scaled_circle[:, 1], 'r-', label=f"Circle with Area {c}")
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title("Scaling Unit Circle to Area c")
plt.show()