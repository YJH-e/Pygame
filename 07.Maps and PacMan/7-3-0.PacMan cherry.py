#I have written a function returning player x and y speeds from Game class after KeyPress
#I do not know how to get the specific player x and y speeds from Game class to player class for updating player position



## -- Define the class tile which is a sprite 
#PYGAME START-UP

import pygame
import random

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
    # Define the constructor for snow 
    def __init__(self):
        # Call the sprite constructor
        super().__init__() 
        #initialise x_speed for player
        self.x_speed = 0
        self.y_speed = 0
        # Create a sprite and put a picture on it
        playerImage = pygame.image.load('PacMan_simple.png')
        self.image = pygame.transform.scale(playerImage, (10, 10))
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 21 
        self.rect.y = 21

    #End Procedure

    def speedSetter(self, x_speed, y_speed):
        self.x_speed = x_speed
        self.y_speed = y_speed
    #endprocedure

    def placeSetter(self, x_speed, y_speed):
        if x_speed > 0 and y_speed == 0:#player moving to the right
            self.rect.x = self.rect.x - 2
        #endif
        if x_speed < 0 and y_speed == 0:#player moving to the left
            self.rect.x = self.rect.x + 2
        #endif
        if x_speed == 0 and y_speed < 0:#player moving up
            self.rect.y = self.rect.y + 2
        #endif
        if x_speed == 0 and y_speed > 0:#player down
            self.rect.y = self.rect.y - 2
        #endif
    #endprocedure


    # update
    def update(self):
        self.rect.x = self.rect.x + self.x_speed
        self.rect.y = self.rect.y + self.y_speed      
    #endprocedure
#End Class

class Cherry():
    def __init__(self):
        # Call the sprite constructor
        super().__init__()

        ###self.image = pygame.Surface([10,10]) 
        ###self.image.fill(RED)

        # Create a sprite and put a picture on it
        cherryImage = pygame.image.load('cherry.png')
        self.image = pygame.transform.scale(cherryImage, (10, 10))
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(21,171)
        self.rect.y = random.randrange(21,171)
    #End Procedure

    def getCherryPos(self):
        return self.rect.x, self.rect.y
    #endfunction
        
class Game():
    def __init__(self):
        self.done = False
        #variables for setting player speed in response to keys pressed
        self.player_x_speed = 0
        self.player_y_speed = 0
        #list to hold x and y cooridnates of cherreis
        self.cherry_x = []
        self.cherry_y = []
        #list of cherries picked up by player
        self.cherries_picked = []

        # Create a list of all sprites 
        self.all_sprites_list = pygame.sprite.Group() 
        # Create a list of tiles for the walls 
        self.wall_list = pygame.sprite.Group()
        # Create a list of cherries
        self.cherry_list = pygame.sprite.Group()

        # Create walls on the screen (each tile is 20 x 20 so alter cords)
        for y in range(10): 
            for x in range (10): 
                if map[x][y] == 1: 
                    my_wall = tile(BLUE, 20, 20, x*20, y *20) 
                    self.wall_list.add(my_wall) 
                    self.all_sprites_list.add(my_wall)
                #endif
            #next
        #next

        # Create PacMan x 1
        self.p = Player()
        self.all_sprites_list.add(self.p) # adds it to the group of all Sprites

        # Create cherries x 5
        num_of_cherries = 5
        for j in range (num_of_cherries):
            self.c = Cherry()
            #getting position of the new cherry created to check for overlapping
            temp_cherry_x, temp_cherry_y = self.c.getCherryPos()
            

            #check if cherry has generated on top of each other or on walls
            #check if cherries overlap or are adjacent
            if j > 1:
                for k in range (0,len(self.cherry_x)):
                    while temp_cherry_x <= self.cherry_x[k] + 10 and temp_cherry_x >= self.cherry_x[k] - 10 and temp_cherry_y <= self.cherry_y[k] + 10 and temp_cherry_y >= self.cherry_y[k] - 10:
                        self.c = Cherry()
                        #getting position of the new cherry created to check for overlapping
                        temp_cherry_x, temp_cherry_y = self.c.getCherryPos()
                    #endwhile
                #next
            #endif
            #check if the cherry has generated on a wall
            cherry_hit_wall_list = pygame.sprite.spritecollide(self.c, self.wall_list, False)
            for i in cherry_hit_wall_list:
                self.c = Cherry()
                #getting position of the new cherry created to check for overlapping
                temp_cherry_x, temp_cherry_y = self.c.getCherryPos()
                #check if cherries overlap or are adjacent
                for k in range (0,len(self.cherry_x)):
                      while temp_cherry_x <= self.cherry_x[k] + 10 and temp_cherry_x >= self.cherry_x[k] - 10 and temp_cherry_y <= self.cherry_y[k] + 10 and temp_cherry_y >= self.cherry_y[k] - 10:
                        self.c = Cherry()
                        #getting position of the new cherry created to check for overlapping
                        temp_cherry_x, temp_cherry_y = self.c.getCherryPos()
                    #endwhile
                #next
            #next
            self.cherry_x.append(temp_cherry_x)
            self.cherry_y.append(temp_cherry_y)
            self.cherry_list.add(self.c)
            self.all_sprites_list.add(self.c)
        #next       
    #endprocedure

    def runGame(self):
        while not self.done:

            self.done = False
            # -- User input and controls
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.done = True
                #endif


                if event.type == pygame.KEYDOWN: # - a key is down 
                    if event.key == pygame.K_UP:
                        self.player_x_speed = 0
                        self.player_y_speed = -1
                    elif event.key == pygame.K_DOWN:
                        self.player_x_speed = 0
                        self.player_y_speed = 1

                    elif event.key == pygame.K_LEFT: # - if the left key pressed
                        self.player_x_speed = -1
                        self.player_y_speed = 0
                    elif event.key == pygame.K_RIGHT: # - if the right key pressed
                        self.player_x_speed = 1
                        self.player_y_speed = 0

                    elif event.key == pygame.K_SPACE: #stop player
                        self.player_x_speed = 0
                        self.player_y_speed = 0
                    #endif
                    
                    #pass speed values into object player
                    self.p.speedSetter(self.player_x_speed, self.player_y_speed)
                #endif
            #next

            # -- Check for collisions between pacman and wall tiles 
            player_hit_list = pygame.sprite.spritecollide(self.p, self.wall_list, False)
            for i in player_hit_list:
                print("hit")
                print(self.p.rect.x)
                print(self.p.rect.y)
                print(self.player_x_speed)
                print(self.player_y_speed)
                #set player back to position before hitting wall
                self.p.placeSetter(self.player_x_speed, self.player_y_speed)
                # bounce pacman off wall
                self.player_x_speed = 0 #-self.player_x_speed
                self.player_y_speed = 0 #-self.player_y_speed
                self.p.speedSetter(self.player_x_speed, self.player_y_speed)
            #next
            
            # -- Screen background is BLACK 
            screen.fill (BLACK) 
            # -- Draw here
            self.all_sprites_list.draw(screen)
            self.all_sprites_list.update()
            # -- flip display to reveal new position of objects 
            pygame.display.flip()
            # - The clock ticks over 
            clock.tick(60)
        #End While - End of game loop
        pygame.quit()### -- Game Loop
    #endprocedure
#endclass


g = Game()
g.runGame()