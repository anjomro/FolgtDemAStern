import csv
from typing import List

from boot.Field import Field
from boot.Terrain import Terrain


class Area:
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
        #Set Neighbours for all fields
        row: List[Field]
        for i, row in enumerate(self.fields):
            field: Field
            for j, field in enumerate(row):
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
