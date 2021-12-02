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

# -- Colours
#board colours
#BLACK = (0,0,0) 
#WHITE = (255,255,255)
#player colours
#ORANGE = (255,165,0)
#BLUE = (50,50,255)
#snake colour:
#GREEN = (0,128,0)
#ladder colour:
#OAK = (187,129,65)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
#x_size_screen = 1000
#y_size_screen = 620 
#size = (x_size_screen, y_size_screen) 
#screen = pygame.display.set_mode(size)

# -- Title of new window/screen 
#pygame.display.set_caption("Snakes and Ladders")

# -- Exit game flag set to false 
done = False


#class obstacles
class Obstacle:
    startList = []
    endList = []
    #ascending numbers as positive direction (e.g. 10 to 50)
    directionList = []

    #construct obstacle
    def __init__(self, start, end, direction, color):
        # Set the position of the obstacle

        #QUESTION: start and end have different requirements for snakes and ladders
        self.start = random.randrange(0, ) 
        self.end = random.randrange()

        #recreate obstacle starting coordinate if the new obstacle overlaps or is adjacent to a previously created invader
        #obstacleNum = 5
        #for obstacleNum in range (0, len(self.startList)):
            #checks if new obstacle is adjacent or overlapping a previous invader
            #while #no same start and end :
                #recreate obstacle
            #endwhile
        #next

        #add coordinate of new obstacle to coordinate lists
        self.startList.append(self.start)
        self.endList.append(self.end)
    #endfunction
#end class


#class snakes
class Snakes(Obstacle):
    #snake constructor
    #construct obstacle
    def __init__(self):



        #QUESTION: start and end have different requirements for snakes and ladders
        self.start = random.randrange(2, 99) 
        self.end = random.randrange(1, self.start)

        #recreate obstacle starting coordinate if the new obstacle overlaps or is adjacent to a previously created obstacle
        snakeNum = 0
        for snakeNum in range (0, len(self.startList)):
            #checks if new obstacle is adjacent or overlapping a previous invader
            while self.start == self.startList(snakeNum):
                #recreate obstacle start
                self.start = random.randrange(2, 99)
            #endwhile
            while self.end == self.endList(snakeNum):
                #recreate obstacle start
                self.end = random.randrange(1, self.start)
            #endwhile
        #next

        #add coordinate of new obstacle to coordinate lists
        self.startList.append(self.start)
        self.endList.append(self.end)
    #endfunction

    #move player method for snakes

#end class


#class ladders
class Ladders(Obstacle):
    #ladder constructor
    #construct obstacle
    def __init__(self):


        #QUESTION: start and end have different requirements for snakes and ladders
        self.start = random.randrange(1, 99) 
        self.end = random.randrange(self.start, 100)

        #recreate obstacle starting coordinate if the new obstacle overlaps or is adjacent to a previously created obstacle
        ladderNum = 0
        for ladderNum in range (0, len(self.startList)):
            #checks if new obstacle is adjacent or overlapping a previous invader
            while self.start == self.startList(ladderNum):
                #recreate obstacle start
                self.start = random.randrange(1, 99) 
            #endwhile
            while self.end == self.endList(ladderNum):
                #recreate obstacle start
                self.end = random.randrange(self.start, 100)
            #endwhile
        #next

        #add coordinate of new obstacle to coordinate lists
        self.startList.append(self.rect.start)
        self.endList.append(self.rect.end)
    #endfunction

    #move player method for ladders

#end class

#class player
class Player:
    #player constructor
    def __init__(self):
        self.pos = 0
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