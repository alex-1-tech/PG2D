import os
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._move_speed = 2
        self._image = pygame.Surface((int(os.environ.get('PLAYER_WIDTH')), int(os.environ.get('PLAYER_HEIGHT'))))
        self._image.fill(pygame.Color("#888888"))
        self._rect = pygame.Rect(x, y, int(os.environ.get('PLAYER_WIDTH')), int(os.environ.get('PLAYER_HEIGHT')))

    def update(self, movement_right, traps) -> int:
        self._rect.x += movement_right * self._move_speed

        if len(self._rect.collidelistall(traps)) != 0:
            return False
        return True

    def draw(self, screen):
        screen.blit(self._image, (self._rect.x, self._rect.y))

    def getX(self):
        return self._rect.x

    def getY(self):
        return self._rect.y
