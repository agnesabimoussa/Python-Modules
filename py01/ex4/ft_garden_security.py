class SecurePlant:
    """Represents a plant with validated attribute setters."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with validation.
        
        Args:
            name: Plant name
            height: Height in centimeters
            age: Age in days
        """
        self.name = name
        self.height = height
        self.age = age
        print("Plant created:", self.name.capitalize())

    def set_height(self, height: int) -> None:
        """Set plant height if non-negative.
        
        Args:
            height: Height in centimeters
        """
        if height >= 0:
            self.height = height
            print(f"Height updated: {self.height}cm [OK]")
        else:
            print("Security: Negative height rejected")

    def get_height(self) -> int:
        """Return the plant height.
        
        Returns:
            Height in centimeters
        """
        return self.height

    def set_age(self, age: int) -> None:
        """Set plant age if non-negative.
        
        Args:
            age: Age in days
        """
        if age >= 0:
            self.age = age
            print(f"Age updated: {self.age} days [OK]")
        else:
            print("Security: Negative age rejected")

    def get_info(self) -> None:
        """Display plant information."""
        print(f"{self.name.capitalize()}: ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("rose", 0, 0)
    plant.set_height(25)
    plant.set_age(30)
    print("")
    print("Invalid operation attenpt: height -5cm [REJECTED]")
    plant.set_height(-5)
    print("Current plant: ", end="")
    plant.get_info()
