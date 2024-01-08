import pygame
from pygame.locals import *
from OpenGL.GL import *
#from OpenGL.GLUT import *
import math
#import time

#initial camera position (translation)
camera_x, camera_y, camera_z = 0, 0, -5
#initial camera rotation (-||-)
camera_rot_x, camera_rot_y, camera_rot_z = 0, 0, 0


#
vertices = (            # X Y Z
    (0, -2, -2),         #0                
    (0, 0, -2),          #1
    (-2, 0, -2),         #2
    (-2, -2, -2),        #3                                     right = - y
    (0, -2, 0),          #4              ###                    left = + y
    (0, 0, 0),           #5                ###                  up   = + x
    (-2, -2, 0),         #6                                     down = - x
    (-2, 0, 0)           #7
)

edges = (
    (0, 1),     #0, 1
    (1, 2),     #1, 2
    (2, 3),     #2, 3
    (3, 0),     #3, 0
    (4, 5),     #4, 5
    (4, 6),     #4, 6
    (6, 7),     #6, 7
    (7, 5),     #7, 5
    (0, 4),     #0, 4
    (1, 5),     #1, 5
    (2, 7),     #2, 7
    (3, 6)      #3, 6
)


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def set_projection_matrix():
    near_clip = 0.1
    far_clip = 50.0
    #fov_y = 45.0

    aspect_ratio = 800 / 600
    #f = 1 / math.tan(fov_y * 0.5 * math.pi / 180)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-near_clip * aspect_ratio, near_clip * aspect_ratio, -near_clip, near_clip, near_clip, far_clip)
    glMatrixMode(GL_MODELVIEW)


def main():
    global camera_x, camera_y, camera_z, camera_rot_x, camera_rot_y, camera_rot_z

    pygame.init()
    display = (1600, 1200)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()

    set_projection_matrix()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        ################ ROTATION

        if keys[K_q]:
            camera_rot_y += 1
        if keys[K_a]:
            camera_rot_y -= 1
        if keys[K_w]:
            camera_rot_x += 1
        if keys[K_s]:
            camera_rot_x -= 1
        if keys[K_e]:
            camera_rot_z -= 1
        if keys[K_d]:
            camera_rot_z += 1

        ############### TRANSLATION

        if keys[K_r]:
            camera_y += 0.1
        if keys[K_f]:
            camera_y -= 0.1
        if keys[K_t]:
            camera_x += 0.1
        if keys[K_g]:
            camera_x -= 0.1
        if keys[K_y]:
            camera_z += 0.1
        if keys[K_h]:
            camera_z -= 0.1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(camera_x, camera_y, camera_z)

        glRotatef(camera_rot_x, 1, 0, 0)
        glRotatef(camera_rot_y, 0, 1, 0)
        glRotatef(camera_rot_z, 0, 0, 1)

        cube()

        pygame.display.flip()
        pygame.time.wait(10)
        clock.tick(30)


if __name__ == "__main__":
    main()
