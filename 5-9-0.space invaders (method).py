#PYGAME START-UP

import pygame
import random
import math



# -- Exit game flag set to false 
done = False

#initialise all variables inside Game class (except done)
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
# -- Initialise PyGame
pygame.init() 
# -- Blank Screen
x_size = 1000
y_size = 620
size = (x_size,y_size) 


## -- Define the class invader which is a sprite 
class Invader(pygame.sprite.Sprite):
    # Create a list of x and y_coordinates of invaders
    x_co = []
    y_co = []

    # Define the constructor for invader
    def __init__(self, width, height, speed):
        # Call the sprite constructor 
        super().__init__()
        #create a sprite and put a picture on it
        invImage = pygame.image.load('invader.png')
        self.image = pygame.transform.scale(invImage, (width, height))
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = random.randrange(0, x_size - 40) 
        self.rect.y = random.randrange(-50, 0)

        #recreate invader starting coordinate if the new invader overlaps or is adjacent to a previously created invader
        invNum = 0
        for invNum in range (0, len(self.x_co)):
            #checks if new inavder is adjacent or overlapping a previous invader
            while self.rect.x <= self.x_co[invNum] + 40 and self.rect.x >= self.x_co[invNum] - 40 and self.rect.y <= self.y_co[invNum] + 40 and self.rect.y >= self.y_co[invNum] - 40:
                self.rect.x = random.randrange(0, x_size - 40) 
                self.rect.y = random.randrange(-50, 0)
            #endwhile
        #next

        #add coordinate of new snowflake to coordinate lists
        self.x_co.append(self.rect.x)
        self.y_co.append(self.rect.y)

        # Set speed of the sprite 
        self.speed = speed
    #End Procedure
    
    # Class update function - runs for each pass through the game loop 
    def update(self): 
        self.rect.y = self.rect.y + self.speed
        #make snowflake reappear on top of screen after falling pass bottom
        if self.rect.y > y_size:
            self.rect = self.image.get_rect() 
            self.rect.x = random.randrange(0, x_size - 40) 
            self.rect.y = random.randrange(-100, 0)

            #recreate invader starting coordinate if the new invader overlaps or is adjacent to a previously created invader
            invNum = 0
            for invNum in range (0, len(self.x_co)):
                #checks if new inavder is adjacent or overlapping a previous invader
                while self.rect.x <= self.x_co[invNum] + 40 and self.rect.x >= self.x_co[invNum] - 40 and self.rect.y <= self.y_co[invNum] + 40 and self.rect.y >= self.y_co[invNum] - 40:
                    self.rect.x = random.randrange(0, x_size - 40) 
                    self.rect.y = random.randrange(-100, 0)
                #endwhile
            #next
        #endif
    #endprocedure
#End Class

## -- Define the class player which is a sprite 
class Player(pygame.sprite.Sprite):
    # Define the constructor for player
    def __init__(self, width, height):
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and put a picture on it
        playerImage = pygame.image.load('player.png')
        self.image = pygame.transform.scale(playerImage, (width, height))
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        self.rect.x = 300 
        self.rect.y = y_size - 100
        self.x_speed = 0

        self.score = 50
        self.lives = 5
        self.bullets = 50
        self.width = width
        self.height = height

    #End Procedure
    
    # Class update function - runs for each pass through the game loop 
    def update(self):
        #keep player within screen while moving player
        if (self.rect.x >= 3 and self.rect.x <= x_size - 3 - self.width) or (self.rect.x <= 3 and self.x_speed > 0) or (self.rect.x >= x_size - 3 - 40 and self.x_speed < 0):
            self.rect.x = self.rect.x + self.x_speed
        #endif
    #endprocedure
#End Class


## -- Define the class bullet which is a sprite 
class Bullet(pygame.sprite.Sprite):
    # create bullet firing position
    x_pos = 300

    # Define the constructor for bullets
    def __init__(self, color, width, height, x_pos, x_speed):
        # Call the sprite constructor 
        super().__init__() 
        # Create a sprite and fill it with colour 
        self.image = pygame.Surface([width,height]) 
        self.image.fill(color) 
        # Set the position of the sprite 
        self.rect = self.image.get_rect() 
        if x_pos == None and x_speed < 0:
            x_pos = 0
        elif x_pos == None and x_speed > 0:
            x_pos = x_size - 5
        #endif

        self.rect.x = x_pos
        self.rect.y = y_size - 100

    #End Procedure
    
    # Class update function - runs for each pass through the game loop 
    def update(self):
        #keep player within screen while moving player
        self.rect.y = self.rect.y - 7

        #endif
    #endprocedure
#End Class

class Game():
    
    def __init__(self):
        # Create a list of all sprites 
        self.all_sprites_group = pygame.sprite.Group()
    
        # Create a list of the snow blocks 
        self.invader_group = pygame.sprite.Group()

        #create a list of all bullets
        self.bullet_group = pygame.sprite.Group()

        self.screen = pygame.display.set_mode(size)

        
        #text display
        self.font = pygame.font.SysFont("monospace", 15)
        self.fontEnd = pygame.font.SysFont("monospace", 25)

        #initialise life for player
        self.life = 5

        #initialise score of player
        self.score = 0

        #intialise number of bullets
        self.bullet_count = 0
        self.bullet_fired = False

        #initialise position where bullets are fired
        self.x_pos = 300

        #initialise x_speed (for player) to check where player is on screen
        self.x_speed = 0

        # Create the invaders       
        number_of_invaders = 10 # we are creating 10 invaders
        for x in range (number_of_invaders): 
            self.invaders = Invader(40, 50, 1)
            self.invader_group.add (self.invaders) # adds the new invader to the group of invaders
            self.all_sprites_group.add (self.invaders) # adds it to the group of all Sprites
        #Next x

        # Create the player

        number_of_players = 1 # we are creating 10 invaders
        for y in range (number_of_players):
            self.player = Player(40, 50) # snowflakes are white with size 5 by 5 px
            self.all_sprites_group.add (self.player) # adds it to the group of all Sprites
        #Next y
    #end procedure
  

    def keyPress(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            elif event.type == pygame.KEYDOWN: # - a key is down 
                if event.key == pygame.K_LEFT: # - if the left key pressed 
                    self.x_speed = -3 # speed set to -3
                elif event.key == pygame.K_RIGHT: # - if the right key pressed
                    self.x_speed = 3 # speed set to 3
                elif event.key == pygame.K_p: #stop player
                    self.x_speed = 0
                elif event.key == pygame.K_SPACE: # fire bullets
                    if self.bullet_count > 49:
                        pass
                    else:
                        bullet_fired = True
                        bullet = Bullet(RED,5,15, self.x_pos, self.x_speed)
                        self.all_sprites_group.add(bullet)
                        self.bullet_group.add(bullet)
                        self.bullet_count += 1
                    #endif
                #endif
            #End If
        #Next event
    #end function

    def logic(self):
        # -- Game logic goes in here 
        self.all_sprites_group.update()



        # Game logic of player hitting invader
        # -- when player hits invader, deduct life by 1. 
        player_hit_list = pygame.sprite.spritecollide(self.player, self.invader_group, True)
        for h in player_hit_list:
            self.life = self.life - 1
        #next
        # -- when bullet hits invader, add 5 to score.
        if self.bullet_fired == True:
            bullet_hit_list = pygame.sprite.groupcollide(self.bullet, self.invader_group, True, True)
            for h in bullet_hit_list:
                self.score = self.score + 5     
             #next
        #endif

        # -- Screen background is BLACK 
        self.screen.fill(BLACK) 
        # -- Drawing code goes here
        self.all_sprites_group.draw(self.screen)
    #endprocedure


    def scoreBoard(self):
        scoreDisplay = self.font.render("score: " + str(self.score), 1, WHITE)
        self.screen.blit(scoreDisplay,(20, 20))
        bulletDisplay = self.font.render("bullets left: " + str(50 - self.bullet_count), 1, WHITE)
        self.screen.blit(bulletDisplay,(20, 40))
        lifeDisplay = self.font.render("life left: " + str(self.life), 1, WHITE)
        self.screen.blit(lifeDisplay,(20, 60))
        if self.score == 50 or self.score == 50 - (5-self.life)*5:
            endGame = self.fontEnd.render("Thank you for playing space invaders.", 1, ORANGE)
            endGame_rect = endGame.get_rect(center = (x_size/2, y_size/2 - 25))
            self.screen.blit(endGame,endGame_rect)
            endGame2 = self.fontEnd.render("Your victory has saved your planet.", 1, ORANGE)
            endGame2_rect = endGame2.get_rect(center = (x_size/2, y_size/2 + 25))
            self.screen.blit(endGame2, endGame2_rect)
        #endif
    #end procedure

#End Class


############################################################### GAME LOOP ###############################################################
g = Game()
# PYGAME LOOP

while not done:
    # -- Title of new window/screen 
    pygame.display.set_caption("Space Invaders")

    #keyPress that closes window or moves player or fire bullets
    g.keyPress()

    #game logic that calculates player's life, bullets and collisions and scores
    g.logic()
    
    #display score, number of bullets and lives on upper left corner of screen
    g.scoreBoard()

    # -- flip display to reveal new position of objects 
    pygame.display.flip()

    # -- Manages how fast screen refreshes 
    clock = pygame.time.Clock()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop 
pygame.quit()### -- Game Loop