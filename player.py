"""
This file deals with the Player class.
This is where you create the character via height and length, keypress, collision, etc.

"""



import pygame
from colors import *
from wallsRooms import *

pygame.init() 

class Player(pygame.sprite.Sprite):
    """ This class represents the user, in the form of a white box (can be changed if necessary) """
 
 
    def __init__(self, x, y):
        # Call the Sprite's constructor since pygame is a collection of modules to use its set of functions
        super().__init__()
        # Set the height and width of the player, along with set color
        self.image = pygame.image.load('jennienpc.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.changeX = 0
        self.changeY = 0
 
    #Changes speed of the player
    def changespeed(self, x, y):
        self.changeX += x
        self.changeY += y
 
    #Find a new position for the player
    def move(self, walls): 
        # Move left/right
        self.rect.x += self.changeX
 
        #This deals with sprite collisions against the walls
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.changeX > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.changeY
 
        #This also deals with sprite collisions
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.changeY > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
    def update(self):
        """ Move the player. """
        self.rect.move_ip(self.changeX, self.changeY)

    def changePlayerImage(self, image_file):
        """Changes the player image"""
        self.image = pygame.image.load(image_file).convert_alpha()

class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('coin.png') 
        self.image = pygame.transform.scale(self.image, (20, 20)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


