from typing import List

from boot.Terrain import Terrain


class Field:
    neighbours: List['Field']

    def __init__(self, terrain: Terrain):
        self.terrain = terrain

    def __str__(self):
        return "Field, T{}".format(self.terrain.terrain_number)

    def set_neighbours(self, neighbours: List['Field']):
        """
        Sets the list of all fields that are directly reachable
        :param neighbours: List of all directly reachable neighbours
        """
        self.neighbours = neighbours