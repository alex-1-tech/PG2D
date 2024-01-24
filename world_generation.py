import os
import random
import pygame


class World:
    def __init__(self):
        self._size = 10
        self._min_delta = 100
        self._max_delta = 200
        self._left_traps, self._left_y = self.firstInitialization()
        self._right_traps, self._right_y = self.firstInitialization()
        self._stars, self._stars_y = self.firstInitialization(True)
        self.rectangles = []
        self._trap = pygame.image.load('sprites/trap.png')
        self._trap_inv = pygame.transform.flip(self._trap, True, False)
        self._star = pygame.image.load('sprites/star.png')
        self._height = 0
        self.score = 0

    def generationY(self, y: int, is_star: bool = False) -> int:
        if not is_star:
            return random.randint(self._min_delta + y, self._max_delta + y)
        return random.randint(self._min_delta + 300 + y, self._max_delta + y + 300)

    def firstInitialization(self, is_star: bool = False) -> (list, int):
        traps = list()
        y = 400
        for _ in range(self._size):
            y = self.generationY(y, is_star)
            traps.append(y)
        return traps, y

    def update(self):
        self._height += 1
        self._left_y -= 1
        self._right_y -= 1
        self._stars_y -= 1
        for i in range(self._size):
            self._left_traps[i] -= 1
            self._right_traps[i] -= 1
            self._stars[i] -= 1
            if self._height > int(os.environ.get("FINISH_HEIGHT")):
                for j in range(self._size):
                    if self._stars[j] > max(self._left_y, self._right_y):
                        self._stars[j] = -1
                continue

            if self._left_traps[i] < 0:
                self._left_y = self.generationY(self._left_y)
                self._left_traps[i] = self._left_y

            if self._right_traps[i] < 0:
                self._right_y = self.generationY(self._right_y)
                self._right_traps[i] = self._right_y

            if self._stars[i] < 0:
                self._stars_y = self.generationY(self._stars_y, True)
                self._stars[i] = self._stars_y

    def isFinished(self):
        return (max(self._left_y, self._right_y) - self._min_delta) < 0

    def draw(self, screen, player_collide: pygame.rect):
        self.rectangles = []

        for y in self._left_traps:
            self.rectangles.append(screen.blit(self._trap, (int(os.environ.get('WALL_SIZE')) - 2,
                                                            int(os.environ.get("HEIGHT")) - y)))

        for y in self._right_traps:
            self.rectangles.append(screen.blit(self._trap_inv,
                                               (int(os.environ.get('WIDTH')) - int(
                                                   os.environ.get('WALL_SIZE')) - 38,
                                                int(os.environ.get("HEIGHT")) - y)))

        for y in range(len(self._stars)):
            star = screen.blit(self._star, (100, int(os.environ.get("HEIGHT")) - self._stars[y]))
            if player_collide.colliderect(star):
                self.score += 1
                self._stars[y] = -1
