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
        converter = [2,2,1,4,3]
        #Todo: Write interface for entering custom costs
        self.cost = converter[terrain_number]

    @staticmethod
    def get_cheapest_terrain_cost() -> int:
        # Cast the dict of terrains into a list, get the first element and assign cost
        cheapest_terrain_cost = list(Terrain.terrain_cache.values())[0].cost
        for terrain in Terrain.terrain_cache.values():
            if terrain.cost < cheapest_terrain_cost:
                cheapest_terrain_cost = terrain.cost
        return cheapest_terrain_cost

    def is_water(self) -> bool:
        return self.terrain_number == 0
