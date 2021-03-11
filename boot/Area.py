import csv
from typing import List

from boot.Field import Field
from boot.Terrain import Terrain


class Area:
    open_list: List[Field]
    closed_list: List[Field]

    def __init__(self, filename: str):
        """
        Creates a new Area object based on a csv file
        :param filename: name of the file from which the area data is read
        """
        self.fields: List[List[Field]] = []
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
            field: Field
            for j, field in enumerate(row):
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

    def a_star(self, start: Field, target: Field):
        current_field = start
        current_field.cost_from_start = 0
        self.open_list.append(current_field)
        while current_field != target:
            for field in self.open_list:
                if field.get_total_cost(target) < current_field.get_total_cost(target):
                    current_field = field
            for neighbour in current_field.neighbours:
                if neighbour.visited:
                    continue
                if neighbour.terrain.is_water():
                    if not neighbour.boat_available():
                        continue
                    else:
                        self.open_list.append(neighbour)
                        neighbour.visited = True
            self.open_list.remove(current_field)
            self.closed_list.append(current_field)
