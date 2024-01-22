import os
import pygame
from support import import_sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._move_speed = 2

        self._animations = {'idle': [], 'run': [], 'jump': [], 'roll': []}
        self.importCharacterAsset()
        self._frame_index = 0
        self._animation_speed = 0.15
        self._image = self._animations['idle'][0]
        self._orientation_right = True
        self._status = 'idle'

        self._rect = pygame.Rect(x, y, int(os.environ.get('PLAYER_WIDTH')), int(os.environ.get('PLAYER_HEIGHT')))

    def animate(self):
        animation = self._animations[self._status]
        self._frame_index += self._animation_speed
        if self._frame_index >= len(animation):
            self._frame_index = 0

        self._image = animation[int(self._frame_index)]

        image = animation[int(self._frame_index)]
        if self._orientation_right:
            self._image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self._image = flipped_image

    def importCharacterAsset(self):
        character_path = "sprites/player/"
        for key in self._animations.keys():
            self._animations[key] = import_sprite(character_path + key)

    def update(self, movement_right, traps) -> int:
        self._rect.x += movement_right * self._move_speed
        self.animate()
        self._orientation_right = True if movement_right == 1 else False
        if len(self._rect.collidelistall(traps)) != 0:
            return False
        return True

    def changeOrientation(self, movement_right):
        if movement_right == 1 and not self._orientation_right:
            self._orientation_right = True
            self._image = pygame.transform.flip(self._image, True, False)
        elif movement_right == -1 and self._orientation_right:
            self._orientation_right = False
            self._image = pygame.transform.flip(self._image, True, False)

    def draw(self, screen):
        screen.blit(self._image, (self._rect.x, self._rect.y))

    def getX(self):
        return self._rect.x

    def getY(self):
        return self._rect.y
