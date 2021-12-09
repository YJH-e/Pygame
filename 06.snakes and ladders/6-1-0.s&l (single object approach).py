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
        start = random.randrange(1,98)
        end = random.randrange(start + 1,99)
        #check if the start of end is already existing                         #this piece of code (in the function) is quite inefficient with O(n^2)
        i = len(self.allList)
        if i > 0:
            j = 0
            for j in range (0,i):
                while start == self.allList[j]:
                    start = random.randrange(1,98)
                #endwhile
                while end == self.allList[j]:
                    end = random.randrange(start + 1,99)
                #endwhile
            #next
        #endif
        #add coordinate of new obstacle to coordinate lists
        self.allList.append(start)
        self.allList.append(end)
        return start, end
        #next                
    #endfunction
#end class

#class Snake (single object)
class Snake(Obstacle):
    start = 0
    end = 0

    #snake constructor is in obstacle constructor
    def __init__(self):
        self.end, self.start = super().__init__()
    #endfunction

    #get start of snake
    def getStartSnake(self):
        return self.start
    #endfunction

    def getEndSnake(self):
        return self.end
    #endfunction

    #def displaySnake(self):
        #print(self.start, self.end)
    #endprocedure
#end class

#class Ladder (single object)
class Ladder(Obstacle):
    start = 0
    end = 0

    #snake constructor is in obstacle constructor
    def __init__(self):
        self.start, self.end = super().__init__()
    #endfunction

    #get start of snake
    def getStartLadder(self):
        return self.start
    #endfunction

    def getEndLadder(self):
        return self.end
    #endfunction

    #def displayLadder(self):
        #print(self.start, self.end)
    #endprocedure
#end class

#class Player
class Player():
    #list holding all player position
    posOfPlayer = 0
    nameOfPlayer = ""

    #player constructor (initialises player position off the board at square  no.0)
    def __init__(self, name):
        self.posOfPlayer = 0
        nameOfPlayer = name
    #endfunction

    #get player position
    def getPlayerPos(self):
        return self.posOfPlayer
    #endfunction

    #get player name
    def getPlayerName(self):
        return self.nameOfPlayer
    #endfunction
#end class

#class Dice
class Dice():
    #can have different number of faces and dices/can later be a user input
    diceFace = 6
    
    #roll a random integer method
    def roll(self):
        return random.randrange(1, self.diceFace) 
    #endfuntion
#endclass

#class Game
class Game():
    snakesStartList = []
    snakesEndList = []
    laddersStartList = []
    laddersEndList = []
    playersPosList = []
    playersNameList = []
    

    # Create a snake 5 times 
    def createSnake(self):
        number_of_snakes = 5 # we are creating 5 snakes
        x = 0
        for x in range (0, number_of_snakes):
            s = Snake()
            self.snakesStartList.append(s.getStartSnake())
            self.snakesEndList.append(s.getEndSnake())
        #Next
    #endprocedure

    # Create a ladder 5 times   
    def createLadder(self):
        number_of_ladders = 5 # we are creating 5 ladders
        y = 0
        for y in range (0, number_of_ladders):
            l = Ladder()
            self.laddersStartList.append(l.getStartLadder())
            self.laddersEndList.append(l.getEndLadder())
        #Next
    #endprocedure

    def createPlayer(self):
        p1 = Player("Player A")
        self.playersPosList.append(p1.getPlayerPos())
        self.playersNameList.append("Player A")
        p2 = Player("Player B")
        self.playersPosList.append(p2.getPlayerPos())
        self.playersNameList.append("Player B")

    def display(self):
        print("Below are the start square numbers of snakes")
        s1 = 0
        for s1 in range (0, len(self.snakesStartList)):
            print(self.snakesStartList[s1])
        #next
        print("Below are the end square numbers of snakes")
        s2 = 0
        for s2 in range (0, len(self.snakesEndList)):
            print(self.snakesEndList[s2])
        #next
        print("Below are the start square numbers of ladders")
        l1 = 0
        for l1 in range (0, len(self.laddersStartList)):
            print(self.laddersStartList[l1])
        #next
        print("Below are the end square numbers of ladders")
        l2 = 0
        for l2 in range (0, len(self.laddersEndList)):
            print(self.laddersEndList[l2])
        #next
        print("Below are the names of the players")
        p1 = 0
        for p1 in range (0, len(self.playersNameList)):
            print(self.playersNameList[p1])
        #next
        print("Below are the start square numbers of the players")
        p2 = 0
        for p2 in range (0, len(self.playersPosList)):
            print(self.playersPosList[p2])
        #next
    #endprocedure
#endclass



g = Game()
g.createSnake()
g.createLadder()
g.createPlayer()
g.display()