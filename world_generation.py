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
        self.rectangles = []

    def generationY(self, y: int) -> int:
        return random.randint(self._min_delta + y, self._max_delta + y)

    def firstInitialization(self) -> (list, int):
        traps = list()
        y = 0
        for _ in range(self._size):
            y = self.generationY(y)
            traps.append(y)
        return traps, y

    def update(self):
        self._left_y -= 1
        self._right_y -= 1
        for i in range(self._size):
            self._left_traps[i] -= 1
            if self._left_traps[i] < 0:
                self._left_y = self.generationY(self._left_y)
                self._left_traps[i] = self.generationY(self._left_y)

            self._right_traps[i] -= 1
            if self._right_traps[i] < 0:
                self._right_y = self.generationY(self._right_y)
                self._right_traps[i] = self.generationY(self._right_y)

    def draw(self, screen):
        self.rectangles = []
        width_trap = 20
        height_trap = 10

        for y in self._left_traps:
            self.rectangles.append(pygame.draw.rect(screen,
                                                    (255, 0, 0),
                                                    (int(os.environ.get('WALL_SIZE')),
                                                     int(os.environ.get("HEIGHT")) - y,
                                                     width_trap,
                                                     10)
                                                    ))

        for y in self._right_traps:
            self.rectangles.append(pygame.draw.rect(screen,
                                                    (255, 0, 0),
                                                    (int(os.environ.get('WIDTH')) - int(
                                                        os.environ.get('WALL_SIZE')) - width_trap,
                                                     int(os.environ.get("HEIGHT")) - y,
                                                     width_trap,
                                                     height_trap)
                                                    )
                                   )
