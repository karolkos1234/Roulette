import pygame
import numpy as np

SCREEN_W = 800
SCREEN_H = 800

def pixels(r1: float, r2: float, alpha: float):
    angles_list = []

    constant =  np.pi *(2/37)
    diameters = np.linspace(r1, r2 + 0.1, 40)
    
    
    

    for num in range(0, 36, 2):
        angles_new = np.linspace(alpha + num* constant, alpha + (num + 1) * constant, 40 )
        angles_list.append(angles_new)

    angles = np.concatenate(angles_list)
    xv,yv = np.meshgrid(diameters, angles)

    return xv, yv
    

def rotate(r: float,theta: float, centre_coords: tuple, angle: float):
    

    x_rot = centre_coords[0] +  r * np.cos(theta + angle)
    y_rot = centre_coords[1] +  r * np.sin(theta + angle)

    return x_rot, y_rot

def draw(x,y):
    points_list = []
    shape = np.shape(x)
    for a in range(shape[0]):
        for b in range(shape[1]):
                x_c = x[a][b]
                y_c = y[a][b]
                point = pygame.Rect((x_c,y_c, 1.5, 1.5))
                points_list.append(point)

    for dot in points_list:
        pygame.draw.rect(screen, (220, 20, 20), dot)





# class DrawableObject:
#     def __init__(self) -> None:
#         # self.pixels - a list of coordinate tuples
#         self.pixels : list = [()]
#         pass



pygame.init()

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

run = True



a, b, c = 30, 90, 15

r = 15


dot = pygame.Rect((300.16, 250.17, 1.5, 1))


t = 0

center_coords = (SCREEN_W / 2, (SCREEN_H / 8) * 3)

r_coords, theta_coords = pixels( 140 , 180 ,  0)

while run:
    
    x_co, y_co = rotate(r_coords,theta_coords,(SCREEN_W / 2, (SCREEN_H / 8) * 3), t * 0.08)

    # r_coords, theta_coords = pixels((SCREEN_W / 2, (SCREEN_H / 8) * 3), 140 , 180 , 0 + t * 0.08)
    
    screen.fill((a,b,c))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                r += 5

        if event.type == pygame.QUIT:
            run = False
    
    # pygame.draw.circle(screen , (240,50,50), (350,350), r)
    
    draw(x_co,y_co)
    if pygame.key.get_pressed()[pygame.K_a] == True:
        t += 1

    pygame.display.update()

pygame.quit()