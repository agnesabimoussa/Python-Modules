class Plant:
    """Represents a plant with basic attributes."""

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

    def get_info(self) -> None:
        """Display plant creation information."""
        print(f"Created: {self.name.capitalize()}"
              f"({self.height}cm, {self.age}days)")


class PlantFactory:
    """Manages a collection of plant objects."""

    def __init__(self, plants: list[Plant]):
        """Initialize factory with a list of plants.
        
        Args:
            plants: List of plant objects
        """
        self.plants = plants

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the factory.
        
        Args:
            plant: Plant object to add
        """
        self.plants.append(plant)

    def display_plants(self) -> None:
        """Display all plants in the factory."""
        print("=== Plant Factory Output ===")
        for i in range(len(self.plants)):
            self.plants[i].get_info()
        print(f"Total plants created: {len(self.plants)}")


if __name__ == "__main__":
    """Main function that creates a new factory, adds new
    plants and prints their information
    """
    plants = [Plant("Rose", 25, 30), Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90), Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120)]
    factory = PlantFactory(plants)
    factory.display_plants()
