import pygame
from colors import *
from maze import Maze, Room
from wallsRooms import Room1, Room2, Room3, Room4


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Maze Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.running = True
        self.game_over = False

        self.maze = Maze()
        room1 = Room1()
        room2 = Room2()
        room3 = Room3()
        room4 = Room4()
        self.maze.add_room(room1)
        self.maze.add_room(room2)
        self.maze.add_room(room3)
        self.maze.add_room(room4)

        self.player = Player(room1)

        # Set the win room
        self.win_room = room4

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.move_down()
                elif event.key == pygame.K_LEFT:
                    self.player.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()
                elif event.key == pygame.K_q:
                    self.running = False

            # Add input handling for movement, picking up items, and quitting the game

    def update(self):
        if self.player.current_room == self.win_room:
            # Player has won the game
            self.game_over = True

        self.player.move(self.player.current_room.wallsList)
        star_hit_list = pygame.sprite.spritecollide(self.player, self.player.current_room.enemy_sprites, True)
        for star in star_hit_list:
            self.player.points += 1

    def draw(self):
        self.screen.fill(BLACK)

        if self.game_over:
            # End game screen
            end_text = f"Congratulations! You completed the game with a score of {self.player.points}."
            end_surface = pygame.font.Font(None, 36).render(end_text, True, WHITE)
            self.screen.blit(end_surface, (100, 250))
        else:
            # Draw the room, items, and player character
            # Draw the text box with the room description and available exits
            text_box = pygame.Surface((800, 100))
            text_box.fill(WHITE)
            self.screen.blit(text_box, (0, 500))

            # Draw the player's score and elapsed time
            score_text = f"Score: {self.player.score}"
            score_surface = pygame.font.Font(None, 36).render(score_text, True, BLACK)
            self.screen.blit(score_surface, (10, 510))

            elapsed_time = (pygame.time.get_ticks() // 1000)
            timer_text = f"Time: {elapsed_time} s"
            timer_surface = pygame.font.Font(None, 36).render(timer_text, True, BLACK)
            self.screen.blit(timer_surface, (650, 510))

            # Draw the room description and available exits
            text = self.font.render(self.player.current_room.description, True, BLACK)
            self.screen.blit(text, (10, 10))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

class Player(pygame.sprite.Sprite):
    def __init__(self, room):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = room.player_start_x
        self.rect.y = room.player_start_y
        self.change_x = 0
        self.change_y = 0
        self.points = 0
        self.current_room = room

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        star_hit_list = pygame.sprite.spritecollide(self, self.current_room.enemy_sprites, True)
        for star in star_hit_list:
            self.points += 1



if __name__ == "__main__":
    game = Game()
    game.run()
