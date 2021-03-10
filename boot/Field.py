from typing import List, Tuple

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

    def __str__(self):
        return "Field, T{}".format(self.terrain.terrain_number)

    def set_neighbours(self, neighbours: List['Field']):
        """
        Sets the list of all fields that are directly reachable
        :param neighbours: List of all directly reachable neighbours
        """
        self.neighbours = neighbours

    def boat_available(self) -> bool:
        """
        Checks for availability of the boat recursively
        :return: Boolean is true, if boat is still available
        """
        if self.terrain.terrain_number != 0 and self.previous.terrain.terrain_number == 0:
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
