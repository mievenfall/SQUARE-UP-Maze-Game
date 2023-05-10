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
import sys

# Create the player, along with creating the sprite
# Load the player image
player_image = pygame.image.load("jennienpc.png")

# Create the player
player = Player(70, 70)

movingsprites = pygame.sprite.Group()
movingsprites.add(player)

def createRoomsList():

    roomsList = [RoomStart(0, player),
                 RoomFull(1, player),
                 RoomFull(2, player),
                 RoomFullTop(3, player),
                 RoomFull(4, player),
                 RoomFullLeft(5, player),
                 RoomFullTop(6, player),
                 RoomFullTopBottom(7, player),
                 RoomFullTop(8, player),
                 RoomFullLeftRight(9, player),
                 RoomFull(10, player),
                 RoomFullBottom(11, player),
                 RoomEmptyTop(12, player),
                 RoomEmptyLeft(13, player),
                 RoomEmptyLeft(14, player),
                 RoomEmptyRight(15, player),
                 RoomEmptyBottom(16, player),
                 RoomGoal(17, player)]
    return roomsList

   

def topPos(player):
    return 390, 50

def botPos(player):
    return 390, 550

def leftPos(player):
    return 50, 295

def rightPos(player):
    return  740, 295

def goLeft(num, roomsList, player):
    # ROOM 1 -> ROOM 2
    if num == 1: 
        num = 2
        player.rect.x, player.rect.y = topPos(player)

    # ROOM 2 -> ROOM 2
    elif num == 2:
        num = 2
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 3 -> ROOM 1
    elif num == 3:
        num = 1
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 4 -> ROOM 1
    elif num == 4:
        num = 1   
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 5 XX

    # ROOM 6 -> ROOM 7
    elif num == 6:
        num = 7   
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 7 -> ROOM 8
    elif num == 7:
        num = 8   
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 8 -> ROOM 7
    elif num == 8:
        num = 7   
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 9 xxx

    # ROOM 10 -> ROOM 6
    elif num == 10:
        num = 6
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 11 -> ROOM 10
    elif num == 11:
        num = 10
        player.rect.x, player.rect.y = topPos(player)

    # DEAD END -> ROOM 4
    elif num == 13:
        num = 4
        player.rect.x, player.rect.y = rightPos(player)

    # DEAD END -> ROOM 4
    elif num == 14:
        num = 4
        player.rect.x, player.rect.y = botPos(player)
    
    # GOAL -> ROOM 11
    elif num == 17:
        num = 11
        player.rect.x, player.rect.y = rightPos(player)


    else:
        pass


    current_room = roomsList[num]

    return current_room, player.rect.x, player.rect.y, num

def goRight(num, roomsList, player):
    # ROOM 1 -> ROOM 3
    if num == 1: 
        num = 3
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 2 -> DEADEND
    elif num == 2:
        num = 12
        player.rect.x, player.rect.y = topPos(player)

    # ROOM 3 -> ROOM 4
    elif num == 3:
        num = 4
        player.rect.x, player.rect.y = topPos(player)

    # ROOM 4 -> DEAD END
    elif num == 4:
        num = 13
        player.rect.x, player.rect.y = leftPos(player)

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
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 9 xxx

    # ROOM 10 -> ROOM 8
    elif num == 10:
        num = 8
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 11 -> GOAL
    elif num == 11:
        num = 17
        player.rect.x, player.rect.y = leftPos(player)

    # DEAD END -> ROOM 5
    elif num == 15:
        num = 5
        player.rect.x, player.rect.y = topPos(player)
    
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
    elif num == 1: 
        num = 4
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 2 -> ROOM 2
    elif num == 2:
        num = 2
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 3 -> ROOM 5
    elif num == 3:
        num = 5
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 4 -> DEAD END
    elif num == 4:
        num = 14
        player.rect.x, player.rect.y = leftPos(player)


    # ROOM 5 -> ROOM 6
    elif num == 5:
        num = 6
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 6 -> ROOM 10
    elif num == 6:
        num = 10   
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 7 xxx

    # ROOM 8 -> ROOM 9
    elif num == 8:
        num = 9
        player.rect.x, player.rect.y = topPos(player)

    # ROOM 9 -> DEAD END
    elif num == 9:
        num = 16
        player.rect.x, player.rect.y = botPos(player)


    # ROOM 10 -> ROOM 10
    elif num == 10:
        num = 10
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 11 xxx
    
    # DEAD END -> ROOM 5
    elif num == 15:
        num = 5
        player.rect.x, player.rect.y = topPos(player)


    # DEAD END -> ROOM 9
    elif num == 16:
        num = 9
        player.rect.x, player.rect.y = botPos(player)

    else:
        pass


    current_room = roomsList[num]

    return current_room, player.rect.x, player.rect.y, num

def goUp(num, roomsList, player):

    # ROOM 1 -> ROOM 0
    if num == 1: 
        num = 0
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 2 -> ROOM 1
    elif num == 2:
        num = 1
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 3 xxx

    # ROOM 4 -> ROOM 3
    elif num == 4:
        num = 3
        player.rect.x, player.rect.y = rightPos(player)

    # ROOM 5 -> DEAD END
    elif num == 5:
        num = 15
        player.rect.x, player.rect.y = rightPos(player)


    # ROOM 6 xxx

    # ROOM 7 xxx

    # ROOM 8 xxx

    # ROOM 9 -> ROOM 8
    elif num == 9:
        num = 8
        player.rect.x, player.rect.y = botPos(player)

    # ROOM 10 -> ROOM 11
    elif num == 10:
        num = 11
        player.rect.x, player.rect.y = leftPos(player)

    # ROOM 11 -> ROOM 11
    elif num == 11:
        num = 11
        player.rect.x, player.rect.y = topPos(player)

    # DEAD END -> ROOM 2
    elif num == 12:
        num = 2
        player.rect.x, player.rect.y = rightPos(player)


    else:
        pass

    current_room = roomsList[num]

    return current_room, player.rect.x, player.rect.y, num

def createStarsList(roomsList, player):
    """ This function creates a list of all the stars in the game """
    starsList = pygame.sprite.Group()

    for room in roomsList:
        if room in player.accessible_rooms:
            # Calculate the maximum x and y values for the room
            max_x = room.x + room.width - 50
            max_y = room.y + room.height - 50

            # Generate a random number of stars to place in the room (between 1 and 3)
            num_stars = random.randint(1, 3)

            for i in range(num_stars):
                # Generate a random position for the star within the room
                star_x = random.randint(room.x + 10, max_x)
                star_y = random.randint(room.y + 10, max_y)

                # Create the star and add it to the list
                star = Star(star_x, star_y)
                starsList.add(star)

    return starsList

def main():
    """Uses the functions, classes, and other methods to setup and create the game"""
    # Initialize pygame
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('SQUARED UP: MAZE GAME')
 
    start_button_img = "start.png"
    exit_button_img = "exit.png"
    
    menu_screen = MenuScreen(screen, 800, 600, start_button_img, exit_button_img, 200, 75)

    # Load sound files
    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play(-1)

    # Set the initial volume and mute state
    volume = 1.0
    is_muted = False

    # Load speaker images
    speaker_muted_img = pygame.image.load('mute.png')
    speaker_muted_img = pygame.transform.scale(speaker_muted_img, (30, 30))
    speaker_rect = speaker_muted_img.get_rect()
    speaker_rect.topright = (screen.get_width() - 30, 30)
 
    #This list is used for toggling between rooms if the user goes through the doors
    roomsList = createRoomsList()
    total_stars = sum([len(room.star_sprites) for room in roomsList])

    current_room_no = 0
    current_room = roomsList[current_room_no]

    #Keep track of how many stars the player has collected
    stars_collected = 0
    points = 0
    total_points = 0

    
    #Set up font for displaying points
    font = pygame.font.Font(None, 36) 

    clock = pygame.time.Clock()
 
    finishPlay = False

    #Initialize flag for goal room reached
    congratulations = False

 
    while not finishPlay and points < total_stars:
 
        # --- Event Processing ---
 
        for event in pygame.event.get():
            #If user clicks exit button, quit the game
            if event.type == pygame.QUIT:
                finishPlay = True

            #Handle input events for menu screen
            if menu_screen.active:
                menu_screen.handle_input(event)

            else:

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

        #If on the menu screen, handle input and display the screen
        if menu_screen.active:
            menu_screen.draw()

        else:
        # --- Game Logic ---

        
            player.move(current_room.wallsList)

            #Check if player has collided with a star:
            star_collisions = pygame.sprite.spritecollide(player, current_room.star_sprites, True)
            points = len(star_collisions)
            total_points += points

     
            #If the player touches the end of either side of the screen, move them into the next/previous room

            #GO TO THE LEFT
            if player.rect.x < -15:
                current_room, player.rect.x, player.rect.y, current_room_no = goLeft(current_room_no, roomsList, player)
                print(current_room.num, current_room_no)
            #GO TO THE RIGHT
            if player.rect.x > 801:
                current_room, player.rect.x, player.rect.y, current_room_no = goRight(current_room_no, roomsList, player)
                print(current_room.num, current_room_no)
            #GO DOWN
            if player.rect.y > 600:
                current_room, player.rect.x, player.rect.y, current_room_no = goDown(current_room_no, roomsList, player)
                print(current_room.num, current_room_no)
            #GO UP
            if player.rect.y < 15:
                current_room, player.rect.x, player.rect.y, current_room_no = goUp(current_room_no, roomsList, player)
                print(current_room.num, current_room_no)
            
            # --- Drawing ---

        if is_muted:
            screen.blit(speaker_muted_img, speaker_rect)

        # Display congratulations message
        if congratulations:
            #new screen
            screen.fill(BLACK)
            #screen.blit(player.image, player.rect)

            #Draw sprites onto the screen
            movingsprites.draw(screen)
            current_room.wallsList.draw(screen)
            current_room.star_sprites.draw(screen)
            current_room.player_sprite.draw(screen)

            # Check for collision with goal room
            if current_room == roomsList[17]:
                # Draw stars onto the screen
                current_room.star_sprites.draw(screen)
                
                # Check for collision with stars
                star_collide = pygame.sprite.spritecollide(player, current_room.star_sprites, True)

                #Display text to tell user the big prize at the WIN ROOM:
                font = pygame.font.Font(None, 24)
                text = font.render("Double your score with the big prize", True, ROSE)
                screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 35))

                if star_collide:
                    stars_collected += 1
                    total_points += len(star_collide)

                if stars_collected == len(current_room.star_sprites):
                    congratulations = True
                    finishPlay = True

            # Display congratulations message
            if congratulations:
                #new screen
                screen.fill(BLACK)
                font = pygame.font.Font(None, 40)
                text1 = font.render("Congratulations!", True, ROSE)
                text1_rect = text1.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
                screen.blit(text1, text1_rect)

                font = pygame.font.Font(None, 30)
                text2 = font.render("You have reached the goal room!", True, ROSE)
                text2_rect = text2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
                screen.blit(text2, text2_rect)

                # Display score in the middle of the screen
                font = pygame.font.Font(None, 34)
                text3 = font.render(f"New Score: {total_points*2}", True, ROSE)   #Times 2 score
                text3_rect = text3.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
                screen.blit(text3, text3_rect)

                #Update walls color and draw them on the screen
                current_room.wallsList.draw(screen)
                pygame.display.flip()
                pygame.time.wait(20000)
                

            #Display score at left corner
            if not congratulations:
                font = pygame.font.Font(None, 36)
                text = font.render(f"Points: {total_points}", True, PINK)
                screen.blit(text, (30, 30))

            pygame.display.flip()
            clock.tick(60)


    pygame.quit()
 
if __name__ == "__main__":
    main()