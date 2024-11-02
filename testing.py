import pygame
import numpy as np

SCREEN_W = 800
SCREEN_H = 800

def pixels(centre_coords: tuple , r1: float, r2: float, alpha: float):
    constant =  np.pi *(2/37)
    diameters = np.linspace(r1, r2 + 0.1, 200)
    angles = np.linspace(alpha,alpha  + constant, 100)
    angles_new = np.linspace(alpha + 2* constant, alpha + 3 * constant, 100 )
    angles = np.append(angles,angles_new)
    xv,yv = np.meshgrid(diameters, angles)

    #plt.plot(xv, yv, marker='o', color='k', linestyle='none')

    x_rot = centre_coords[0] +  xv * np.cos(yv)
    y_rot = centre_coords[1] +  xv * np.sin(yv)

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

while run:
    
    x_coords, y_coords = pixels((SCREEN_W / 2, (SCREEN_H / 8) * 3), 140 , 180 , 0 + t * 0.08)
    
    screen.fill((a,b,c))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                r += 5

        if event.type == pygame.QUIT:
            run = False
    
    # pygame.draw.circle(screen , (240,50,50), (350,350), r)
    
    draw(x_coords,y_coords)
    if pygame.key.get_pressed()[pygame.K_a] == True:
        t += 1

    pygame.display.update()

pygame.quit()