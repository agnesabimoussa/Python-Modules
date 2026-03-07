def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(
            f"Error: water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_cases():
    print("Testing good values...")
    try:
        check_plant_health("tomato", 2, 3)
    except ValueError as e:
        print(e)

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 2, 10)
    except ValueError as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 12)
    except ValueError as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 2, 0)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_cases()
    print("\nAll error raising tests completed!")
