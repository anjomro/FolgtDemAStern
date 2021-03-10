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
        converter = [1,2,1,3,2]
        #Todo: Write interface for entering custom costs
        self.cost = converter[terrain_number]