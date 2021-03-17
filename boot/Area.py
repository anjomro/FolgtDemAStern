import csv
import pygame
from typing import List

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
        Each row presents one row of the are, fields are sperated using the given delimiter
        :param filename: filname of the csv file to process
        :param delimiter: delimiter used to process the csv file
        """
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            row: List[str]
            for row in reader:
                if '' not in row:
                    #Append one row at a time, for each element create a field with terrain corresponding to read number
                    self.fields.append(list(map(lambda x: Field(Terrain(int(x))), row)))
        #Set Neighbours for all fields, set coordinates
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
        if self.fields.__len__() < 1:
            return
        self.display = pygame.display.set_mode([self.width * self.DRAW_SIZE, self.height * self.DRAW_SIZE])
        row: List[Field]
        for x, row in enumerate(self.fields):
            field: Field
            for y, field in enumerate(row):
                pygame.draw.rect(self.display, self.color_cache[field.terrain.terrain_number],
                                 (x * self.DRAW_SIZE, y * self.DRAW_SIZE, self.DRAW_SIZE, self.DRAW_SIZE))

    def draw_path(self, path: List[Field]):
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
        return [int(pos[0]/self.DRAW_SIZE), int(pos[1]/self.DRAW_SIZE)]

    def __a_star(self, start: Field, target: Field):
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
            for field in self.open_list[1:]:
                if field.get_total_cost(target) < current_field.get_total_cost(target):
                    current_field = field
            for neighbour in current_field.neighbours:
                if not neighbour.visited and (not neighbour.terrain.is_water() or current_field.boat_available()):
                    self.open_list.append(neighbour)
                    neighbour.cost_from_start = current_field.cost_from_start + current_field.terrain.cost
                    neighbour.visited = True
                    neighbour.previous = current_field
            if current_field in self.open_list:
                self.open_list.remove(current_field)
            self.closed_list.append(current_field)

    def reset(self):
        """
        Resets all fields in Area so that the A*-Algorithmus can be run again
        """
        for row in self.fields:
            for field in row:
                field.reset()

    def get_path(self, start: Field, target: Field) -> List[Field]:
        self.reset()
        self.__a_star(start, target)
        path: List[Field] = []
        try:
            path = target.recurse_path()
        except PathNotFoundException:
            path = [start, target]
        finally:
            return path