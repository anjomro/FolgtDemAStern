from typing import List, Tuple, Union

from boot.PathNotFoundException import PathNotFoundException
from boot.Terrain import Terrain


class Field:
    neighbours: List['Field']
    terrain: Terrain
    position: List[int]
    previous: Union['Field', None]
    cost_from_start: Union[int, None]
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
        """
        Finds path by recursively going through the previous fields. Should be executed on the target field
        :return: The path from self back to start as list of type Field
        """
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
            return True  # Recursion End
        elif self.terrain.terrain_number != 0 and self.previous.terrain.terrain_number == 0:
            return False
        else:
            return self.previous.boat_available()

    def reset(self):
        """
        Reset all field parameters to default. Should be used before new execution of A*
        """
        self.previous = None
        self.cost_from_start = None
        self.visited = False

    def get_position(self) -> Tuple[int, int]:
        """
        Gets the position of the field and returns it as Tuple
        :return: Coordinate Tuple (x, y)
        """
        return self.position[0], self.position[1]

    def set_position(self, x: int, y: int):
        """
        Stores the given coordinates as the position
        :param x: x coordinate
        :param y: y coordinate
        """
        self.position = [x, y]

    def get_estimated_cost(self, target: 'Field') -> int:
        """
        Estimates the minimum cost from the field to the target.
        :param target: the requested target field
        :return: Estimated cost as integer value
        """
        estimated_cost = abs(target.position[0] - self.position[0]) + abs(target.position[1] - self.position[1])
        estimated_cost *= Terrain.get_cheapest_terrain_cost()
        return estimated_cost

    def get_total_cost(self, target: 'Field') -> int:
        """
        Calculates the total cost from the start field to the target
        :param target: the requested target field
        :return: Total cost of the path passing through this field as integer value
        """
        estimated_cost = self.get_estimated_cost(target)
        return self.cost_from_start + self.terrain.cost + estimated_cost
