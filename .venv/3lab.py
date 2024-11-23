import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math
from mpl_toolkits.mplot3d import Axes3D
vertices_cube = np.array([
    [-1, 1, 1,-1,-1, 1, 1,-1],
    [-1,-1, 1, 1,-1,-1, 1, 1],
    [-1,-1,-1,-1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1]
])

faces_cube = np.array([
    [0, 1, 5, 4],
    [1, 2, 6, 5],
    [2, 3, 7, 6],
    [3, 0, 4, 7],
    [0, 1, 2, 3],
    [4, 5, 6, 7]
])

fig = plt.figure()
ax = fig.add_subplot(projection='3d', proj_type = 'ortho')

def draw_shape(vertices, faces, color):
    vertices = (vertices[:3, :] / vertices[3, :]).T
    ax.add_collection3d(Poly3DCollection(vertices[faces], facecolors=color, edgecolors='k', linewidths=0.2))

draw_shape(vertices_cube, faces_cube, 'blue')

ax.set_box_aspect([1,1,1])
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
ax.view_init(azim=-37.5, elev=30)
ax.set_xticks(np.linspace(-1, 1, 5)); ax.set_yticks(np.linspace(-1, 1, 5)); ax.set_zticks(np.linspace(-1, 1, 5))

plt.show()
def scale(vertices, sx, sy, sz):
    S = np.array([[sx, 0,  0,  0],
                  [0,  sy, 0,  0],
                  [0,  0,  sz, 0],
                  [0,  0,  0,  1]])
    return S @ vertices

# Применяем масштабирование к кубику
scaled_vertices_cube = scale(vertices_cube, 1.5, 1, 0.5)

# Рисуем масштабированный кубик
fig = plt.figure()
ax = fig.add_subplot(projection='3d', proj_type='ortho')
draw_shape(scaled_vertices_cube, faces_cube, 'green')

ax.set_box_aspect([1,1,1])
ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-2, 2)
ax.view_init(azim=-37.5, elev=30)

plt.show()
#Задание 3
def translate(vertices, tx, ty, tz):
    T = np.array([[1, 0, 0, tx],
                  [0, 1, 0, ty],
                  [0, 0, 1, tz],
                  [0, 0, 0,  1]])
    return T @ vertices


translated_vertices_cube = translate(vertices_cube, 2, 1, -1)

fig = plt.figure()
ax = fig.add_subplot(projection='3d', proj_type='ortho')
draw_shape(translated_vertices_cube, faces_cube, 'red')

ax.set_box_aspect([1,1,1])
ax.set_xlim(-2, 3); ax.set_ylim(-2, 3); ax.set_zlim(-2, 3)
ax.view_init(azim=-37.5, elev=30)

plt.show()
TS_vertices = translate(scale(vertices_cube, 1.5, 1, 0.5), 2, 1, -1)
fig = plt.figure()
ax = fig.add_subplot(projection='3d', proj_type='ortho')
draw_shape(TS_vertices, faces_cube, 'red')

ax.set_box_aspect([1,1,1])
ax.set_xlim(-2, 3); ax.set_ylim(-2, 3); ax.set_zlim(-2, 3)
ax.view_init(azim=-37.5, elev=30)

plt.show()
ST_vertices = scale(translate(vertices_cube, 2, 1, -1), 1.5, 1, 0.5)
fig = plt.figure()
ax = fig.add_subplot(projection='3d', proj_type='ortho')
draw_shape(ST_vertices, faces_cube, 'red')

ax.set_box_aspect([1,1,1])
ax.set_xlim(-2, 3); ax.set_ylim(-2, 3); ax.set_zlim(-2, 3)
ax.view_init(azim=-37.5, elev=30)

plt.show()

# 4 задание
rotate_matr=np.array([[1,0,0,0],
                      [0,np.cos(60),-np.sin(60),0],
                      [0,np.sin(60),np.cos(60),0],
                      [0,0,0,1]])
vert_cube=rotate_matr@vertices_cube
fig = plt.figure()
ax = fig.add_subplot(projection='3d', proj_type='ortho')
draw_shape(vert_cube, faces_cube, 'green')

ax.set_box_aspect([1,1,1])
ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-2, 2)
ax.view_init(azim=-37.5, elev=30)

plt.show()


# 5 задание

R1=np.array([[1,0,0,1],
             [0,1,0,-1],
             [0,0,1,-1],
             [0,0,0,1]])
R2=np.array([[1,0,0,0],
            [0,np.cos(60),-np.sin(60),0],
            [0,np.sin(60),np.cos(60),0],
            [0,0,0,1]])

R3=np.array([[np.cos(60),0,np.sin(60),0],
                      [0,1,0,0],
                      [-np.sin(60),0,np.cos(60),0],
                      [0,0,0,1]])
R4=np.array([[np.cos(60),-np.sin(60),0,0],
            [np.sin(60),np.cos(60),0,0],
            [0,0,1,0],
            [0,0,0,1]])
R=np.array([[1,0,0,-1],
             [0,1,0,1],
             [0,0,1,1],
             [0,0,0,1]])
rot_vert_cube=R@R4@R3@R2@R1@vertices_cube
fig = plt.figure()
ax = fig.add_subplot(projection='3d', proj_type='ortho')
draw_shape(rot_vert_cube, faces_cube, 'green')
draw_shape(vertices_cube,faces_cube,'red')

ax.set_box_aspect([1,1,1])
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)
ax.view_init(azim=-37.5, elev=30)

plt.show()


#6 задание(ВОПРОСИТЕЛЬНО)
sc = np.array([[0.4, 0, 0, 0],
               [0, 0.4, 0, 0],
               [0, 0, 0.4, 0],
               [0, 0, 0, 1]])

move1 = np.array([[1, 0, 0, 0.8],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

move2 = np.array([[1, 0, 0, -0.8],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

theta1 = np.radians(30)
theta2 = np.radians(70)

t1 = np.array([[1, 0, 0, 0],
               [0, np.cos(theta1), -np.sin(theta1), 0],
               [0, np.sin(theta1), np.cos(theta1), 0],
               [0, 0, 0, 1]])

t2 = np.array([[1, 0, 0, 0],
               [0, np.cos(theta2), -np.sin(theta2), 0],
               [0, np.sin(theta2), np.cos(theta2), 0],
               [0, 0, 0, 1]])
camera_position = np.array([3, -4, 4])
camera_rotation_angle = np.radians(45)


T_camera = np.array([[1, 0, 0, -camera_position[0]],
                     [0, 1, 0, -camera_position[1]],
                     [0, 0, 1, -camera_position[2]],
                     [0, 0, 0, 1]])

R_camera = np.array([[np.cos(camera_rotation_angle), -np.sin(camera_rotation_angle), 0, 0],
                     [np.sin(camera_rotation_angle), np.cos(camera_rotation_angle), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

C_inv = R_camera @ T_camera
vert_cube1 = C_inv @ t2 @ t1 @ sc @ vertices_cube
vert_cube2 = C_inv @ t2 @ t1 @ move1 @ sc @ vertices_cube
vert_cube3 = C_inv @ t2 @ t1 @ move2 @ sc @ vertices_cube

fig = plt.figure()
ax = fig.add_subplot(projection='3d', proj_type='ortho')
draw_shape(vert_cube1, faces_cube, 'green')
draw_shape(vert_cube2, faces_cube, 'red')
draw_shape(vert_cube3, faces_cube, 'orange')

# Set the view for the scene with the camera
ax.set_box_aspect([1, 1, 1])
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
ax.view_init(azim=0, elev=-90)  # View from below

plt.show()

#7 задание(НЕ ДОДЕЛАНО)

sc=np.array([[0.4,0,0,0],
                [0,0.4,0,0],
                [0,0,0.4,0],
                [0,0,0,1]])
move1=np.array([[1,0,0,0.8],
                [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]])
move2=np.array([[1,0,0,-0.8],
                [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]])
fov=60
S=1/np.tan(fov/((2*np.pi)/180))
f=2
n=0.3
x=f/(f-n)
y=-f*n/(f-n)
per=np.array([[S,0,0,0],
              [0,S,0,0],
              [0,0,x,-1],
              [0,0,y,0]])
vert_cube1=per@sc@vertices_cube
vert_cube2=per@move1@sc@vertices_cube
vert_cube3=per@move2@sc@vertices_cube
fig = plt.figure()
ax = fig.add_subplot(projection='3d', proj_type='ortho')
draw_shape(vert_cube1, faces_cube, 'green')
draw_shape(vert_cube2,faces_cube,'red')
draw_shape(vert_cube3, faces_cube, 'orange')

ax.set_box_aspect([1,1,1])
ax.set_xlim(-15, 15); ax.set_ylim(-15, 15); ax.set_zlim(-15, 15)
ax.view_init(azim=-37.5, elev=30)

plt.show()
