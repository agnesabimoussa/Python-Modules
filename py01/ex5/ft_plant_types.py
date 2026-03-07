class Plant:
    """Base class representing a plant."""

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
        """Display plant information based on subclass type."""
        # print(self.__class__)
        if isinstance(self, Flower):
            print(f"{self.name.capitalize()} (Flower): {self.height}cm, "
                  f"{self.age}days, {self.color}color")
            self.bloom()
        elif isinstance(self, Tree):
            print(f"{self.name.capitalize()} (Tree): {self.height}cm, "
                  f"{self.age}days, {self.trunk_diameter}cm diameter")
            self.produce_shade()
        elif isinstance(self, Vegetable):
            print(f"{self.name.capitalize()} (Vegetable): {self.height}cm, "
                  f"{self.age}days, {self.season}harvest")
            print(f"{self.name.capitalize()} is rich in "
                  f"{self.val}")
        else:
            print(f"{self.name.capitalize()}: {self.height}cm, "
                  f"{self.p_age} days old")


class Flower(Plant):
    """Represents a flowering plant."""

    def __init__(self, name: str, height: int, age: int, color: str):
        """Initialize a flower.
        
        Args:
            name: Plant name
            height: Height in centimeters
            age: Age in days
            color: Flower color
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display bloom message."""
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    """Represents a tree plant."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int):
        """Initialize a tree.
        
        Args:
            name: Plant name
            height: Height in centimeters
            age: Age in days
            trunk_diameter: Trunk diameter in centimeters
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Display shade information for the tree."""
        print(f"{self.name.capitalize()} provides {self.trunk_diameter} "
              f"square meters of shade")


class Vegetable(Plant):
    """Represents a vegetable plant."""

    def __init__(self, name: str, height: int, age: int,
                 season: str, val: str):
        """Initialize a vegetable.
        
        Args:
            name: Plant name
            height: Height in centimeters
            age: Age in days
            season: Harvest season
            val: Nutritional value
        """
        super().__init__(name, height, age)
        self.val = val
        self.season = season


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("")
    plants = [Flower("rose", 25, 30, "red"),
              Tree("oak", 500, 1825, 50),
              Vegetable("tomato", 80, 90, "summer", "vitamin C")]
    for i in range(len(plants)):
        plants[i].get_info()
        print("")
