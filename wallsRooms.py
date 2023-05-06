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

 
# START ROOM
class RoomStart(Room):
    """This creates all the walls in room"""  
    def __init__(self, num):
        super().__init__()
        self.num = num
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 800, 20, WHITE], #top

                 [0, 0, 20, 600, WHITE], #left

                 [780, 0, 20, 600, WHITE], #right

                 [20, 580, 320, 20, WHITE], #bottom
                 [450, 580, 330, 20, WHITE], 
                
                 [190, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

# 4 WALLS ROOM
class RoomFull(Room):
    """This creates all the walls in room"""  
    def __init__(self, num):
        super().__init__()
        self.num = num
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, WHITE], #top
                 [450, 0, 330, 20, WHITE],

                 [0, 0, 20, 250, WHITE], #left
                 [0, 350, 20, 250, WHITE],

                 [780, 0, 20, 250, WHITE], #right
                 [780, 350, 20, 250, WHITE],

                 [20, 580, 320, 20, WHITE], #bottom
                 [450, 580, 330, 20, WHITE], 
                
                 [190, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
 
# FULL TOP ROOM
class RoomFullTop(Room):
    """This creates all the walls in room 3"""
    def __init__(self, num):
        super().__init__()
        self.num = num
         #[x, y, width, height, color]
        walls = [[20, 0, 600, 20, WHITE], #top

                 [0, 0, 20, 250, WHITE], #left
                 [0, 350, 20, 250, WHITE],

                 [780, 0, 20, 250, WHITE], #right
                 [780, 350, 20, 250, WHITE],

                 [20, 580, 320, 20, WHITE], #bottom
                 [450, 580, 330, 20, WHITE], 

                 [190, 50, 20, 500, BLUE],
                 [290, 50, 20, 500, PURPLE],

                 [20, 0, 760, 20, WHITE], #Any walls underneath the white walls are extras
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

# FULL LEFT ROOM
class RoomFullLeft(Room): 
    """This creates all the walls in room 4"""
    def __init__(self, num):
        super().__init__()
        self.num = num
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, WHITE], #top
                 [450, 0, 330, 20, WHITE],

                 [0, 0, 20, 600, WHITE], #left

                 [780, 0, 20, 250, WHITE], #right
                 [780, 350, 20, 250, WHITE],

                 [20, 580, 320, 20, WHITE], #bottom
                 [450, 580, 330, 20, WHITE], 

                 [190, 50, 20, 500, BLUE],
                 [290, 50, 20, 500, BLUE],
                 [390, 50, 20, 500, BLUE],
                 [490, 50, 20, 500, BLUE],
                 [590, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
 
# FULL RIGHT ROOM
class RoomFullRight(Room):
    """This creates all the walls in room"""  
    def __init__(self, num):
        super().__init__()
        self.num = num
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, WHITE], #top
                 [450, 0, 330, 20, WHITE],

                 [0, 0, 20, 250, WHITE], #left
                 [0, 350, 20, 250, WHITE],

                 [780, 0, 20, 600, WHITE], #right

                 [20, 580, 320, 20, WHITE], #bottom
                 [450, 580, 330, 20, WHITE], 
                
                 [190, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
 
# FULL BOTTOM ROOM
class RoomFullBottom(Room):
    """This creates all the walls in room"""  
    def __init__(self, num):
        super().__init__()
        self.num = num
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, WHITE], #top
                 [450, 0, 330, 20, WHITE],

                 [0, 0, 20, 250, WHITE], #left
                 [0, 350, 20, 250, WHITE],

                 [780, 0, 20, 250, WHITE], #right
                 [780, 350, 20, 250, WHITE],

                 [20, 580, 600, 20, WHITE], #bottom
                
                 [190, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
 
 

# WE CAN CREATE A DIFFERENT DECORATION CLASS / METHOD HERE AND ADD TO THE ROOM
# DONT NEED TO BE TOO FANCY
# ROOMS CAN HAVE THE SAME DECORATION

# FULL LEFT RIGHT ROOM
class RoomFullLeftRight(Room): 
    """This creates all the walls in room 4"""
    def __init__(self, num):
        super().__init__()
        self.num = num
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, WHITE], #top
                 [450, 0, 330, 20, WHITE],

                 [0, 0, 20, 600, WHITE], #left

                 [780, 0, 20, 600, WHITE], #right

                 [20, 580, 320, 20, WHITE], #bottom
                 [450, 580, 330, 20, WHITE], 

                 [190, 50, 20, 500, BLUE],
                 [290, 50, 20, 500, BLUE],
                 [390, 50, 20, 500, BLUE],
                 [490, 50, 20, 500, BLUE],
                 [590, 50, 20, 500, BLUE]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
 
# FULL TOP BOTTOM ROOM
class RoomFullTopBottom(Room):
    """This creates all the walls in room 3"""
    def __init__(self, num):
        super().__init__()
        self.num = num
         #[x, y, width, height, color]
        walls = [[20, 0, 600, 20, WHITE], #top

                 [0, 0, 20, 250, WHITE], #left
                 [0, 350, 20, 250, WHITE],

                 [780, 0, 20, 250, WHITE], #right
                 [780, 350, 20, 250, WHITE],

                 [20, 580, 600, 20, WHITE], #bottom

                 [190, 50, 20, 500, BLUE],
                 [290, 50, 20, 500, PURPLE],

                 [20, 0, 760, 20, WHITE], #Any walls underneath the white walls are extras
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
