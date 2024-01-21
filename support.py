import sys
from os import walk
import pygame


def import_sprite(path: str) -> list:
    """
    :param path: the path to the directory with images
    :return: list images : pygame image
    """
    surface_list = []
    try:
        for _, __, img_file in walk(path):
            for image in img_file:
                full_path = f"{path}/{image}"
                img_surface = pygame.image.load(full_path).convert_alpha()
                surface_list.append(img_surface)
        if len(surface_list) == 0:
            raise FileNotFoundError("the folder is empty")
    except FileNotFoundError as e:
        print("Warning: %s" % e)
    return surface_list
