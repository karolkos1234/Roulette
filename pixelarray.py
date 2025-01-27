import numpy as np
import pygame
import pygame.surfarray as surfarray

SCREEN_W = 800
SCREEN_H = 800

def setup(c = 200):
    

    a = np.zeros((c, c, 2))

    for x in range(c):
        for y in range(c):
            a[y, x, 0] = x
            a[y, x, 1] = y

    half = (c - 1) / 2

    a = a - half

    x = a[:, :, 0]
    y = a[:, :, 1]

    r = np.sqrt(x*x + y*y)

    cos_theta = np.divide(x, y, out = np.zeros_like(x), where = y != 0)
    theta = np.arctan2(x,y) + np.pi

    red = np.array((255, 0, 0))
    blue = np.array((0, 150, 150))
    red_vector = np.full((c, c, 3), red)
    blue_vector = np.full( (c, c, 3), blue)

    r_3 = np.dstack((r,r,r))
    theta_3 = np.dstack((theta,theta,theta))
    return red_vector, blue_vector, theta_3, r_3

def pixelarr(theta, r_1, r_2, angle_arr, dia_arr, col_1, col_2, off = 0.16):
    if theta + off <= 2*np.pi:
        colormap = np.where(((dia_arr <= r_2) & (dia_arr >= r_1)) & ((theta  <= angle_arr ) &  ((theta + off >= angle_arr  )|(theta + off - 2* np.pi >= angle_arr + off))) , col_1, col_2) 
        # colormap = np.where(((dia_arr >= r_1) & (dia_arr <= r_2))&((angle_arr >= theta)&(angle_arr <= (theta + off) )), col_1,col_2)
    else:
        angle_arr = np.flip(angle_arr)
        colormap = np.where((((dia_arr >= r_1) & (dia_arr <= r_2)) & ((angle_arr >= theta - np.pi) & (angle_arr <= theta + off -np.pi) )), col_1,col_2)
    return colormap


c = 400

red, blue, theta, r = setup(c)


pygame.init()
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
run = True
clock = pygame.time.Clock()

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)


t = 0
phi  = 0
while run:

    screen.fill((30,90,15))
    

    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            run = False
    
    if phi > 2*np.pi:
        phi -= 2*np.pi
    colormap = pixelarr(phi, 140, 180, theta, r, red, blue)
    square = surfarray.make_surface(colormap)

    new_square = surfarray.make_surface(theta * 30)

    screen.blit(new_square,(200,50))

    screen.blit(square,(200,50))

    text_surface = my_font.render(f'phi: {phi}', False, (0, 0, 0))

    screen.blit(text_surface, (600,700))
    if pygame.key.get_pressed()[pygame.K_a] == True:
        phi = phi + 0.01
    if pygame.key.get_pressed()[pygame.K_w] == True:
        phi = phi + 0.04

    
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
    


