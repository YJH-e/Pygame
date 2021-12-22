import pygame 
# -- Global Constants 
# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255)
#RED = (255,0,0)
#GREEN = (0,255,0)
LAVA_ORANGE = (247, 70, 3)
#MOSS_GREEN = (70, 109, 29)
BLUE = (50,50,255) 

# -- Initialise PyGame
pygame.init() 
# -- Blank Screen
x_size_screen = 1200
y_size_screen = 800
size = (x_size_screen,y_size_screen) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("PacMan") 
# -- Exit game flag set to false 
done = False
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()



#mapLeft
mapLeft = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
[1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
[1,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0],
[1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,0,0,1,0],#row 5
[1,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
[1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0],
[1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
[1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0],#row 10
]


## -- Define the class tile which is a sprite 
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


class Game():
    def __init__(self):
        self.done = False

        # Create a list of all sprites 
        self.all_sprites_list = pygame.sprite.Group() 
        # Create a list of tiles for the walls 
        self.wall_list = pygame.sprite.Group()
        # Create walls on the screen (each tile is 20 x 20 so alter cords)
        ###note that y is vertical and x is horizontal, so this will create the map as it is in horizontal rows when it is read on paper
        for y in range(10): #column
            for x in range (20): #row
                if mapLeft[y][x] == 1: 
                    my_wall = tile(LAVA_ORANGE, 20, 20, x*20, y *20)
                    self.wall_list.add(my_wall) 
                    self.all_sprites_list.add(my_wall)
                #endif
            #next
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