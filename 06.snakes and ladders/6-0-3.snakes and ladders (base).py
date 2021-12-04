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

#notes
# - to find length of a list or string: len()
# - to access an item in a list: list[]
# - to call a subroutine: subroutineName()
# - when programming OOP, you create the class, but use an object to perform the methods from the class on (e.g. g = Game() // g.playGame())

#PYGAME START-UP
import pygame
import random
# -- Global Constants

# -- Initialise PyGame
pygame.init()

#class obstacles
class Obstacle():
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
class Snakes(Obstacle):
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
    def getStartSnakesList(self):
        return self.startListSnakes
    #endfunction

    def getEndSnakesList(self):
        return self.endListSnakes 
    #endfunction
#end class

#class ladders
class Ladders(Obstacle):
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


    def getStartLaddersList(self):
        return self.startListLadders  
    #endfunction

    def getEndLaddersList(self):
        return self.endListLadders
    #endfunction


    #move player method for ladders
#end class

#class player
class Players():
    #list holding all player position
    posOfPlayers = []
    nameOfPlayers = ["Player A", "Player B"]

    #player constructor (initialises player position off the board at square  no.0)
    def __init__(self):
        self.posOfPlayers.append(0) #0 as in integer - more convenient maths
    #endfunction

    #get player position
    def getPlayerPos(self):
        return self.posOfPlayers
    #endfunction

    #get player name
    def getPlayerNames(self):
        return self.nameOfPlayers
    #endfunction
#end class

class Dice():
    #can have different number of faces and dices/can later be a user input
    diceFace = 6
    
    #roll a random integer method
    def roll(self):
        return random.randrange(1, self.diceFace) 
    #endfuntion
#endclass

#class board
class Board():
    #lists for everything on the board collectively
    everythingList = []
    #lists for everything on the board individually
    snakeList = []
    ladderList = []
    playerList= []

    #list for details of everything on the board individually
    startListSnakes = []
    endListSnakes = []
    startListLadders = []
    endListLadders = []
    posOfPlayers = []
    nameOfPlayers = []    

    #board constructor
    def __init__(self):
        self.startListSnakes, self.endListSnakes = Board.createSnake
        self.startListLadders, self.endListLadders = Board.createLadder
        self.posOfPlayers, self.nameOfPlayers = Board.createPlayer
        Board.displayBoard
    #endprocedure

    # Create the snakes
    def createSnake(self):
        number_of_snakes = 5 # we are creating 5 snakes
        for x in range (number_of_snakes): 
            snakes = Snakes()
            self.snakeList.append(snakes)
            self.everythingList.append(snakes)
        #Next x
        return Snakes.startListSnakes, Snakes.endListSnakes
    #endprocedure

    # Create the ladders
    def createLadder(self):
        number_of_ladders = 5 # we are creating 5 ladders
        for x in range (number_of_ladders): 
            ladders = Ladders()
            self.ladderList.append(ladders)
            self.everythingList.append(ladders)
        #Next x
        return Ladders.startListLadders, Ladders.endListLadders
    #endprocedure

    # Create the players
    def createPlayer(self):
        number_of_players = 2 # we are creating 2 players
        for x in range (number_of_players): 
            players = Players()
            self.playerList.append(players)
            self.everythingList.append(players)
        #Next x
        return Players.posOfPlayers, Players.nameOfPlayers
    #procedure

    def displayBoard(self):
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
    #endprocedure

    def getAllLists(self):
        return self.startListSnakes, self.endListSnakes, self.startListLadders, self.endListLadders, self.posOfPlayers, self.nameOfPlayers
    #endfunction
#end class

class Game():
    #private variable that copies the start and end lists from class Snakes and Ladders, and position list from class Players
    #is this memory inefficient? but this would be safer in case the contents of the lists are altered in the Game class.
    startListSnakes = []
    endListSnakes = []
    startListLadders = []
    endListLadders = []
    posOfPlayers = []
    nameOfPlayers = []

    #flag of initialising Game (get all lists above required)
    listObtained = False

    def playGame(self):
        #initialise board
        b = Board()
        while self.listObtained == False:
                self.startListSnakes, self.endListSnakes, self.startListLadders, self.endListLadders, self.posOfPlayers, self.nameOfPlayers = b.getAllLists()
                self.listObtained = True
        #endwhile
        #flag of any one of the players winning
        win =False
        while win != True:
            for p in self.nameOfPlayers:
                #roll dice and add to player position (as square number)
                d = Dice()
                r = d.roll
                #use the created object dice and roll it
                self.posOfPlayers[p] += r
                print(self.nameOfPlayers[p], "rolled a ", r, "and is now on square numebr ", self.posOfPlayers[p])
                #checks if player position is greater than 100, i.e. passed the finish line too far, rebounce player
                if self.posOfPlayers[p] > 100:
                    #calculate rebounce
                    difference = self.posOfPlayers[p] - 100
                    self.posOfPlayers[p] = 100 - difference
                    print(self.nameOfPlayers[p], " has went over 100 and has rebounced back to square number ",self.posOfPlayers[p])
                elif self.posOfPlayers[p] == 100:
                    win = True
                    print(self.nameOfPlayers[p], " has won")
                    print("Game Ends")
                #endif
                else:
                    #flag of player hitting snake
                    hitSnake = False
                    s = 0
                    #checks if player has hit snake
                    while s != len(self.startListSnakes) or hitSnake != True:
                        if self.posOfPlayers[p] == self.startListSnakes[s]:
                            hitSnake = True
                            print(self.nameOfPlayers[p], " has hit a snake that spans from ", self.startListSnakes[s], " to ", self.endListSnakes[s])
                            self.posOfPlayers[p] == self.endListSnakes[s]
                            print(self.nameOfPlayers[p], " is on square number ", self.posOfPlayers[p])
                        #endif
                        s += 1
                    #endwhile
                    #flag of player hitting ladder
                    hitLadder = False
                    l = 0
                    #checks if player has hit ladder
                    while l != len(self.startListLadders) or hitLadder != True:
                        if self.posOfPlayers[p] == self.startListSnakes[l]:
                            hitLadder = True
                            print(self.nameOfPlayers[p], " has hit a ladder that spans from ", self.startListLadders[l], " to ", self.endListLadders[l])
                            self.posOfPlayers[p] == self.endListLadders[l]
                            print(self.nameOfPlayers[p], " is on square number ", self.posOfPlayers[p])
                        #endif
                        l += 1
                    #endwhile
                #endif
            #next player
        #endwhile
    #endprocedure
#endclass



##############################################           Game display...see terminal           ##############################################
g = Game()
g.playGame