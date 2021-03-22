import PyInstaller.__main__
import sys

'''
Not execute this file with pipenv Dev-Mode enabled so that the module Pyinstaller is available!
Command could be e.g. on Linux: pipenv install --dev && pipenv run python build-executable.py
'''

if sys.platform.startswith('linux') or sys.platform.startswith('freebsd') or sys.platform.startswith('darwin'):
    print("Building for {}".format(sys.platform))
    PyInstaller.__main__.run([
        '--onefile', #'--windowed',
        '--name=FolgtDemAStern',
        '--add-data=resources/gelaende_001.csv:resources/',
        'main.py'
    ])
elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    print("Building for Windows ({})".format(sys.platform))
    PyInstaller.__main__.run([
        '--onefile', #'--windowed',
        '--name=FolgtDemAStern',
        '--add-data=resources/gelaende_001.csv;resources/',
        'main.py'
    ])
else:
    print("Your current platform (known to Python as '{}' isnt supported for building an executable for now!)".format(sys.platform))