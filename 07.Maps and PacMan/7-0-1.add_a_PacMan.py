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
x_size_screen = 640
y_size_screen = 480
size = (x_size_screen,y_size_screen) 
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

class Player(pygame.sprite.Sprite):
    #initialise x_speed for player
    x_speed = 0
    y_speed = 0

    # Define the constructor for snow 
    def __init__(self):
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and put a picture on it
        playerImage = pygame.image.load('PacMan_simple.png')
        self.image = pygame.transform.scale(playerImage, (10, 10))
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 21 
        self.rect.y = 21

        x_pos = self.rect.x
        y_pos = self.rect.y

    #End Procedure
    
    # Class update function - runs for each pass through the game loop 
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # - a key is down 
                if event.key == pygame.K_LEFT: # - if the left key pressed 
                    self.x_speed = -1 # speed set to -3
                elif event.key == pygame.K_RIGHT: # - if the right key pressed
                    self.x_speed = 1 # speed set to 3
                elif event.key == pygame.K_UP:
                    self.y_speed = -1
                elif event.key == pygame.K_DOWN:
                    self.y_speed = 1
                elif event.key == pygame.K_SPACE: #stop player
                    self.x_speed = 0
                    self.y_speed = 0
                #endif
            #endif
        #next
        #keep player within screen while moving player
        if (self.rect.x >= 1 and self.rect.x <= x_size_screen - 1 - 10) or (self.rect.x <= 1 and self.x_speed > 0) or (self.rect.x >= x_size_screen - 1 - 10 and self.x_speed < 0):
            self.rect.x = self.rect.x + self.x_speed
        elif (self.rect.y >= 1 and self.rect.y <= y_size_screen - 1 - 10) or (self.rect.y <= 1 and self.y_speed > 0) or (self.rect.y >= y_size_screen - 1 - 10 and self.y_speed < 0):
            self.rect.y = self.rect.y + self.y_speed
        #endif
    #endprocedure
#End Class

class Game():
    def keyPress():
        # -- User input and controls
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            else:
                Player.update()
            #endif
        #next
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

# Create PacMan x 1
player = Player() # snowflakes are white with size 5 by 5 px
all_sprites_list.add (player) # adds it to the group of all Sprites


# PYGAME LOOP
### -- Game Loop 
while not done:
    
    # -- Game logic goes after this comment
    # -- Screen background is BLACK 
    screen.fill (BLACK) 
    # -- Draw here
    all_sprites_list.draw(screen)
    all_sprites_list.update()
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop