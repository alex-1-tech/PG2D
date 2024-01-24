from os import walk
import pygame


def createResult(table):
    font = pygame.font.Font(None, 24)
    ans = []
    results = table.getTopScores()
    for number in range(5):
        if number + 1 > len(results):
            ans.append(
                font.render(f"{number+1}: - -", True, (0, 0, 0))
            )
        else:
            ans.append(
                font.render(f"{number+1}:{results[number][0]} {results[number][1]}", True, (0, 0, 0))
            )
    return ans


def importSprite(path: str) -> list:
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
