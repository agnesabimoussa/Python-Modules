class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(f"Caught GardenError: {message}")

    def __str__(self):
        return super().__str__()


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(f"Caught PlantError: {message}")

    def __str__(self):
        return super().__str__()


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(f"Caught WaterError: {message}")

    def __str__(self):
        return super().__str__()


def testing_errors() -> None:
    print("Testing PlantError...")
    raise PlantError("The tomato plant is wilting!\n")

    print("Testing WaterError...\n")
    raise WaterError(" Not enough water in the tank!\n")

    print("Testing catching all garden errors...")
    raise GardenError("The tomato plant is wilting!\n")
    raise GardenError("Not enough water in the tank!\n")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("All custom error types work correctly!")