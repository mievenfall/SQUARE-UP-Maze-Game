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

def createRoomsList():
    roomsList = [RoomStart(0),
                 RoomFull(1),
                 RoomFull(2),
                 RoomFullTop(3),
                 RoomFull(4),
                 RoomFullLeft(5),
                 RoomFullTop(6),
                 RoomFullTopBottom(7),
                 RoomFullTop(8),
                 RoomFullLeftRight(9),
                 RoomFull(10),
                 RoomFullBottom(11)]
    return roomsList

def topPos(player):
    return 300, 0

def botPos(player):
    return 320, 580

def leftPos(player):
    return 0, 300

def rightPos(player):
    return  790, 300

def goLeft(num, roomsList, player):
    # ROOM 1 -> ROOM 2
    if num == 1: 
        num = 2
        player.rect.x, player.rect.y = topPos(player)

    # ROOM 2 -> ROOM 2
    if num == 2:
        num = 2
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 3 -> ROOM 1
    if num == 3:
        num = 1
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 4 -> ROOM 1
    if num == 4:
        num = 1   
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 5 XX

    # ROOM 6 -> ROOM 7
    if num == 6:
        num = 7   
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 7 -> ROOM 8
    if num == 7:
        num = 8   
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 8 -> ROOM 7
    if num == 8:
        num = 7   
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 9 xxx

    # ROOM 10 -> ROOM 6
    if num == 10:
        num = 6
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 11 -> ROOM 10
    if num == 11:
        num = 10
        player.rect.x, player.rect.y = topPos(player)


    current_room = roomsList[num]

    return current_room, player.rect.x, player.rect.y, num

def goRight(num, roomsList, player):
    # ROOM 1 -> ROOM 3
    if num == 1: 
        num = 3
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 2 -> DEADEND
    elif num == 2:
        pass

    # ROOM 3 -> ROOM 4
    elif num == 3:
        num = 4
        player.rect.x, player.rect.y = topPos(player)

    # ROOM 4 -> DEAD END
    elif num == 4:
        pass

    # ROOM 5 -> ROOM 3
    elif num == 5:
        num = 3
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 6 -> ROOM 5
    elif num == 6:
        num = 5   
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 7 -> ROOM 6
    elif num == 7:
        num = 6  
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 8 -> ROOM 10
    elif num == 8:
        num = 10 
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 9 xxx

    # ROOM 10 -> ROOM 8
    elif num == 10:
        num = 8
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 11 -> GOAL
    else:
        pass

    current_room = roomsList[num]

    return current_room, player.rect.x, player.rect.y, num
    
def goDown(num, roomsList, player):
    # ROOM 0 -> ROOM 1
    if num == 0:
        num = 1
        player.rect.x, player.rect.y = topPos(player)

    # ROOM 1 -> ROOM 4
    if num == 1: 
        num = 4
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 2 -> ROOM 2
    if num == 2:
        num = 2
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 3 -> ROOM 5
    if num == 3:
        num = 5
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 4 -> DEAD END
    if num == 4:
        pass

    # ROOM 5 -> ROOM 6
    if num == 5:
        num = 6
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 6 -> ROOM 10
    if num == 6:
        num = 10   
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 7 xxx

    # ROOM 8 -> ROOM 9
    if num == 8:
        num = 9
        player.rect.x, player.rect.y = topPos(player)

    # ROOM 9 -> DEAD END
    if num == 9:
        pass

    # ROOM 10 -> ROOM 10
    if num == 10:
        num = 10
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 11 xxx


    current_room = roomsList[num]

    return current_room, player.rect.x, player.rect.y, num

def goUp(num, roomsList, player):

    # ROOM 1 -> ROOM 0
    if num == 1: 
        num = 0
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 2 -> ROOM 1
    if num == 2:
        num = 1
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 3 xxx

    # ROOM 4 -> ROOM 3
    if num == 4:
        num = 3
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 5 -> DEAD END
    if num == 5:
        pass

    # ROOM 6 xxx

    # ROOM 7 xxx

    # ROOM 8 xxx

    # ROOM 9 -> ROOM 8
    if num == 9:
        num = 8
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 10 -> ROOM 11
    if num == 10:
        num = 11
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 11 -> ROOM 11
    if num == 11:
        num = 11
        player.rect.x, player.rect.y = topPos(player)

    current_room = roomsList[num]

    return current_room, player.rect.x, player.rect.y, num


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
 
    #This list i(s used for toggling between rooms if the user goes through the doors
    roomsList = createRoomsList()
 
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

        #GO TO THE LEFT
        if player.rect.x < -15:
            current_room, player.rect.x, player.rect.y, current_room_no = goLeft(current_room_no, roomsList, player)
            print(current_room.num)

        #GO TO THE RIGHT
        if player.rect.x > 801:
            current_room, player.rect.x, player.rect.y, current_room_no = goRight(current_room_no, roomsList, player)
            print(current_room.num)
        #GO DOWN
        if player.rect.y > 600:
            current_room, player.rect.x, player.rect.y, current_room_no = goDown(current_room_no, roomsList, player)
            print(current_room.num)
        #GO UP
        if player.rect.y < 15:
            current_room, player.rect.x, player.rect.y, current_room_no = goUp(current_room_no, roomsList, player)
            print(current_room.num)
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