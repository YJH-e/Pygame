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


#class obstacles
class Obstacle:
    startList = []
    endList = []
    #ascending numbers as positive direction (e.g. 10 to 50)
    directionList = []

    #construct obstacle
    def __init__(self):
        # Set the position of the obstacle
        #randomly generate the start and end of the obstacle
        self.start = random.randrange(1,99)
        self.end = random.randrange(1,99)
        #make sure that start and end are not the same square number
        if self.end == self.start:
            self.end = random.randrange(1,99)
        #endif

        #check if the start of end is already existing
        i = len(self.startList)
        if i > 0:
            j = 0
            for j in range (0,i):
                while self.start == self.startList[j] or self.start == self.end:
                    self.start = random.randrange(1,99)
                #endwhile
                while self.end == self.endList[j] or self.start == self.end:
                    self.end = random.randrange(1,99)
                #endwhile
            #next
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
class Players:
    #list holding all player position
    posOfPlayers = []

    #player constructor (initialises player position off the board at square  no.0)
    def __init__(self):
        self.posOfPlayers.append(0) #0 as in integer - more convenient maths
    #endfunction


    #move player method for players

#end class

class Dice:
    #can have different number of faces and dices/can later be a user input
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
        number_of_snakes = 5 # we are creating 5 snakes
        for x in range (number_of_snakes): 
            snakes = Snakes()
            self.snakeList.append(snakes)
            self.everythingList.append(snakes)
        #Next x
    #endprocedure

    # Create the ladders
    def createLadder(self):
        number_of_ladders = 5 # we are creating 5 ladders
        for x in range (number_of_ladders): 
            ladders = Ladders()
            self.ladderList.append(ladders)
            self.everythingList.append(ladders)
        #Next x
    #endprocedure

    # Create the players
    def createPlayer(self):
        number_of_players = 2 # we are creating 2 players
        for x in range (number_of_players): 
            players = Players()
            self.playerList.append(players)
            self.everythingList.append(players)
        #Next x
    #procedure

#end class





##############################################           Game Loop...see terminal           ##############################################

#no game logic at this point

b = Board()

b.createSnake()
b.createLadder()
b.createPlayer()

#if all starts and ends of both snakes and ladders are in Obstacle class, while the create snakes and ladders are in their own class, how do I print all snakes' and ladders' starts and ends individually?
