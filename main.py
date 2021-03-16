import pygame

from boot.Area import Area

if __name__ == '__main__':
    area = Area("resources/gelaende_001.csv")
    area.draw_area()
    start = area.fields[0][2]
    target = area.fields[33][18]
    path = area.get_path(start, target)
    area.draw_path(path)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
