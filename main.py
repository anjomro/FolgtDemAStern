import pygame

from boot.Area import Area

if __name__ == '__main__':
    area = Area("resources/gelaende_001.csv")
    area.draw_area()

    pygame.display.update()

    start_set = False
    target_set = False
    while not target_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = area.convert_mouse_to_field(list(pygame.mouse.get_pos()))
                if not start_set:
                    start = area.fields[pos[0]][pos[1]]
                    area.draw_path([start])
                    pygame.display.update()
                    start_set = True
                elif not target_set:
                    target = area.fields[pos[0]][pos[1]]
                    target_set = True

    path = area.get_path(start, target)
    area.draw_path(path)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
