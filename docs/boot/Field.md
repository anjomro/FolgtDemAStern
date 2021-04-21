# Field

> Auto-generated documentation for [boot.Field](../../boot/Field.py) module.

- [Folgtdemastern](../README.md#folgtdemastern-index) / [Modules](../MODULES.md#folgtdemastern-modules) / [Boot](index.md#boot) / Field
    - [Field](#field)
        - [Field().boat_available](#fieldboat_available)
        - [Field().get_estimated_cost](#fieldget_estimated_cost)
        - [Field().get_position](#fieldget_position)
        - [Field().get_total_cost](#fieldget_total_cost)
        - [Field().is_start_field](#fieldis_start_field)
        - [Field().recurse_path](#fieldrecurse_path)
        - [Field().reset](#fieldreset)
        - [Field().set_as_start_field](#fieldset_as_start_field)
        - [Field().set_neighbours](#fieldset_neighbours)
        - [Field().set_position](#fieldset_position)

## Field

[[find in source code]](../../boot/Field.py#L7)

```python
class Field():
    def __init__(terrain: Terrain):
```

#### See also

- [Terrain](Terrain.md#terrain)

### Field().boat_available

[[find in source code]](../../boot/Field.py#L57)

```python
def boat_available() -> bool:
```

Checks for availability of the boat recursively

#### Returns

Boolean is true, if boat is still available

### Field().get_estimated_cost

[[find in source code]](../../boot/Field.py#L92)

```python
def get_estimated_cost(target: 'Field') -> int:
```

Estimates the minimum cost from the field to the target.

#### Arguments

- `target` - the requested target field

#### Returns

Estimated cost as integer value

### Field().get_position

[[find in source code]](../../boot/Field.py#L77)

```python
def get_position() -> Tuple[int, int]:
```

Gets the position of the field and returns it as Tuple

#### Returns

Coordinate Tuple (x, y)

### Field().get_total_cost

[[find in source code]](../../boot/Field.py#L102)

```python
def get_total_cost(target: 'Field') -> int:
```

Calculates the total cost from the start field to the target

#### Arguments

- `target` - the requested target field

#### Returns

Total cost of the path passing through this field as integer value

### Field().is_start_field

[[find in source code]](../../boot/Field.py#L35)

```python
def is_start_field() -> bool:
```

#### Returns

Returns True when Field is start, False if not

### Field().recurse_path

[[find in source code]](../../boot/Field.py#L44)

```python
def recurse_path() -> List['Field']:
```

Finds path by recursively going through the previous fields. Should be executed on the target field

#### Returns

The path from self back to start as list of type Field

### Field().reset

[[find in source code]](../../boot/Field.py#L69)

```python
def reset():
```

Reset all field parameters to default. Should be used before new execution of A*

### Field().set_as_start_field

[[find in source code]](../../boot/Field.py#L29)

```python
def set_as_start_field():
```

Sets Field as start field by linking 'previous' attribute to itself

### Field().set_neighbours

[[find in source code]](../../boot/Field.py#L22)

```python
def set_neighbours(neighbours: List['Field']):
```

Sets the list of all fields that are directly reachable

#### Arguments

- `neighbours` - List of all directly reachable neighbours

### Field().set_position

[[find in source code]](../../boot/Field.py#L84)

```python
def set_position(x: int, y: int):
```

Stores the given coordinates as the position

#### Arguments

- `x` - x coordinate
- `y` - y coordinate
