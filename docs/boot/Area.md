# Area

> Auto-generated documentation for [boot.Area](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py) module.

- [FolgtDemAStern](../README.md#folgtdemastern-index) / [Modules](../README.md#folgtdemastern-modules) / [Boot](index.md#boot) / Area
    - [Area](#area)
        - [Area().__a_star](#area__a_star)
        - [Area.cls](#areacls)
        - [Area().convert_mouse_to_field](#areaconvert_mouse_to_field)
        - [Area().draw_area](#areadraw_area)
        - [Area().draw_path](#areadraw_path)
        - [Area().get_path](#areaget_path)
        - [Area.get_path_cost](#areaget_path_cost)
        - [Area().read_csv](#arearead_csv)
        - [Area().reset](#areareset)
        - [Area().start_window](#areastart_window)

## Area

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L13)

```python
class Area():
    def __init__(filename: str):
```

### Area().__a_star

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L171)

```python
def __a_star(start: Field, target: Field, force_land: bool = False):
```

Implementation of the A* algorithm for pathfinding with implementation of a one-time usable boat to cross water

#### Arguments

- `start` - Requestet start Field
- `target` - Requestet target Field
- `force_land` - Optional boolean parameter to force the algorithm to prefer land fields.
                   Used for the second iteration if the first one did not find a valid path.

#### See also

- [Field](Field.md#field)

### Area.cls

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L98)

```python
@staticmethod
def cls():
```

Clears console screen output

### Area().convert_mouse_to_field

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L163)

```python
def convert_mouse_to_field(pos: List[int]) -> List[int]:
```

Assigns mouse coordinates in pixels to the selected field

#### Arguments

- `pos` - Mouse pointer position relative to the pygame window in pixels

#### Returns

Coordinates of the clicked field

### Area().draw_area

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L78)

```python
def draw_area():
```

Does the setup for the pygame window and draws the CSV data as a colored field

### Area().draw_path

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L146)

```python
def draw_path(path: List[Field]):
```

Draws the given list of Fields as a path with red dots on land and yellow dots on water

#### Arguments

- `path` - Path as a list of objects of the type Field

### Area().get_path

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L243)

```python
def get_path(start: Field, target: Field) -> List[Field]:
```

Calls the A* function with the given parameters and converts the result into a list of type Field.
Catches PathNotFoundException if no valid path was found. Also starts a second iteration of the A*
algorithm avoiding water fields if the first one does not work.

#### Arguments

- `start` - Start field of the path
- `target` - Target field of the path

#### Returns

Found path as a list of type Field including start and target. List is empty if no path was found.

#### See also

- [Field](Field.md#field)

### Area.get_path_cost

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L269)

```python
@staticmethod
def get_path_cost(path: List[Field]) -> int:
```

Adds up the complete cost of a path

#### Arguments

- `path` - Path as list of type Field

#### Returns

Path cost as integer value

### Area().read_csv

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L42)

```python
def read_csv(filename: str, delimiter: str = ';'):
```

Reads a csv file that describes the area.
Each row presents one row of the are, fields are separated using the given delimiter

#### Arguments

- `filename` - filename of the csv file to process
- `delimiter` - delimiter used to process the csv file

### Area().reset

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L234)

```python
def reset():
```

Resets all fields in Area so that the A*-Algorithmus can be run again

### Area().start_window

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Area.py#L105)

```python
def start_window():
```

Handles the pygame window input including the mouse interaction. Calls the get_path function
