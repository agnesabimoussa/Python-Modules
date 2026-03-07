class Plant:
    """Represents a plant with growth simulation capabilities."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant.
        
        Args:
            name: Plant name
            height: Height in centimeters
            age: Age in days
        """
        self.name = name
        self.height = height
        self.p_age = age

    def grow(self) -> None:
        """Increase plant height by 1 centimeter."""
        self.height = self.height + 1

    def age(self) -> None:
        """Increase plant age by 1 day."""
        self.p_age = self.p_age + 1

    def get_info(self) -> None:
        """Display plant name, height, and age."""
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.p_age} days old")


if __name__ == "__main__":
    """ Testing the Plant class and demonstrating it's behavior """
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(1, 7):
        rose.age()
        rose.grow()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - 25}cm")
