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


#ball
ball_width = 20
x_val = 150
y_val = 200
x_direction = 0
y_direction = 0

#initialise number of times ball is hit
hit = 0
modCount = 0

#paddle
x_padd = 0
y_padd = 20
padd_length = 15
padd_width = 60

#paddle speed
y_speed = 0

#initialise life
lifeLeft = 3

#text display
font = pygame.font.SysFont("monospace", 15)

# PYGAME LOOP
### -- Game Loop 
while not done and lifeLeft > 0: 
    # -- User input and controls
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        #endif

        #paddle control

        #user press down on a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
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

    # -- Game logic goes after this comment
    # -- Screen background is BLACK 
    screen.fill (BLACK) 

    #move paddle within screen
    if y_padd >= 5 and y_padd <= y_size - 65:
        y_padd = y_padd + y_speed * 1
    elif y_padd == 0 and y_speed > 0:
        y_padd = y_padd + y_speed * 1
    elif y_padd == y_size - 60 and y_speed < 0:
        y_padd = y_padd + y_speed * 1
    #endif   


    #draw paddle
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
    
    #draw ball
    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width)) 
    x_val += x_direction
    y_val += y_direction

    #ball bounce by reversing direction
    #bounce on opposite wall (right) of screen
    if x_val >= x_size - 20:
        x_direction = -x_direction
    #bounce on paddle
    elif x_val == 15 and y_val >= y_padd - 20 and y_val <= y_padd + 60:
        x_direction = -x_direction
        hit += 1
        modCount = 0
    elif x_val == 10 and y_val >= y_padd - 20 and y_val <= y_padd + 60:
        x_direction = -x_direction
        hit += 1
        modCount = 0
    #paddle missed ball
    elif x_val < 0:
        x_val = 150
        y_val = 200
        if x_direction < 0:
            x_direction = -x_direction
        #endif
        if y_direction < 0:
            y_direction = -y_direction
        #endif
        lifeLeft = lifeLeft - 1
    #endif
    
    #bounce on side
    if y_val >= y_size - 20 or y_val <= 0:
        y_direction = -y_direction
    #endif

    #text display
    if lifeLeft == 3:
        life = font.render("life left: 3", 1, WHITE)
        screen.blit(life,(x_size - 200, 20))
    elif lifeLeft == 2:
        life = font.render("life left: 2", 1, WHITE)
        screen.blit(life,(x_size - 200, 20))
    elif lifeLeft == 1:
        life = font.render("life left: 1", 1, WHITE)
        screen.blit(life,(x_size - 200, 20))
    #endif

    #change ball speed
    if hit%5 == 0:
        if x_direction >= 0:
            x_direction = x_direction + 5
        else:
            x_direction = x_direction - 5
        #endif
        if y_direction >= 0:
            y_direction = y_direction + 5
        else:
            y_direction = y_direction - 5
        #endif
        modCount += 1
    #endif

    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop