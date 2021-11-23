#game specification
# - 10 by 10 board, 100 spaces
# - 5 snakes
# - 5 ladders
# - 2 players
# - to start, players are off the board with first step on space no.1
# - to win, players must land exactly on space no.100. additional steps will bounce back

#techniques to use
# - encapsulation
# - inheritance (Obstacle as parent class; Snakes and Ladders as child class)


#PYGAME START-UP
import pygame
import random
import math
# -- Global Constants

# -- Colours
#board colours
BLACK = (0,0,0) 
WHITE = (255,255,255)
#player colours
ORANGE = (255,165,0)
BLUE = (50,50,255)
#snake colour:
GREEN = (0,128,0)
#ladder colour:
OAK = (187,129,65)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
x_size_screen = 1000
y_size_screen = 620 
size = (x_size_screen, y_size_screen) 
screen = pygame.display.set_mode(size)

# -- Title of new window/screen 
pygame.display.set_caption("Snakes and Ladders")

# -- Exit game flag set to false 
done = False


#class obstacles
class Obstacle:
    startList = []
    endList = []
    #ascending numbers as positive direction (e.g. 10 to 50)
    directionList = []

    #construct obstacle
    def __init__(self, start, end, direction):
        # Call the sprite constructor 
        super().__init__()

        # Set the position of the obstacle

        #QUESTION: start and end have different requirements for snakes and ladderse
        self.rect.start = random.randrange(0, ) 
        self.rect.end = random.randrange()

        #recreate invader starting coordinate if the new invader overlaps or is adjacent to a previously created invader
        obstacleNum = 5
        for obstacleNum in range (0, len(self.startList)):
            #checks if new inavder is adjacent or overlapping a previous invader
            while #no same start and end :
                #recreate obstacle
            #endwhile
        #next

        #add coordinate of new snowflake to coordinate lists
        self.startList.append(self.rect.start)
        self.endList.append(self.rect.end)
#end class


#class snakes
class Snakes(Obstacle):
    #snake constructor

    #move player method for snakes

#end class


#class ladders
class Ladders(Obstacle):
    #ladder constructor

    #move player method for ladders

#end class

#class player
class Player:
    #player constructor

    #move player method for players

#end class

class Dice:
    #can have different number of faces and dices

    #roll a random integer method

#endclass


#class board
class Board:
    #lists for everything on the board collectively
    everythingList = []
    #lists for everything on the board individually
    snakeList = []
    ladderList = []
    playerList= []    

    #board constructor

    #create obstacles

    # Create the snakes
    number_of_snakes = 5 # we are creating 10 invaders
    for x in range (number_of_snakes): 
        snakes = Snakes(#start, end, direction)
        everythingList.add (snakes) # adds the new invader to the group of invaders
        snakeList.add (snakes) # adds it to the group of all Sprites
    #Next x

#end class



# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()

##############################################           Game Loop           ##############################################
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
     
    # -- flip display to reveal new position of objects 
    pygame.display.flip()
    # - The clock ticks over 
    clock.tick(60) 
#End While - End of game loop
pygame.quit()