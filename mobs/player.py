from game_settings import *
from general_mob import Entity
from weapons import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_position
        self.angle = player_angle

    # def inventory(self):
        # weapon =
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:  # north
            self.x += Player.movement_speed * cos_a
            self.y += Player.movement_speed * sin_a
            # self.y = self.y - Player.movement_speed
        if keys[pygame.K_s]:  # south
            self.x += - Player.movement_speed * cos_a
            self.y += - Player.movement_speed * sin_a
            # self.y = self.y + Player.movement_speed
        if keys[pygame.K_a]:  # east
            self.x += Player.movement_speed * sin_a
            self.y += - Player.movement_speed * cos_a
            # self.x = self.x - Player.movement_speed
        if keys[pygame.K_d]:  # west
            self.x += - Player.movement_speed * sin_a
            self.y += Player.movement_speed * cos_a
            # self.x = self.x + Player.movement_speed
        if keys[pygame.K_LEFT]:  # Left_rotation
            self.angle = self.angle - 0.2
        if keys[pygame.K_RIGHT]:  # right_rotation
            self.angle = self.angle + 0.2

    @property
    def position(self):
        return (self.x, self.y)


Player = Entity(Renion, 25, 1, 0, 1, 2, 6)
