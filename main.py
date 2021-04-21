import os
from boot.Area import Area
import sys

from boot.Debug import Debug


def main():
    """
    Main entrypoint for method
    """
    #Debug.set_active()
    try:
        field_path = input("Select field CSV-File (Default: resources/gelaende_001.csv):")
        if field_path == "":
            field_path = "resources/gelaende_001.csv"
            if getattr(sys, 'frozen', False):
                #Special path for internal file when distributed as packaged app
                field_path = os.path.join(sys._MEIPASS, field_path)
            print("Using default file!")
        try:
            area = Area(field_path)
            area.start_window()
        except FileNotFoundError:
            print("File not found, exiting!")
        except UnicodeDecodeError:
            print(" The file cant be decoded, please ensure its a valid csv-format without any (maybe hidden) special characters")
    except KeyboardInterrupt:
        print("Program execution cancelled by user, exiting!")


if __name__ == '__main__':
    main()
