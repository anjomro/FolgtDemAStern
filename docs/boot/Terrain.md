# Terrain

> Auto-generated documentation for [boot.Terrain](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Terrain.py) module.

- [FolgtDemAStern](../README.md#folgtdemastern-index) / [Modules](../README.md#folgtdemastern-modules) / [Boot](index.md#boot) / Terrain
    - [Terrain](#terrain)
        - [Terrain.get_cheapest_terrain_cost](#terrainget_cheapest_terrain_cost)
        - [Terrain.get_max_terrain_cost](#terrainget_max_terrain_cost)
        - [Terrain().init](#terraininit)
        - [Terrain().is_water](#terrainis_water)

## Terrain

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Terrain.py#L4)

```python
class Terrain():
    def __init__(terrain_number: int):
```

### Terrain.get_cheapest_terrain_cost

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Terrain.py#L48)

```python
@staticmethod
def get_cheapest_terrain_cost() -> int:
```

Finds the cheapest terrain cost

#### Returns

Minimum tarrain cost as integer

### Terrain.get_max_terrain_cost

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Terrain.py#L61)

```python
@staticmethod
def get_max_terrain_cost() -> int:
```

Finds the most expensive terrain cost

#### Returns

Maximum terrain cost as integer

### Terrain().init

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Terrain.py#L19)

```python
def init(terrain_number: int):
```

### Terrain().is_water

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Terrain.py#L73)

```python
def is_water() -> bool:
```

Used to check if a terrain is water

#### Returns

True if terrain is water
