"""
This is the main file, where it imports all files used to create and run this game.
The rooms are created, the controls are set, etc.

For documentation of pygame, visit the following sites:
https://www.pygame.org/docs/
https://devdocs.io/pygame/
"""

import pygame
from colors import *
from wallsRooms import *
from player import *

def main():
    """Uses the functions, classes, and other methods to setup and create the game"""
    # Initialize pygame
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
 
    # Create the player, along with creating the sprite
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
 
    #This list is used for toggling between rooms if the user goes through the doors
    roomsList = []
 
    room = Room1()
    roomsList.append(room)
 
    room = Room2()
    roomsList.append(room)
 
    room = Room3()
    roomsList.append(room)
 
    current_room_no = 0
    current_room = roomsList[current_room_no]
 
    clock = pygame.time.Clock()
 
    finishPlay = False
 
    while not finishPlay:
 
        # --- Event Processing ---
 
        for event in pygame.event.get():
            #If user clicks exit button, quit the game
            if event.type == pygame.QUIT:
                finishPlay = True
 
            #Player contrls using WASD keys
            #Can also change the WASD keys to arrow keeps with K_LEFT, K_RIGHT, etc. if needed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_d:
                    player.changespeed(5, 0)
                if event.key == pygame.K_w:
                    player.changespeed(0, -5)
                if event.key == pygame.K_s:
                    player.changespeed(0, 5)
 
            #Notice the change in signs in the change speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.changespeed(5, 0)
                if event.key == pygame.K_d:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_w:
                    player.changespeed(0, 5)
                if event.key == pygame.K_s:
                    player.changespeed(0, -5)
 
        # --- Game Logic ---
 
        player.move(current_room.wallsList)
 
        #If the player touches the end of either side of the screen, move them into the next/previous room
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = roomsList[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = roomsList[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = roomsList[current_room_no]
                player.rect.x = 790
 
        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = roomsList[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = roomsList[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = roomsList[current_room_no]
                player.rect.x = 0
 
        # --- Drawing ---

        #Black background color
        screen.fill(BLACK)
 
        #Draw sprites onto the screen
        movingsprites.draw(screen)
        current_room.wallsList.draw(screen)
 
        #Update the display onto the screen
        pygame.display.flip()
 
        #Max 60 fps
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()