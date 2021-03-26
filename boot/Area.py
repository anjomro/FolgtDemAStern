import csv
import pygame
from typing import List, Union

from boot.Debug import Debug
from boot.Field import Field
from boot.PathNotFoundException import PathNotFoundException
from boot.Terrain import Terrain


class Area:
    open_list: List[Field]
    closed_list: List[Field]

    width: int
    height: int
    DRAW_SIZE = 15
    INDENT = int(DRAW_SIZE/3)

    color_cache = {
        0: [28, 151, 217],
        1: [68, 230, 18],
        2: [87, 87, 87],
        3: [102, 90, 44],
        4: [37, 77, 31]
    }

    display = None

    def __init__(self, filename: str):
        """
        Creates a new Area object based on a csv file
        :param filename: name of the file from which the area data is read
        """
        self.fields: List[List[Field]] = []
        self.open_list: List[Field] = []
        self.closed_list: List[Field] = []
        self.read_csv(filename)

    def read_csv(self, filename: str, delimiter: str = ';'):
        """
        Reads a csv file that describes the area.
        Each row presents one row of the are, fields are separated using the given delimiter
        :param filename: filename of the csv file to process
        :param delimiter: delimiter used to process the csv file
        """
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            row: List[str]
            for row in reader:
                if '' not in row:
                    # Append one row at a time, for each element create a field with terrain corresponding to read number
                    self.fields.append(list(map(lambda x: Field(Terrain(int(x))), row)))
        # Set Neighbours for all fields, set coordinates
        row: List[Field]
        for i, row in enumerate(self.fields):
            self.width = i
            field: Field
            for j, field in enumerate(row):
                self.height = j
                field.set_position(i, j)
                neighbours: List[Field] = []
                # Potentially available neighbours:
                #    b
                #  a x d
                #    c
                for offsets in [
                    [-1,0], # a
                    [0,-1], # b
                    [0,1],  # c
                    [1,0]]: # d
                    if (0 <= i + offsets[0] < len(self.fields)) and (0 <= j + offsets[1] < len(self.fields[i])):
                        neighbours.append(self.fields[i + offsets[0]][j + offsets[1]])
                field.set_neighbours(neighbours)

    def draw_area(self):
        """
        Does the setup for the pygame window and draws the CSV data as a colored field
        """
        if self.fields.__len__() < 1:
            return
        self.display = pygame.display.set_mode([(self.width + 1) * self.DRAW_SIZE, (self.height + 1) * self.DRAW_SIZE])
        row: List[Field]
        for x, row in enumerate(self.fields):
            field: Field
            for y, field in enumerate(row):
                pygame.draw.rect(self.display, self.color_cache[field.terrain.terrain_number],
                                 (x * self.DRAW_SIZE, y * self.DRAW_SIZE, self.DRAW_SIZE, self.DRAW_SIZE))

    def start_window(self):
        """
        Handles the pygame window input including the mouse interaction. Calls the get_path function
        """
        self.draw_area()
        pygame.display.update()
        start: Union[Field, None] = None
        target: Union[Field, None] = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = self.convert_mouse_to_field(list(pygame.mouse.get_pos()))
                    # event.button: 1 is for left mouse click, 2 for middle, 3 for right
                    if event.button == 3:
                        start = self.fields[pos[0]][pos[1]]
                    elif event.button == 1:
                        if start is None:
                            start = self.fields[pos[0]][pos[1]]
                        else:
                            target = self.fields[pos[0]][pos[1]]
                    if start is not None:
                        self.draw_area()
                        if target is not None:
                            path = self.get_path(start, target)
                            self.draw_path(path)
                        else:
                            self.draw_path([start])
                    pygame.display.update()
            pygame.display.update()

    def draw_path(self, path: List[Field]):
        """
        Draws the given list of Fields as a path with red dots on land and yellow dots on water
        :param path: Path as a list of objects of the type Field
        """
        if self.display is None:
            return
        for field in path:
            color = [255, 0, 0]
            if field.terrain.is_water():
                color = [255, 255, 0]
            x = field.position[0] * self.DRAW_SIZE + self.INDENT
            y = field.position[1] * self.DRAW_SIZE + self.INDENT
            pygame.draw.rect(self.display, color, (x, y, self.INDENT, self.INDENT))

    def convert_mouse_to_field(self, pos: List[int]) -> List[int]:
        """
        Assigns mouse coordinates in pixels to the selected field
        :param pos: Mouse pointer position relative to the pygame window in pixels
        :return: Coordinates of the clicked field
        """
        return [int(pos[0]/self.DRAW_SIZE), int(pos[1]/self.DRAW_SIZE)]

    def __a_star(self, start: Field, target: Field, force_land: bool = False):
        """
        Implementation of the A* algorithm for pathfinding with implementation of a one-time usable boat to cross water
        :param start: Requestet start Field
        :param target: Requestet target Field
        :param force_land: Optional boolean parameter to force the algorithm to prefer land fields.
                           Used for the second iteration if the first one did not find a valid path.
        """
        start.set_as_start_field()
        current_field = start
        current_field.visited = True
        current_field.cost_from_start = 0
        self.open_list = [current_field]
        self.closed_list = []
        while current_field != target:
            if len(self.open_list) > 0:
                current_field = self.open_list[0]
            else:
                return
            # Iterate over open list to find the element with shortest estimated cost to target
            for field in self.open_list:
                # This is the standard approach
                if field.get_total_cost(target) < current_field.get_total_cost(target):
                    current_field = field

            # Check every neighbour (set in read_csv function)
            for neighbour in current_field.neighbours:
                # If the neighbour is in one of the both lists (= visited), check if we found a shorter path
                if neighbour.visited and (not neighbour.terrain.is_water() or current_field.boat_available()):
                    if current_field.get_total_cost(target) < neighbour.get_total_cost(target):
                        neighbour.previous = current_field
                        neighbour.cost_from_start = current_field.cost_from_start + current_field.terrain.cost
                        if force_land and not current_field.terrain.is_water() and neighbour.terrain.is_water():
                            boat_penalty = Terrain.get_max_terrain_cost() * self.width * self.height
                            neighbour.cost_from_start += boat_penalty
                        # Move field from closed to open list if needed
                        if neighbour in self.closed_list:
                            self.closed_list.remove(neighbour)
                            self.open_list.append(neighbour)
                if not neighbour.visited and (not neighbour.terrain.is_water() or current_field.boat_available()):
                    self.open_list.append(neighbour)
                    neighbour.cost_from_start = current_field.cost_from_start + current_field.terrain.cost
                    if force_land and not current_field.terrain.is_water() and neighbour.terrain.is_water():
                        boat_penalty = Terrain.get_max_terrain_cost() * self.width * self.height
                        neighbour.cost_from_start += boat_penalty
                    neighbour.visited = True
                    neighbour.previous = current_field
            if current_field in self.open_list:
                self.open_list.remove(current_field)
            self.closed_list.append(current_field)
            if Debug.active:
                for item in self.open_list:
                    x = item.position[0] * self.DRAW_SIZE + self.INDENT
                    y = item.position[1] * self.DRAW_SIZE + self.INDENT
                    pygame.draw.rect(self.display, (255, 255, 255), (x, y, self.INDENT, self.INDENT))
                for item in self.closed_list:
                    x = item.position[0] * self.DRAW_SIZE + self.INDENT
                    y = item.position[1] * self.DRAW_SIZE + self.INDENT
                    pygame.draw.rect(self.display, (0, 0, 0), (x, y, self.INDENT, self.INDENT))
                pygame.display.update()

    def reset(self):
        """
        Resets all fields in Area so that the A*-Algorithmus can be run again
        """
        for row in self.fields:
            for field in row:
                field.reset()
        self.draw_area()

    def get_path(self, start: Field, target: Field) -> List[Field]:
        """
        Calls the A* function with the given parameters and converts the result into a list of type Field.
        Catches PathNotFoundException if no valid path was found. Also starts a second iteration of the A*
        algorithm avoiding water fields if the first one does not work.
        :param start: Start field of the path
        :param target: Target field of the path
        :return: Found path as a list of type Field including start and target. List is empty if no path was found.
        """
        self.reset()
        self.__a_star(start, target)
        path: List[Field] = []
        try:
            path = target.recurse_path()
        except PathNotFoundException:
            self.reset()
            self.__a_star(start, target, True)
            try:
                path = target.recurse_path()
            except PathNotFoundException:
                path = []
        finally:
            return path

    @staticmethod
    def get_path_cost(path: List[Field]) -> int:
        """
        Adds up the complete cost of a path
        :param path: Path as list of type Field
        :return: Path cost as integer value
        """
        total_cost = 0
        for field in path:
            total_cost += field.terrain.cost
        return total_cost
