from typing import List, Tuple

from boot.PathNotFoundException import PathNotFoundException
from boot.Terrain import Terrain


class Field:
    neighbours: List['Field']
    terrain: Terrain
    position: List[int]
    previous: 'Field'
    cost_from_start: int
    visited: bool

    def __init__(self, terrain: Terrain):
        self.terrain = terrain
        self.visited = False

    def __str__(self):
        return "F({}|{})-T{}".format(self.position[0], self.position[1], self.terrain.terrain_number)

    def set_neighbours(self, neighbours: List['Field']):
        """
        Sets the list of all fields that are directly reachable
        :param neighbours: List of all directly reachable neighbours
        """
        self.neighbours = neighbours

    def set_as_start_field(self):
        """
        Sets Field as start field by linking 'previous' attribute to itself
        """
        self.previous = self

    def is_start_field(self) -> bool:
        """
        :return: Returns True when Field is start, False if not
        """
        try:
            return self is self.previous
        except AttributeError: # In Case previous Field is not yet set
            return False

    def recurse_path(self) -> List['Field']:
        if self.is_start_field():
            return [self]
        else:
            try:
                return self.previous.recurse_path() + [self]
            except AttributeError:
                raise PathNotFoundException("Target field isnt connected to startpoint.")

    def boat_available(self) -> bool:
        """
        Checks for availability of the boat recursively
        :return: Boolean is true, if boat is still available
        """
        if self.is_start_field():
            return True # Recursion End
        elif self.terrain.terrain_number != 0 and self.previous.terrain.terrain_number == 0:
            return False
        else:
            return self.previous.boat_available()

    def get_position(self) -> Tuple[int, int]:
        return self.position[0], self.position[1]

    def set_position(self, x: int, y: int):
        self.position = [x, y]

    def get_total_cost(self, target: 'Field') -> int:
        estimated_cost = abs(target.position[0] - self.position[0]) + abs(target.position[1] - self.position[1])
        estimated_cost *= Terrain.get_cheapest_terrain_cost()
        return self.cost_from_start + self.terrain.cost + estimated_cost
