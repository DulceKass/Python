import pygame
import random

#iniciar pygame
pygame.init()

#imagenes
screen = pygame.image.load("C:/Users/Tactical_IT_2/Documents/Scrips/TEST/pract/python/Día 10/galaxy.png")
icon = pygame.image.load("C:/Users/Tactical_IT_2/Documents/Scrips/TEST/pract/python/Día 10/ovni.png")
player_icon = pygame.image.load("C:/Users/Tactical_IT_2/Documents/Scrips/TEST/pract/python/Día 10/astronave.png")
enemy1_icon = pygame.image.load("C:/Users/Tactical_IT_2/Documents/Scrips/TEST/pract/python/Día 10/extraterrestre.png")

#display size

display = pygame.display.set_mode((1000, 800))


#title and icon
        #name
pygame.display.set_caption("Space girls")
        #icon
pygame.display.set_icon(icon)


#player
    #initial position
player_icon_x = 468
player_icon_y = 600
x_change = 0
y_change = 0

#enemy
    #initial position, random
enemy1_icon_x = random.randint(0, 936)
enemy1_icon_y = random.randint(0, 100)

xe_change = 0.5
ye_change = 50


#function player movement 
def player(x,y):
    display.blit(player_icon,(x,y))

#function enemy movement 
def enemy1(x,y):
    display.blit(enemy1_icon,(x,y))

#game loop
    
flag = True
while flag:
    # first, imagen of the screen.
    display.blit(screen,(0,0))

    
    for event in pygame.event.get():
        # when we click the X the loop ends
        if event.type == pygame.QUIT:
            flag = False
        
        # condition about the movement of the skyrocket, when we press the left key the skyrocket moves 0.2px to the left, when we press the right key the skyrocket moves 0.2px to the right.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -1
            if event.key == pygame.K_RIGHT:
                x_change = +1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -1
            if event.key == pygame.K_DOWN:
                y_change = +1

        # condition about the movement of the skyrocket, when we press the up key the skyrocket moves 0.2px up, when we press the down key the skyrocket moves 0.2px down.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    # the player appears
                
    player_icon_x += x_change
    player_icon_y += y_change

    #limits within  the display, the size of the screen in X its between 0-1000 so, the limit of its between 0 and 1000, so... the player shouldn't pass less than 0 and more than 1000, but the size of the icon player its 64px, then, we have to rest 1000 - 64
    if player_icon_x <= 0:
        player_icon_x = 0
    elif player_icon_x >=936 :
        player_icon_x = 936
    elif player_icon_y <=0 :
        player_icon_y = 0
    elif player_icon_y >= 736:
        player_icon_y = 736

# the enemy appears
                
    enemy1_icon_x += xe_change

    #limits within  the display, the size of the screen in X its between 0-1000 so, the limit of its between 0 and 1000, so... the player shouldn't pass less than 0 and more than 1000, but the size of the icon player its 64px, then, we have to rest 1000 - 64
    if enemy1_icon_x <= 0:
        xe_change = 0.5
        enemy1_icon_y += ye_change
    elif enemy1_icon_x >= 936:
        xe_change = -0.5
        enemy1_icon_y += ye_change



    player(player_icon_x,player_icon_y)
    enemy1(enemy1_icon_x, enemy1_icon_y)

    pygame.display.update()

