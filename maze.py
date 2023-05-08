# maze.py
import pygame
import colors

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)

class Maze:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def get_room(self, name):
        return self.rooms.get(name)
    


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.previous_room = None
        self.items = []
        self.score = 0

    def move(self, direction):
        new_room = self.current_room.get_exit(direction)
        if new_room:
            self.previous_room = self.current_room
            self.current_room = new_room
            return True
        else:
            return False

    def pickup_item(self, item):
        self.items.append(item)

    def has_item(self, item):
        return item in self.items
    
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(colors.GOLD) # Add GOLD color in colors.py
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

