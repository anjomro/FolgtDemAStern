from typing import Union

import pygame

from boot.Area import Area
from boot.Field import Field

if __name__ == '__main__':
    area = Area("resources/gelaende_001.csv")
    area.draw_area()

    pygame.display.update()

    start: Union[Field, None] = None
    target: Union[Field, None] = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = area.convert_mouse_to_field(list(pygame.mouse.get_pos()))
                #event.button: 1 is for left mouse click, 2 for middle, 3 for right
                if event.button == 3:
                    start = area.fields[pos[0]][pos[1]]
                elif event.button == 1:
                    if start is None:
                        start = area.fields[pos[0]][pos[1]]
                    else:
                        target = area.fields[pos[0]][pos[1]]
                if start is not None:
                    area.draw_area()
                    if start is not None and target is not None:
                        path = area.get_path(start, target)
                        area.draw_path(path)
                    else:
                        area.draw_path([start])
                pygame.display.update()
        pygame.display.update()
