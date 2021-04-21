# Debug

> Auto-generated documentation for [boot.Debug](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Debug.py) module.

- [FolgtDemAStern](../README.md#folgtdemastern-index) / [Modules](../README.md#folgtdemastern-modules) / [Boot](index.md#boot) / Debug
    - [Debug](#debug)
        - [Debug.print](#debugprint)
        - [Debug.set_active](#debugset_active)

## Debug

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Debug.py#L2)

```python
class Debug():
```

Class contains debug functionalities

### Debug.print

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Debug.py#L8)

```python
@staticmethod
def print(msg: str):
```

Simple debug print. Only prints if debug option is active

#### Arguments

- `msg` - Message to print

### Debug.set_active

[[find in source code]](https://github.com/anjomro/FolgtDemAStern/blob/master/boot/Debug.py#L17)

```python
@staticmethod
def set_active():
```

Call at the beginning of the program to activate debug functionalities
