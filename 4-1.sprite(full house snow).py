#no overlapping nor adjecent snowflakes



#PYGAME START-UP

import pygame
import random
import math

# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen
x_size = 640
y_size = 480
size = (x_size,y_size) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("Snow") 
# -- Exit game flag set to false 
done = False

## -- Define the class snow which is a sprite 
class Snow(pygame.sprite.Sprite): 
    # Define the constructor for snow 
    def __init__(self, color, width, height): 
        # Call the sprite constructor 
        super().__init__() 
    # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(0, x_size) 
        self.rect.y = random.randrange(0, y_size)
    #End Procedure
#End Class

# Create a list of the snow blocks 
snow_group = pygame.sprite.Group()

# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()

# Create the snowflakes 
reCreate = False
number_of_flakes = 50 # we are creating 50 snowflakes
for x in range (number_of_flakes): 
    my_snow = Snow(WHITE, 5, 5) # snowflakes are white with size 5 by 5 px
    
    #recreate snow flake if the new snowflake overlaps or is adjacent to a previously created snowflake
    if x > 0:
        count = 0
        for count in all_sprites_group:
            if my_snow == all_sprites_group(count):
                my_snow = Snow(WHITE, 5, 5) # recreate snowflake
            #endif
        #next
    #endif

    snow_group.add (my_snow) # adds the new snowflake to the group of snowflakes
    all_sprites_group.add (my_snow) # adds it to the group of all Sprites
#Next x
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

    # - Screen background is BLACK 
    screen.fill (BLACK) 
    # -- Draw here 
    all_sprites_group.draw (screen)
     
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop