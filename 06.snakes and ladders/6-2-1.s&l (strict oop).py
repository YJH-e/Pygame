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
    #player constructor (initialises player position off the board at square  no.0)
    def __init__(self):
        self.posOfPlayer = 0
    #endfunction

    #get player position
    def getPlayerPos(self):
        return self.posOfPlayer
    #endfunction
#end class

#class Dice
class Dice():
    #roll a random integer method
    def roll(self):
        self.diceFace = 6
        return int(random.randrange(1, self.diceFace) )
    #endfuntion
#endclass

#class Game
class Game():
    def __init__(self):
        self.snakesStartList = []
        self.snakesEndList = []
        self.laddersStartList = []
        self.laddersEndList = []
        self.playersPosList = []
        self.playersNameList = []

        #create snakes
        number_of_snakes = 5 # we are creating 5 snakes
        x = 0
        for x in range (0, number_of_snakes):
            s = Snake()
            self.snakesStartList.append(s.getStartSnake())
            self.snakesEndList.append(s.getEndSnake())
        #Next

        #create ladders
        number_of_ladders = 5 # we are creating 5 ladders
        y = 0
        for y in range (0, number_of_ladders):
            l = Ladder()
            self.laddersStartList.append(l.getStartLadder())
            self.laddersEndList.append(l.getEndLadder())
        #Next

        #create players
        p1 = Player()
        self.playersPosList.append(p1.getPlayerPos())
        self.playersNameList.append("Player A")
        p2 = Player()
        self.playersPosList.append(p2.getPlayerPos())
        self.playersNameList.append("Player B")
    #endprocedure

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

    def playGame(self):
        #create just 1 dice object so that it can be rolled later
        d = Dice()
        #flag of any one of the players winning
        win = False
        #actual game starts here
        while win  == False:
            p = 0
            for p in range (0, len(self.playersNameList)):
                #roll dice and add to player position (as square number)       
                r = d.roll()
                #use the created object dice and roll it
                self.playersPosList[p] = self.playersPosList[p] + r
                print(self.playersNameList[p], "rolled a", r, "and is now on square number", self.playersPosList[p])
                #checks if player position is greater than 100, i.e. passed the finish line too far, rebounce player
                if self.playersPosList[p] > 100:
                    #calculate rebounce
                    difference = self.playersPosList[p] - 100
                    self.playersPosList[p] = 100 - difference
                    print(self.playersNameList[p], "has went over 100 and has rebounced back to square number",self.playersPosList[p])
                elif self.playersPosList[p] == 100:
                    win = True
                    print(self.playersNameList[p], "has won")
                    print("Game Ends")
                #endif
                else:
                    #flag of player hitting snake
                    hitSnake = False
                    s = 0
                    #checks if player has hit snake
                    while s < len(self.snakesStartList) and hitSnake != True:
                        if self.playersPosList[p] == self.snakesStartList[s]:
                            hitSnake = True
                            print(self.playersNameList[p], "has hit a snake that spans from", self.snakesStartList[s], "to", self.snakesEndList[s])
                            self.playersPosList[p] = self.snakesEndList[s]
                            print(self.playersNameList[p], "is on square number", self.playersPosList[p])
                        #endif
                        s += 1
                    #endwhile
                    #flag of player hitting ladder
                    hitLadder = False
                    l = 0
                    #checks if player has hit ladder
                    while l < len(self.laddersStartList) and hitLadder != True:
                        if self.playersPosList[p] == self.snakesStartList[l]:
                            hitLadder = True
                            print(self.playersNameList[p], "has hit a ladder that spans from", self.laddersStartList[l], "to", self.laddersEndList[l])
                            self.playersPosList[p] = self.laddersEndList[l]
                            print(self.playersNameList[p], "is on square number", self.playersPosList[p])
                        #endif
                        l += 1
                    #endwhile
                #endif
            #next player
        #endwhile
    #endprocedure
#endclass


#main program
g = Game()
g.display()
g.playGame()