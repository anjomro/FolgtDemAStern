import os

from boot.Area import Area
import sys

if __name__ == '__main__':
    preset = "resources/gelaende_001.csv"
    if getattr(sys, 'frozen', False):
        preset = os.path.join(sys._MEIPASS, preset)
    area = Area(preset)
    area.start_window()
