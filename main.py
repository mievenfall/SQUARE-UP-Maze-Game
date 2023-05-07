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

def createRoomList():
    roomsList = [RoomFull(),
                 RoomFull(),
                 RoomFullTop(),
                 RoomFull(),
                 RoomFullLeft(),
                 RoomFullTop(),
                 RoomFullBottom(),
                 RoomFullTop(),
                 RoomFull(),
                 RoomFull(),
                 RoomFullBottom()]
    return roomsList

#Display text on screen
#First arg is the text, second arg is the color, third arg is the screen, fourth/fifth arg is the x/y coord respectively
def showText(text, color, screen, x, y):
    #Font Arial of size 30
    font = pygame.font.SysFont("Arial", 30)

    #Renders the text
    #Boolean represents antialias
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def main():
    """Uses the functions, classes, and other methods to setup and create the game"""
    # Initialize pygame
    pygame.init()
 
    # Create an 800x750 sized screen
    screen = pygame.display.set_mode([800, 750])
 
    # Set the title of the window
    pygame.display.set_caption('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
 
    # Create the player, along with creating the sprite
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
 
    #This list i(s used for toggling between rooms if the user goes through the doors
    roomsList = createRoomList()
 
    current_room_no = 1
    current_room = roomsList[current_room_no-1]
 
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

        #GO TO THE LEFT
        if player.rect.x < -15:
            # ROOM 1 -> ROOM 2
            if current_room_no == 1:
                current_room_no = 2
                current_room = roomsList[current_room_no-1]
                player.rect.x = 400
                player.rect.y = 0

            # ROOM 2 -> ROOM 2
            elif current_room_no == 2:
                current_room_no = 2
                current_room = roomsList[current_room_no-1]
                player.rect.x = 0
                player.rect.y = 300
            
            # ROOM 3 -> ROOM 3
            elif current_room_no == 3:
                current_room_no = 1
                current_room = roomsList[current_room_no-1]
                player.rect.x = 790

            # ROOM 4 -> ROOM 1
            elif current_room_no == 4:
                current_room_no = 1   
                current_room = roomsList[current_room_no-1]
                player.rect.x = 400
                player.rect.y = 600

            # ROOM 5 xx
            else:
                current_room_no = 3   
                current_room = roomsList[current_room_no-1]
 

        #GO TO THE RIGHT
        if player.rect.x > 801:
            # ROOM 1 -> ROOM 3
            if current_room_no == 1:
                current_room_no = 3
                current_room = roomsList[current_room_no-1]
                player.rect.x = 0

            # ROOM 2 -> DEAD END

            # ROOM 3 -> ROOM 4
            elif current_room_no == 3:
                current_room_no = 4
                current_room = roomsList[current_room_no-1]
                player.rect.x = 400
                player.rect.y = 0
            
            # ROOM 4 -> DEAD END

            # ROOM 5 -> ROOM 3
            else:
                current_room_no = 3
                current_room = roomsList[current_room_no-1]
                player.rect.x = 400
                player.rect.y = 600
 
        # --- Drawing ---

        #Black background color
        screen.fill(BLACK)
 
        #Draw sprites onto the screen
        movingsprites.draw(screen)
        current_room.wallsList.draw(screen)
        
        #Display text onto the screen at (100, 500) using the showText function
        #This would primarily be used to label each room to avoid confusion for the user
        #And could let the user know they unlocked something after completing a puzzle if it were implemented
        showText("Testing", WHITE, screen, 100, 500)
        
        #Update the display onto the screen
        pygame.display.flip()
 
        #Max 60 fps
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()
