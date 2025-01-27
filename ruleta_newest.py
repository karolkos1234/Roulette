import numpy as np
import pygame
import pygame.surfarray as surfarray
from math import cos, sin, pi

SCREEN_W = 1400
SCREEN_H = 900
background_rgb = (30,90,15)

size = 600 # je potřeba aby byl int a zároveň násobek 10

FONT_COLOR = (255, 255, 255)  
TEXT_HEIGHT = 40
pygame.font.init() 
font = pygame.font.SysFont("Arial", TEXT_HEIGHT)

pygame.init()
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

def setup(c):
    

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
    blue = np.array((0, 0, 0))
    green = np.array((10, 125, 10))
    background_color = np.array(background_rgb)
    red_vector = np.full((c, c, 3), red)
    blue_vector = np.full( (c, c, 3), blue)
    green_vector = np.full( (c, c, 3), green)
    background_vector = np.full( (c, c, 3), background_color)

    r_3 = np.dstack((r,r,r))
    theta_3 = np.dstack((theta,theta,theta))
    return red_vector, blue_vector, green_vector, background_vector,theta_3, r_3

def pixelarr(theta_1, theta_2, r_1, r_2, angle_arr, dia_arr, col_1, colormap_original):
    
    colormap = np.where(((dia_arr >= r_1) & (dia_arr <= r_2)) & ((angle_arr >= theta_1) & (angle_arr <= theta_2)) , col_1, colormap_original) 
       
    return colormap

def screenblit_numbers(number, angle, radius, screen, screen_width, screen_height):
    text_surf = font.render(number, True, FONT_COLOR)
    angle_radians = angle * 2*pi/360
    rotated_text_surface = pygame.transform.rotate(text_surf, -(angle))
    rotated_width, rotated_height = rotated_text_surface.get_size()

    center_x = (screen_width - rotated_width) / 2 + (radius * cos(angle_radians - (pi/2)))
    center_y = (screen_height - rotated_height) / 2 + (radius * sin(angle_radians - (pi/2)))

    screen.blit(rotated_text_surface, (center_x,center_y))




numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23,
                      10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 2, 18, 29, 7, 28, 12, 35, 3, 26]


red, blue,green,background, theta, r = setup(size)

colormap = background

for i, number in enumerate(numbers):
    if (i % 2) == 0 and (i != 0) :
        col = red
    elif (i % 2) ==1:
        col = blue
    else :
        col = green
    
    angle_1 = (i / 37) * 2*pi
    angle_2 = ( (i+1) / 37) * 2*pi
    colormap = pixelarr(angle_1,angle_2,(size/2) - (size/10), (size/2) ,theta,r,col,colormap)

    
square = pygame.surfarray.make_surface(colormap)

for i, number in enumerate(numbers):
    angle = (i/37) * 360 -90 + (1/37)*180 
    number = str(number)
    screenblit_numbers(number, angle, 270,square, size, size)

padding = 50
padded_surface = pygame.Surface(
    (square.get_width() + 2 * padding, square.get_height() + 2 * padding),
    pygame.SRCALPHA,  # Use alpha to allow transparency
)
padded_surface.fill((0, 0, 0, 0))
padded_surface.blit(square, (padding, padding))




x, y = 400, 400
angle = 0

run = True
clock = pygame.time.Clock()
while run:

    screen.fill(background_rgb)

    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            run = False

    rotated_square = pygame.transform.rotate(padded_surface, angle)
    rotated_rect = rotated_square.get_rect(center=(x, y))

    screen.blit(rotated_square, rotated_rect.topleft)
    
    if pygame.key.get_pressed()[pygame.K_a] == True:
        angle += 2
    elif pygame.key.get_pressed()[pygame.K_w] == True:
        angle  += 3
    elif pygame.key.get_pressed()[pygame.K_s] == True:

    
        angle -= 1 
    elif pygame.key.get_pressed()[pygame.K_d] == True:
        angle += 0.01
    else:
        angle += 0.25
    # for number in numbers:
    #     number = str(number)
    #     screenblit_numbers(number, angle, 150)
    #     angle = angle + 10

    # screen.blit(square,(150,50))
    
    pygame.display.flip()
    clock.tick(240)

pygame.quit()