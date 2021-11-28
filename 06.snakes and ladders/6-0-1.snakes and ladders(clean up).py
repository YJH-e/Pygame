#game specification
# - 10 by 10 board, 100 spaces
# - 5 snakes
# - 5 ladders
# - 2 players
# - to start, players are off the board with first step on space no.1
# - to win, players must land exactly on space no.100. additional steps will bounce back

#this game has no graphics

#techniques to use
# - encapsulation; OOP
# - inheritance (Obstacle as parent class; Snakes and Ladders as child class)


#PYGAME START-UP
import pygame
import random
import math
# -- Global Constants

# -- Initialise PyGame
pygame.init()

# -- Exit game flag set to false 
done = False


#class obstacles
class Obstacle:
    startList = []
    endList = []
    #ascending numbers as positive direction (e.g. 10 to 50)
    directionList = []

    #number of obstacles created by iteration (can later be a user input)
    numOfObstacle = 5

    #construct obstacle
    def __init__(self, numOfObstacle):
        # Set the position of the obstacle
        for i in range(0, numOfObstacle):
            #randomly generate the start and end of the obstacle
            self.start = random.randrange(1,99)
            self.end = random.randrange(1,99)
            #make sure that start and end are not the same square number
            if self.end == self.start:
                self.end = random.randrange(1,99)
            #endif

            #check if the start of end is already existing
            if i > 0:
                while self.start == self.startList[i] or self.start == self.end:
                    self.start = random.randrange(1,99)
                #endwhile
                while self.end == self.endList[1] or self.start == self.end:
                    self.end = random.randrange(1,99)
                #endwhile
            #endif

            #add coordinate of new obstacle to coordinate lists
            self.startList.append(self.start)
            self.endList.append(self.end)
        #next                
    #endfunction
#end class


#class snakes
class Snakes(Obstacle):
    #snake constructor continuing obstacle constructor
    def __init__(self):
        super().__init__()
        self.direction = -1
    #endfunction

    #move player method for snakes

#end class


#class ladders
class Ladders(Obstacle):
    #ladder constructor continuing ladder constructor
    def __init__(self):
        super().__init__()
        self.direction = 1
    #endfunction

    #move player method for ladders

#end class

#class player
class Player:
    #number of players (can later be a user input)
    numOfPlayers = 2
    posOfPlayers = []

    #player constructor (initialises player position off the board at square  no.0)
    def __init__(self, numOfPlayers, posOfPlayers):
        for i in range (0, numOfPlayers):
            posOfPlayers[i] = 0
    #endfunction


    #move player method for players

#end class

class Dice:
    #can have different number of faces and dices
    diceFace = 6
    
    #roll a random integer method
    def roll(self):
        self.diceNum = random.randrange(1, self.diceFace)
        return self.diceNum   
    #endfuntion

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

    # Create the snakes
    def createSnake(self):
        number_of_snakes = 5 # we are creating 10 invaders
        for x in range (number_of_snakes): 
            snakes = Snakes(#start, end, direction)
            #snakeList.append(snakes)
            self.everythingList.append(snakes)
        #Next x

    #procedure

    # Create the ladders
    def createLadder(self):
        number_of_ladders = 5 # we are creating 10 invaders
        for x in range (number_of_ladders): 
            ladders = Ladders(#start, end, direction)
            #ladderList.append(ladders)
            self.everythingList.append(ladders)
        #Next x
    #procedure

    # Create the players
    def createPlayer(self):
        number_of_players = 2 # we are creating 10 invaders
        for x in range (number_of_players): 
            players = Players(#start, end, direction)
            #playerList.append(players)
            self.everythingList.append(players)
        #Next x
    #procedure

#end class



# -- Manages how fast screen refreshes 
#clock = pygame.time.Clock()

##############################################           Game Loop           ##############################################
b = Board()
while done == True: 
    # -- User input and controls
    #for event in pygame.event.get(): 
        #if event.type == pygame.QUIT: 
            #done = True 
        #End If
    #Next event
    # -- Game logic goes after this comment
    b.createSnake()
    b.createLadder()
    b.createPlayer()








    


    # -- Screen background is BLACK 
    #screen.fill (BLACK) 
    # -- Draw here 
     
    # -- flip display to reveal new position of objects 
    #pygame.display.flip()
    # - The clock ticks over 
    #clock.tick(60) 
#End While - End of game loop
#pygame.quit()