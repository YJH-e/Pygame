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
# -- Global Constants

# -- Initialise PyGame
pygame.init()


#class obstacles
class Obstacle(Game):
    #the allList contains every start and end square number generated by the random integer generater, so that no start or end number will have the same square number.
    allList = []

    #construct obstacle
    def __init__(self):
        # Set the position of the obstacle
        #randomly generate the start and end of the obstacle
        self.start = random.randrange(1,98)
        self.end = random.randrange(self.start + 1,99)

        #check if the start of end is already existing                         #this piece of code (in the function) is quite inefficient with O(n^2)
        i = len(self.allList)
        if i > 0:
            j = 0
            for j in range (0,i):
                while self.start == self.allList[j]:
                    self.start = random.randrange(1,98)
                #endwhile
                while self.end == self.allList[j]:
                    self.end = random.randrange(self.start + 1,99)
                #endwhile
            #next
        #endif
        #add coordinate of new obstacle to coordinate lists
        self.allList.append(self.start)
        self.allList.append(self.end)
        #next                
    #endfunction
#end class


#class snakes
class Snakes(Obstacle, Game):
    #Snakes' own list of holding all its start square numbers
    startListSnakes = []
    #Snakes' own list of holding all its end square numbers
    endListSnakes = []

    #snake constructor is in obstacle constructor
    def __init__(self):
        super().__init__()
        self.startListSnakes.append(self.end)
        self.endListSnakes.append(self.start)
    #endfunction

    #get start of snake
    def getStartSnakes(self):

    
    #endfunction

    def getEndSnakes(self):
    
    #endfunction

    #identify which snake start square the player has landed on, using player position from class Player
    def identifySnake(self):
        p = Players()
        playerPos = Players.getplayerpos()

    #endfunction


    #move player method for snakes

#end class


#class ladders
class Ladders(Obstacle, Game):
    #Ladders' own list of holding all its start square numbers
    startListLadders = []
    #Ladders' own list of holding all its start square numbers
    endListLadders = []
    #ladder constructor is in ladder constructor
    def __init__(self):
        super().__init__()
        self.startListLadders.append(self.start)
        self.endListLadders.append(self.end)
    #endprocedure


    def getStart(self):
    
    #endfunction

    def getEnd(self):
    
    #endfunction


    #move player method for ladders

#end class

#class player
class Players(Game):
    #list holding all player position
    posOfPlayers = []

    playerName = ""

    #player constructor (initialises player position off the board at square  no.0)
    def __init__(self):
        self.posOfPlayers.append(0) #0 as in integer - more convenient maths
    #endfunction

    #set player position
    def getPlayerPos(self, playerNum): #playerNum is the identifier that is unique to each player
        playerPos = self.posOfPlayers(playerNum)
        return playerPos
    #endfunction


    


    #move player method for players

#end class

class Dice(Game):
    #can have different number of faces and dices/can later be a user input
    diceFace = 6
    
    #roll a random integer method
    def roll(self):
        self.diceNum = random.randrange(1, self.diceFace)
        return self.diceNum   
    #endfuntion

#endclass


#class board
class Board(Game):
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

class Game:
    #need some attributes (lists) from Board class
#endclass





##############################################           Game display...see terminal           ##############################################

#no game logic at this point

#create all snakes, ladders and players at initial position
b = Board()
b.createSnake()
b.createLadder()
b.createPlayer()

#display all start square numbers for snakes
print("Below are all start square numbers for snakes")
for num1 in range (0, len(Snakes.startListSnakes)):
    print(Snakes.startListSnakes[num1])
#next

#display all end square numbers for snakes
print("Below are all end square numbers for snakes")
for num2 in range (0, len(Snakes.endListSnakes)):
    print(Snakes.endListSnakes[num2])
#next

#display all start square numbers for ladders
print("Below are all start square numbers for ladders")
for num3 in range (0, len(Ladders.startListLadders)):
    print(Ladders.startListLadders[num3])
#next

#display all end square numbers for ladders
print("Below are all end square numbers for ladders")
for num4 in range (0, len(Ladders.startListLadders)):
    print(Ladders.endListLadders[num4])
#next

#display all positions as in square number of players
print("Below are all positions as in square number of players")
for num5 in range (0, len(Players.posOfPlayers)):
    print(Players.posOfPlayers[num5])
#next