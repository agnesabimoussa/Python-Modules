class InvalidPlant(Exception):
    pass


class Plant:
    def __init__(self, name):
        self.name = name


def water_plants(plant_list: list[Plant]):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise InvalidPlant
            print(f"Watering {plant.name}")
    except InvalidPlant:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plants = [Plant("tomato"), Plant("lettuce"), Plant("carrots")]
    water_plants(plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    plants = [Plant("tomato"), None]
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")
