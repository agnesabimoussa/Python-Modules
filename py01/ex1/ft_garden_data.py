class Plant:
    """Represents a plant with name, height, and age attributes."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant.
        
        Args:
            name: Plant name
            height: Height in centimeters
            age: Age in days
        """
        self.name = name
        self.height = height
        self.age = age


def plants_report(plants: list[Plant]) -> None:
    """Print a registry of all plants.
    
    Args:
        plants: List of plant objects
    """
    print("=== Garden Plant Registry ===")
    for i in range(len(plants)):
        plant = plants[i]
        print(f"{plant.name.capitalize()}: {plant.height}cm, "
              f"{plant.age} days old")


if __name__ == "__main__":
    """Main function that creates plants and calls the plants_report method
    with the list of plants
    """
    rose_plant = Plant("Rose", 25, 30)
    sunflower_plant = Plant("Sunflower", 80, 45)
    cactus_plant = Plant("Cactus", 15, 120)
    plants = [rose_plant, sunflower_plant, cactus_plant]
    plants_report(plants)
