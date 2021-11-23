#PYGAME START-UP

import pygame 
# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen
# declare screen size as variables
screen_x = 640
screen_y = 480
size = (screen_x,screen_y) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("My Window") 
# -- Exit game flag set to false 
done = False

#introduce some game logic
sun_x = 40
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
    # -- Draw here 
    pygame.draw.rect(screen, BLUE, (220,165,200,150)) 
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y),40,0)
    
    #retrieve sun
    if sun_x != screen_x + 40:
        sun_x = sun_x + 5
    elif sun_x == screen_x + 40:
        sun_x = -40
    #endif
    
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop