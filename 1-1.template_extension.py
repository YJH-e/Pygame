#Try changing the colour of the shapes and removing the fill.
# Try making the circle bigger
#Can you make the rectangle into a square?
# Try changing the circle parameter which is currently zero to 2 and see what happens.
#Try putting the rectangle and the circle at different positions on the screen. 
#Note the use of the optional highlighted parameter zero in the circle method which makes the sun filled in. It is optional in the rectangle method and leaving it out had the same effect.

##PYGAME START-UP

import pygame 
# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 
RED = (255,0, 0)
ORANGE = (255,165,0)
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen 
size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("My Window") 
# -- Exit game flag set to false 
done = False
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

    #rectangle(surface, colour, (x-coordinate for start point, y-coordinate for start point, width, height), thickness)
    pygame.draw.rect(screen, WHITE, (250,150,150,150),20)
    pygame.draw.rect(screen, WHITE, (100,300,50,50),2)
    
    #circle(surface, colour, (x-coordinate for centre, y-coordinate for centre), radius, circle border thickness)
    pygame.draw.circle(screen, ORANGE, (75,100), 150, 1)
    
    #pygame.draw.line(surface, colour, start_pos, end_pos, width): draw a straight
    pygame.draw.line(screen, RED, (200, 200), (200, 300), 5)

    #pygame.draw.lines(surface, color, closed, points, width=1): draw multiple contiguous straight line
    pygame.draw.lines(screen, RED, True, [(340, 180), (300,250), (380,250)])

    #pygame.draw.polygon(surface, color, points)
    pygame.draw.polygon(screen, RED, [(460, 180), (420,250), (500,250)], 5)


    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop