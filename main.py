from boot.Area import Area

if __name__ == '__main__':
    area = Area("resources/gelaende_001.csv")
    start = area.fields[0][2]
    target = area.fields[10][10]
    path = area.get_path(start, target)
    print(path)