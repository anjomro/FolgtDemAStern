from typing import Dict


class Terrain:
    terrain_cache: Dict[int, 'Terrain'] = {}

    cost: int

    def __new__(cls, terrain_number: int):
        if terrain_number in cls.terrain_cache.keys():
            return cls.terrain_cache.get(terrain_number)
        else:
            new_terrain =  object.__new__(cls)
            Terrain.terrain_cache[terrain_number] = new_terrain
            return new_terrain

    def __init__(self, terrain_number: int):
        self.terrain_number = terrain_number
        converter = [3,3,1,6,4]
        #Todo: Write interface for entering custom costs
        self.cost = converter[terrain_number]

    @staticmethod
    def get_cheapest_terrain_cost() -> int:
        """
        Finds the cheapest terrain cost
        :return: Minimum tarrain cost as integer
        """
        # Cast the dict of terrains into a list, get the first element and assign cost
        cheapest_terrain_cost = list(Terrain.terrain_cache.values())[0].cost
        for terrain in Terrain.terrain_cache.values():
            if terrain.cost < cheapest_terrain_cost:
                cheapest_terrain_cost = terrain.cost
        return cheapest_terrain_cost

    @staticmethod
    def get_max_terrain_cost() -> int:
        """
        Finds the most expensive terrain cost
        :return: Maximum terrain cost as integer
        """
        max_terrain_cost = list(Terrain.terrain_cache.values())[0].cost
        for terrain in Terrain.terrain_cache.values():
            if terrain.cost > max_terrain_cost:
                max_terrain_cost = terrain.cost
        return max_terrain_cost

    def is_water(self) -> bool:
        """
        Used to check if a terrain is water
        :return: True if terrain is water
        """
        return self.terrain_number == 0
