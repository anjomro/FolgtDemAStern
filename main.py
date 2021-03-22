import os
from boot.Area import Area
import sys

from boot.Debug import Debug



def main():
    Debug.set_active()
    field_path = input("Select field CSV-File:")
    if field_path == "":
        field_path = "resources/gelaende_001.csv"
        if getattr(sys, 'frozen', False):
            field_path = os.path.join(sys._MEIPASS, field_path)
    try:
        area = Area(field_path)
        area.start_window()
    except FileNotFoundError:
        print("File not found, exiting!")
    except UnicodeDecodeError:
        print(" The file cant be decoded, please ensure its a valid csv-format without any (maybe hidden) special characters")

if __name__ == '__main__':
    main()
