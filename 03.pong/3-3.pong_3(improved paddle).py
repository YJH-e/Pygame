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

x_size = 640
y_size = 480
# -- Blank Screen 
size = (x_size,y_size) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("Pong") 
# -- Exit game flag set to false 
done = False
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()


# PYGAME LOOP

#ball
ball_width = 20
x_val = 150
y_val = 200
x_direction = 5
y_direction = 5

#paddle
x_padd = 0
y_padd = 20
padd_length = 15
padd_width = 60

#paddle speed
y_speed = 0
speed_val = 5
### -- Game Loop 
while not done: 
    # -- User input and controls
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        #endif

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -speed_val
            elif event.key == pygame.K_DOWN:
                y_speed = speed_val
            #endif
        

        # User let up on a key
        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                y_speed = 0
            #endif
            if event.key == pygame.K_DOWN:
                y_speed = 0  
            #endif                
        #End If
    #Next event
    
    #move paddle within screen
    if y_padd >= 5 and y_padd <= y_size - 65:
        y_padd = y_padd + y_speed
    elif y_padd == 0 and y_speed > 0:
        y_padd = y_padd + y_speed
    elif y_padd == y_size - 60 and y_speed < 0:
        y_padd = y_padd + y_speed
    #endif

    

    # -- Game logic goes after this comment
    # -- Screen background is BLACK 
    screen.fill (BLACK) 
    # -- Draw here 
    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width)) 
    x_val += x_direction
    y_val += y_direction

    #bounce by reversing direction
    if x_val >= x_size - 20 or x_val <= 0:
        x_direction = -x_direction
    #endif
    if y_val >= y_size - 20 or y_val <= 0:
        y_direction = -y_direction
    #endif

    
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))




    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop