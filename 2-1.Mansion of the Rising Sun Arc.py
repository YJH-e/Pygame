#PYGAME START-UP

import pygame 
# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 
ORANGE = (255,165,0)
LIGHTBLUE = (173,216,230)
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen
# declare screen size as variables
screen_x = 1024
screen_y = 512
size = (screen_x,screen_y) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("My Window") 
# -- Exit game flag set to false 
done = False

#introduce some game logic
sun_x = 0
sun_y = 100
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()


# PYGAME LOOP
### -- Game Loop 
while not done: 
    # -- User input and controls
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        #End If
    #Next event
    # -- Game logic goes after this comment
    # -- Screen background is BLACK 
    screen.fill (BLACK) 

    # -- Draw Orange Giant (sun)
    pygame.draw.circle(screen, ORANGE, (sun_x, sun_y),200)
    
    #retrieve sun
    if sun_x != screen_x + 200:
        sun_x = sun_x + 2
        sun_y = 1/1024*(sun_x - 512)**2 + 200
    elif sun_x == screen_x + 200:
        sun_x = -200
    #endif

    # -- Draw mansion
    pygame.draw.rect(screen, LIGHTBLUE, (362,350,300,150))
    # mansion windows
    pygame.draw.rect(screen, WHITE, (382, 360, 60, 50))
    pygame.draw.rect(screen, WHITE, (382, 435, 60, 50))
    pygame.draw.rect(screen, WHITE, (582, 360, 60, 50))
    pygame.draw.rect(screen, WHITE, (582, 435, 60, 50))
    #mansion doors
    pygame.draw.rect(screen, WHITE, (467, 430, 40, 70))
    pygame.draw.rect(screen, WHITE, (517, 430, 40, 70))

    
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop