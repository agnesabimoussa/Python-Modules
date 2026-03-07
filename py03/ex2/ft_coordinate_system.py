import sys
import math

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    if (len(sys.argv) <= 1) or (len(sys.argv) != 2 and len(sys.argv) != 4):
        print("Invalid arguments!")
        print("Usage 1: python3 ft_coordinate_system.py \"x,y,z\"")
        print("Usage 2: python3 ft_coordinate_system.py x y z")
    else:
        coordinates: list = []
        if len(sys.argv) == 2:
            coordinates = sys.argv[1].split(",")
        elif len(sys.argv) == 4:
            for arg in sys.argv[1:]:
                coordinates.append(arg)
        try:
            for i in range(len(coordinates)):
                coordinates[i] = int(coordinates[i])
            coordinates = tuple(coordinates)
            # tuple unpacking
            (x, y, z) = coordinates
            distance = math.sqrt((x ** 2) + (y ** 2) + (z ** 2))
            print(f"Position created: {coordinates}")
            print(
                f"Distance between (0, 0, 0) and {coordinates}:"
                f" {round(distance, 2)}")
        except ValueError:
            print("Error parsing coordinates: ", end="")
            print(
                f"invalid literal for int() with base 10: '{coordinates[i]}'")
