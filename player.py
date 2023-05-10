"""
This file deals with the Player class.
This is where you create the character via height and length, keypress, collision, etc.

"""



import pygame
from colors import *
from wallsRooms import *
import sys

pygame.init() 

class Player(pygame.sprite.Sprite):
    """ This class represents the user, in the form of a white box (can be changed if necessary) """
 
 
    def __init__(self, x, y):
        # Call the Sprite's constructor since pygame is a collection of modules to use its set of functions
        super().__init__()
        # Set the height and width of the player, along with set color
        self.image = pygame.image.load('pics/jennienpc.png')
        self.image = pygame.transform.scale(self.image, (55, 55))
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
    SIZE = 10
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('pics/coin.png') 
        self.image = pygame.transform.scale(self.image, (20, 20)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigStar(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('pics/coin.png') 
        self.image = pygame.transform.scale(self.image, (150, 150)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MenuScreen:
    def __init__(self, screen, width, height, start_img, exit_img, button_width, button_height):
        self.screen = screen
        self.width = width
        self.height = height
        # Assuming button_width and button_height are the new dimensions for the start button
        self.start_button = Button(start_img, self.width/2 - button_width/2, self.height/2 - button_height, 200, 150)
        #self.exit_button = Button(exit_img, width/2 - button_width/2, height/2 + button_height/2 + 50, button_width, button_height)
        self.active = True
        self.font = pygame.font.Font(None, 36)  

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.start_button.rect.collidepoint(pos):
                self.active = False
            # elif self.exit_button.rect.collidepoint(pos):
            #     pygame.quit()
            #     sys.exit()

    def draw(self):
        self.screen.fill(BLACK)

        # Draw the buttons
        self.start_button.draw(self.screen)
        #self.exit_button.draw(self.screen)

        # Render the text
        text = self.font.render("Welcome to SQUARED UP: Maze Game", True, (ROSE))

        # Determine the position for the text. It should be centered horizontally,
        # and located above the start button (minus additional space)
        text_x = self.width / 2 - text.get_width() / 2
        text_y = self.start_button.rect.y - text.get_height() - 20  # 20 is the additional space

        # Draw the text onto the screen
        self.screen.blit(text, (text_x, text_y))

        pygame.display.flip()


class EndScreen:
    def __init__(self, screen, width, height, restart_img, quit_img, button_width, button_height):
        self.screen = screen
        self.width = width
        self.height = height
        # Assuming button_width and button_height are the new dimensions for the start button
        self.start_button = Button(restart_img, self.width/2 - button_width/2, self.height/2 - button_height, 200, 150)
        self.quit_button = Button(quit_img, width/2 - button_width/2, height/2 + button_height/2 + 50, button_width, button_height)
        self.active = True
        self.font = pygame.font.Font(None, 36)  

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.start_button.rect.collidepoint(pos):
                self.active = False
            elif self.quit_button.rect.collidepoint(pos):
                pygame.quit()
                sys.quit()

    def draw(self):
        self.screen.fill(BLACK)

        # Draw the buttons
        self.start_button.draw(self.screen)
        self.quit_button.draw(self.screen)

        # Render the text
        text = self.font.render("Welcome to SQUARED UP: Maze Game", True, (ROSE))

        # Determine the position for the text. It should be centered horizontally,
        # and located above the start button (minus additional space)
        text_x = self.width / 2 - text.get_width() / 2
        text_y = self.start_button.rect.y - text.get_height() - 20  # 20 is the additional space

        # Draw the text onto the screen
        self.screen.blit(text, (text_x, text_y))

        pygame.display.flip()

class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width=0, height=0):
        super().__init__()
        self.image = pygame.image.load(image)
        if width != 0 and height != 0:
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


