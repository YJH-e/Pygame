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
pygame.display.set_caption("Space Invaders") 
# -- Exit game flag set to false 
done = False

invaderSize = 10
## -- Define the class snow which is a sprite 
class Invader(pygame.sprite.Sprite): 
    # Define the constructor for snow 
    def __init__(self, color, width, height, speed):
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(0, x_size - invaderSize) 
        self.rect.y = random.randrange(-50, 0)

        # Set speed of the sprite 
        self.speed = speed
    #End Procedure
    
    # Class update function - runs for each pass through the game loop 
    def update(self): 
        self.rect.y = self.rect.y + self.speed
        #make snowflake reappear on top of screen after falling pass bottom
        if self.rect.y > y_size:
            self.rect.y = self.rect.y - y_size - invaderSize
        #endif
    #endprocedure
#End Class

## -- Define the class snow which is a sprite 
class Player(pygame.sprite.Sprite): 
    # Define the constructor for snow 
    def __init__(self, color, width, height):
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 300 
        self.rect.y = size[0] - height

        # Set speed of the sprite 
        self.speed = 0
    #End Procedure
    
    # Class update function - runs for each pass through the game loop 
    def update(self): 
        self.rect.y = self.rect.y + self.speed
        #make snowflake reappear on top of screen after falling pass bottom
        if self.rect.y > y_size:
            self.rect.y = self.rect.y - y_size - invaderSize
        #endif
    #endprocedure
#End Class

# Create a list of the snow blocks 
invader_group = pygame.sprite.Group()

# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()

# Create the invaders
number_of_invaders = 10 # we are creating 10 invaders
for x in range (number_of_invaders): 
    invaders = Invader(BLUE, invaderSize, invaderSize, 1)
    invader_group.add (invaders) # adds the new invader to the group of invaders
    all_sprites_group.add (invaders) # adds it to the group of all Sprites
#Next x

# Create the player
number_of_players = 1 # we are creating 10 invaders
for y in range (number_of_players): 
    player = Player(YELLOW, 10, 10) # snowflakes are white with size 5 by 5 px
    all_sprites_group.add (player) # adds it to the group of all Sprites
#Next y





# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()

# PYGAME LOOP
### -- Game Loop 
while not done: 
    # -- User input and controls
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN: # - a key is down 
            if event.key == pygame.K_LEFT: # - if the left key pressed 
                player.player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                player.player_set_speed(3) # speed set to 3
            #endif
        elif event.type == pygame.KEYUP: # - a key released 
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                    player.player_set_speed(0) # speed set to 0
                #endif
            #endif
        #End If
    #Next event
    # -- Game logic goes after this comment

    # -- Game logic goes in here 
    all_sprites_group.update() 
    # -- Screen background is BLACK 
    screen.fill(BLACK) 
    # -- Drawing code goes here
    all_sprites_group.draw(screen)
     
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop