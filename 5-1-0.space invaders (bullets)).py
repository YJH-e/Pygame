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
RED = (255, 0, 0)
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

#text display
font = pygame.font.SysFont("monospace", 15)

# Create a list of x_coordinates of invaders
x_co = []

# Create a list of y_coordinates of invaders
y_co = []

# create player position globally. The value they hold does not matter until they are being assigned
x_pos = 0
y_pos = 0

#initialise x_speed for player
x_speed = 0
y_speed = 0

#initialise score of player
score = 0

#intialise number of bullets
bullet_count = 0

invaderSize = 10
## -- Define the class invader which is a sprite 
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

        #recreate invader starting coordinate if the new invader overlaps or is adjacent to a previously created invader
        ivdNum = 0
        for invNum in range (0, len(x_co)):
            #checks if new inavder is adjacent or overlapping a previous invader
            while self.rect.x <= x_co[invNum] + invaderSize and self.rect.x >= x_co[invNum] - invaderSize and self.rect.y <= y_co[invNum] + invaderSize and self.rect.y >= y_co[invNum] - invaderSize:
                self.rect.x = random.randrange(0, x_size - invaderSize) 
                self.rect.y = random.randrange(-50, 0)
            #endwhile
        #next

        #add coordinate of new snowflake to coordinate lists
        x_co.append(self.rect.x)
        y_co.append(self.rect.y)

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

## -- Define the class player which is a sprite 
class Player(pygame.sprite.Sprite): 
    # Define the constructor for snow 
    def __init__(self, color, width, height, x_pos, y_pos):
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 300 
        self.rect.y = y_size - 100

        x_pos = self.rect.x
        y_pos = self.rect.y

    #End Procedure
    
    # Class update function - runs for each pass through the game loop 
    def update(self, x_pos, y_pos):
        #keep player within screen while moving player
        if (self.rect.x >= 3 and self.rect.x <= x_size - 13) or (self.rect.x <= 3 and x_speed > 0) or (self.rect.x >= x_size - 13 and x_speed < 0):
            self.rect.x = self.rect.x + x_speed
            x_pos = self.rect.x
        if (self.rect.y >= 3 and self.rect.y <= y_size - 13) or (self.rect.y <= 3 and y_speed > 0) or (self.rect.y >= y_size - 13 and y_speed < 0):
            self.rect.y = self.rect.y + y_speed
            y_pos = self.rect.y
        #endif
    #endprocedure
#End Class


## -- Define the class bullet which is a sprite 
class Bullet(pygame.sprite.Sprite): 
    # Define the constructor for snow 
    def __init__(self, color, width, height, x_pos, y_pos):
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = x_pos
        self.rect.y = y_pos

    #End Procedure
    
    # Class update function - runs for each pass through the game loop 
    def update(self):
        #keep player within screen while moving player
        self.rect.y = self.rect.y - 7

        #endif
    #endprocedure
#End Class

# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group()

# Create a list of the snow blocks 
invader_group = pygame.sprite.Group()

#create a list of all bullets
bullet_group = pygame.sprite.Group()

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
    player = Player(YELLOW, 10, 10, x_pos, y_pos) # snowflakes are white with size 5 by 5 px
    all_sprites_group.add (player) # adds it to the group of all Sprites
#Next y

# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()


############################################################### GAME LOOP ###############################################################
# PYGAME LOOP

while not done: 
    # -- User input and controls
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN: # - a key is down 
            if event.key == pygame.K_LEFT: # - if the left key pressed 
                x_speed = -3 # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                x_speed = 3 # speed set to 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            elif event.key == pygame.K_p: #stop player completely
                x_speed = 0
                y_speed = 0
            elif event.key == pygame.K_SPACE: # fire bullets
                bullet = Bullet(RED,5,5,x_pos, y_pos)
                all_sprites_group.add(bullet)
                bullet_group.add(bullet)
                bullet_count += 1
                
            #endif
        
            #endif
        #End If
    #Next event
    # -- Game logic goes after this comment

    # -- Game logic goes in here 
    all_sprites_group.update()

    # Game logic of player hitting invader
    # -- when invader hits the player add 5 to score. 
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)

    for h in player_hit_group:
        score = score + 5     
    #next


    
    # -- Screen background is BLACK 
    screen.fill(BLACK) 
    # -- Drawing code goes here
    all_sprites_group.draw(screen)
    
    #text
    scoreDisplay = font.render("score: " + str(score), 1, WHITE)
    screen.blit(scoreDisplay,(20, 20))
    bulletDisplay = font.render("bullets left: " + str(50 - bullet_count), 1, WHITE)
    screen.blit(bulletDisplay,(20, 40))

    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop