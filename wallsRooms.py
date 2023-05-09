"""
This files deals with the layout of the maze, along with creating each individual room.

"""
import random
import pygame
from pygame.sprite import Group
from colors import *
from player import Player
 
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

        #Instatiate a Player object with given x and y values:
        self.player = Player(x, y)
 
class Star(pygame.sprite.Sprite):
    SIZE = 10

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([self.SIZE, self.SIZE])
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
#Inherits the object class
class Room(object):
    """Parent class for all rooms"""
 
    #Each room has a list of walls, enemy sprites, star sprites, and player sprite.
    wallsList = None
    enemy_sprites = None
    star_sprites = None
    player_sprite = None
 
    def __init__(self):
        self.wallsList = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.star_sprites = pygame.sprite.Group()
        self.width = 0
        self.height = 0
        self.player_start_x = 0
        self.player_start_y = 0

    def add_wall(self, wall):
        self.wallsList.add(wall)

    def add_enemy(self, enemy):
        self.enemy_sprites.add(enemy)

    def add_star(self, star):
        self.star_sprites.add(star)
 

# 4 WALLS ROOM
class RoomFull(Room):
    """This creates all the walls in room"""  
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.width = 800
        self.height = 600
        self.player_start_x = 50
        self.player_start_y = 50
        self.wall_width = 10
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, PINK], #top
                 [450, 0, 330, 20, PINK],

                 [0, 0, 20, 250, PINK], #left
                 [0, 350, 20, 250, PINK],

                 [780, 0, 20, 250, PINK], #right
                 [780, 350, 20, 250, PINK],

                 [20, 580, 320, 20, PINK], #bottom
                 [450, 580, 330, 20, PINK]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
         
        # Define star position
        x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
        y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
        self.star_sprites.add(Star(x, y)) 
        
        # Add stars
        for i in range(5):
            x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
            y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
            star = Star(x, y)
            self.star_sprites.add(star)                   

# START ROOM
class RoomStart(Room):
    """This creates all the walls in room 3"""
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.width = 800
        self.height = 600
        self.wall_width = 10
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
         #[x, y, width, height, color]
        walls = [[20, 0, 800, 20, PINK], #top

                 [0, 0, 20, 600, PINK], #left

                 [780, 0, 20, 600, PINK], #right

                 [20, 580, 320, 20, PINK], #bottom
                 [450, 580, 330, 20, PINK]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

        # Define star position
        x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
        y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
        self.star_sprites.add(Star(x, y))      

        # Add stars
        for i in range(6):
            x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
            y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
            star = Star(x, y)
            self.star_sprites.add(star)


# GOAL ROOM
class RoomGoal(Room):
    """This creates all the walls in room 3"""
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
         #[x, y, width, height, color]
        walls = [[20, 0, 800, 20, PINK], #top

                 [0, 0, 20, 250, PINK], #left
                 [0, 350, 20, 250, PINK],

                 [780, 0, 20, 600, PINK], #right

                 [20, 580, 800, 20, PINK] #bottom
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

# FULL TOP ROOM
class RoomFullTop(Room):
    """This creates all the walls in room 3"""
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.width = 800
        self.height = 600
        self.player_start_x = 750
        self.player_start_y = 550
        self.wall_width = 10
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)

         #[x, y, width, height, color]
        walls = [[20, 0, 800, 20, PINK], #top

                 [0, 0, 20, 250, PINK], #left
                 [0, 350, 20, 250, PINK],

                 [780, 0, 20, 250, PINK], #right
                 [780, 350, 20, 250, PINK],

                 [20, 580, 320, 20, PINK], #bottom
                 [450, 580, 330, 20, PINK]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

        # Define star position
        x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
        y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
        self.star_sprites.add(Star(x, y))      

        # Add stars
        for i in range(6):
            x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
            y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
            star = Star(x, y)
            self.star_sprites.add(star)

# FULL LEFT ROOM
class RoomFullLeft(Room): 
    """This creates all the walls in room 4"""
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.width = 800
        self.height = 600
        self.player_start_x = 50
        self.player_start_y = 550
        self.wall_width = 10
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, PINK], #top
                 [450, 0, 330, 20, PINK],

                 [0, 0, 20, 600, PINK], #left

                 [780, 0, 20, 250, PINK], #right
                 [780, 350, 20, 250, PINK],

                 [20, 580, 320, 20, PINK], #bottom
                 [450, 580, 330, 20, PINK]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

        # Define star position
        x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
        y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
        self.star_sprites.add(Star(x, y))

        # Add stars
        for i in range(5):
            x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
            y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
            star = Star(x, y)
            self.star_sprites.add(star)

# FULL RIGHT ROOM
class RoomFullRight(Room):
    """This creates all the walls in room"""  
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.width = 800
        self.height = 600
        self.player_start_x = 50
        self.player_start_y = 550
        self.wall_width = 10
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, PINK], #top
                 [450, 0, 330, 20, PINK],

                 [0, 0, 20, 250, PINK], #left
                 [0, 350, 20, 250, PINK],

                 [780, 0, 20, 600, PINK], #right

                 [20, 580, 320, 20, PINK], #bottom
                 [450, 580, 330, 20, PINK]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

        # Define star position
        x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
        y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
        self.star_sprites.add(Star(x, y))

        # Add stars
        for i in range(4):
            x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
            y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
            star = Star(x, y)
            self.star_sprites.add(star)

# FULL BOTTOM ROOM
class RoomFullBottom(Room):
    """This creates all the walls in room"""  
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, PINK], #top
                 [450, 0, 330, 20, PINK],

                 [0, 0, 20, 250, PINK], #left
                 [0, 350, 20, 250, PINK],

                 [780, 0, 20, 250, PINK], #right
                 [780, 350, 20, 250, PINK],

                 [20, 580, 800, 20, PINK] #bottom
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)
 
# FULL LEFT RIGHT ROOM
class RoomFullLeftRight(Room): 
    """This creates all the walls in room 4"""
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.width = 800
        self.height = 600
        self.player_start_x = 50
        self.player_start_y = 550
        self.wall_width = 10
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[20, 0, 320, 20, PINK], #top
                 [450, 0, 330, 20, PINK],

                 [0, 0, 20, 600, PINK], #left

                 [780, 0, 20, 600, PINK], #right

                 [20, 580, 320, 20, PINK], #bottom
                 [450, 580, 330, 20, PINK]
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

        # Define star position
        x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
        y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
        self.star_sprites.add(Star(x, y))

        # Add stars
        for i in range(4):
            x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
            y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
            star = Star(x, y)
            self.star_sprites.add(star) 

# FULL TOP BOTTOM ROOM
class RoomFullTopBottom(Room):
    """This creates all the walls in room 3"""
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.width = 800
        self.height = 600
        self.player_start_x = 50
        self.player_start_y = 550
        self.wall_width = 10
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
         #[x, y, width, height, color]
        walls = [[20, 0, 800, 20, PINK], #top

                 [0, 0, 20, 250, PINK], #left
                 [0, 350, 20, 250, PINK],

                 [780, 0, 20, 250, PINK], #right
                 [780, 350, 20, 250, PINK],

                 [20, 580, 800, 20, PINK] #bottom
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

        # Define star position
        x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
        y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
        self.star_sprites.add(Star(x, y))

        # Add stars
        for i in range(4):
            x = random.randint(self.wall_width, self.width - self.wall_width - Star.SIZE)
            y = random.randint(self.wall_width, self.height - self.wall_width - Star.SIZE)
            star = Star(x, y)
            self.star_sprites.add(star)

# EMPTY TOP ROOM
class RoomEmptyTop(Room):
    """This creates all the walls in room"""  
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
        # Make the walls. (x-axis, y-axis, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 340, 20, PINK], #top
                 [450, 0, 350, 20, PINK],

                 [320, 0, 20, 450, PINK], #left

                 [450, 0, 20, 450, PINK], #right

                 [320, 450, 150, 20, PINK] #bottom
                ]
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls: #[x, y, width, height]
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

# EMPTY BOTTOM ROOM
class RoomEmptyBottom(Room):
    """This creates all the walls in room 3"""
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
         #[x, y, width, height, color]
        walls = [[320, 130, 150, 20, PINK], #top

                 [320, 130, 20, 450, PINK], #left

                 [450, 130, 20, 450, PINK], #right

                 [0, 580, 340, 20, PINK], #bottom
                 [450, 580, 350, 20, PINK]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

# EMPTY LEFT ROOM
class RoomEmptyLeft(Room):
    """This creates all the walls in room 3"""
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
         #[x, y, width, height, color]
        walls = [[20, 230, 550, 20, PINK], #top

                 [0, 0, 20, 250, PINK], #left
                 [0, 350, 20, 250, PINK],

                 [550, 250, 20, 100, PINK], #right

                 [20, 350, 550, 20, PINK] #bottom
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

# EMPTY RIGHT ROOM
class RoomEmptyRight(Room):
    """This creates all the walls in room 3"""
    def __init__(self, num, player):
        super().__init__()
        self.num = num
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)
         #[x, y, width, height, color]
        walls = [[250, 230, 550, 20, PINK], #top

                 [250, 250, 20, 100, PINK], #left

                 [780, 0, 20, 250, PINK], #right
                 [780, 350, 20, 250, PINK],

                 [250, 350, 550, 20, PINK] #bottom
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wallsList.add(wall)

        # Add player to the list
        self.player_sprite = pygame.sprite.Group()
        self.player_sprite.add(player)


class Decor(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y):
        super().__init__()
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# WE CAN CREATE A DIFFERENT DECORATION CLASS / METHOD HERE AND ADD TO THE ROOM
# DONT NEED TO BE TOO FANCY
# ROOMS CAN HAVE THE SAME DECORATION

