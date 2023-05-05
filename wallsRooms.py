"""
This files deals with the layout of the maze, along with creating each individual room.

"""



import pygame
from colors import *
 
#Inherits the sprite class
class Wall(pygame.sprite.Sprite): 
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color):
 
        # Call the parent's constructor
        super().__init__()
 
        #Creates a colored wall based on given width/height
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 

 
#Inherits the object class
class Room(object):
    """Parent class for all rooms"""
 
    #Each room has a list of walls, and of enemy sprites.
    wallsList = None
    enemy_sprites = None
 
    def __init__(self):
        self.wallsList = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
 
 
class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE], #All of these 6 white walls are for the "base" of an empty room
                 [20, 0, 760, 20, WHITE], #Any walls underneath the white walls are extras
                 [20, 580, 760, 20, WHITE], 
                 [190, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
 
 
class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()

        #[x, y, width, height, color]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE], #All of these 6 white walls are for the "base" of an empty room
                 [20, 0, 760, 20, WHITE], #Any walls underneath the white walls are extras
                 [20, 580, 760, 20, WHITE], 
                 [190, 50, 20, 500, BLUE],
                 [290, 50, 20, 500, PURPLE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
 
 
class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
         
         #[x, y, width, height, color]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE], #All of these 6 white walls are for the "base" of an empty room
                 [20, 0, 760, 20, WHITE], #Any walls underneath the white walls are extras
                 [20, 580, 760, 20, WHITE], 
                 [190, 50, 20, 500, BLUE],
                 [290, 50, 20, 500, PURPLE],
                 [390, 50, 20, 500, GREEN]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)


#Copy-paste more rooms when necessary
#Do not forget to update main.py whenever adding new rooms (starting line 83)