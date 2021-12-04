## -- Define the class tile which is a sprite 
#PYGAME START-UP

import pygame 
# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (50,50,255) 

# -- Initialise PyGame
pygame.init() 
# -- Blank Screen 
size = (640,480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("PacMan") 
# -- Exit game flag set to false 
done = False
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()

#map
map = [[1,1,1,1,1,1,1,1,1,1], 
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1], 
[1,1,0,1,1,1,1,1,0,1], 
[1,0,0,0,0,0,1,0,0,1],
[1,0,1,1,1,0,1,0,0,1],
[1,0,1,1,1,0,1,0,0,1], 
[1,0,1,1,1,0,1,0,0,1], 
[1,0,0,0,0,0,0,0,0,1], 
[1,1,1,1,1,1,1,1,1,1]]

class tile(pygame.sprite.Sprite): 
    # Define the constructor for invader 
    def __init__(self, color, width, height, x_ref, y_ref): 
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        self.rect = self.image.get_rect() 
        # Set the position of the player attributes
        self.rect.x = x_ref 
        self.rect.y = y_ref
    #endprocedure
#endclass

# Create a list of all sprites 
all_sprites_list = pygame.sprite.Group() 
 
# Create a list of tiles for the walls 
wall_list = pygame.sprite.Group()
 
# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10): 
    for x in range (10): 
        if map[x][y] == 1: 
            my_wall = tile(BLUE, 20, 20, x*20, y *20) 
            wall_list.add(my_wall) 
            all_sprites_list.add(my_wall)
        #endif
    #next
#next



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
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop