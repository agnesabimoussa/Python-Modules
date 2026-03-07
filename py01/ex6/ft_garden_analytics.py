# Plant -> FloweringPlant -> PrizeFlower
class Plant:
    """Base plant class that stores information about plants."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant.
        
        Args:
            name: Plant name
            height: Height in centimeters
        """
        self.name = name.capitalize()
        self.height = height

    def get_info(self) -> None:
        """Display plant name and height."""
        print(f"{self.name}: {self.height}cm")

    def grow(self) -> None:
        """Increase plant height by 1 centimeter."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """Plant that can flower with a color and blooming status."""

    def __init__(self, name: str, height: int, color: str,
                 is_blooming: bool) -> None:
        """Initialize a flowering plant.
        
        Args:
            name: Plant name
            height: Height in centimeters
            color: Flower color
            is_blooming: Blooming status
        """
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming

    def bloom(self) -> None:
        """Set blooming status to true."""
        self.is_blooming = True

    def wilt(self) -> None:
        """Set blooming status to false."""
        self.is_blooming = False

    def get_info(self) -> None:
        """Display plant information with blooming status."""
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        print(f"{self.name}: {self.height}cm, {self.color} flowers "
              f"({bloom_status})")


class PrizeFlower(FloweringPlant):
    """A flowering plant with prize points."""

    def __init__(self, name: str, height: int, color: str,
                 is_blooming: bool, prize_points: int) -> None:
        """Initialize a prize flower.
        
        Args:
            name: Plant name
            height: Height in centimeters
            color: Flower color
            is_blooming: Blooming status
            prize_points: Prize points value
        """
        super().__init__(name, height, color, is_blooming)
        self.prize_points = prize_points

    def get_info(self) -> None:
        """Display plant information with prize points."""
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        print(f"{self.name}: {self.height}cm, {self.color} flowers "
              f"({bloom_status}), Prize points: {self.prize_points}")


# GardenManager class
# helper: GardenStats
# method: create_garden_network()
class GardenManager:
    """Manages a collection of plants."""

    def __init__(self, manager_name: str) -> None:
        """Initialize the garden manager.
        
        Args:
            manager_name: Manager name
        """
        self.manager_name = manager_name.capitalize()
        self.plants = []

    def create_garden_network(self, plants: list) -> None:
        """Add plants to the garden.
        
        Args:
            plants: List of plant objects
        """
        self.plants.extend(plants)
        for plant in plants:
            print(f"Added {plant.name} to {self.manager_name}'s garden")

    def grow_plants(self) -> None:
        """Grow all plants by 1 centimeter."""
        print(f"{self.manager_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def get_report(self) -> None:
        """Generate and display a garden report."""
        print(f"=== {self.manager_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()
        stats = self.GardenStats
        print(f"\nPlants added: {stats.total_plants(self.plants)}")
        print(f"Total growth: {stats.total_growth(self.plants)}cm")
        type_counts = stats.count_by_type(self.plants)
        print(f"Plant types: {type_counts['Plant']} regular, "
              f"{type_counts['FloweringPlant']} flowering, "
              f"{type_counts['PrizeFlower']} prize flowers")
        print(f"Height validation test: "
              f"{stats.validate_heights(self.plants)}")

    class GardenStats:
        """Helper class for garden statistics."""

        @staticmethod
        def total_plants(plants: list) -> int:
            """Count total plants.
            
            Args:
                plants: List of plants
                
            Returns:
                Number of plants
            """
            return len(plants)

        @staticmethod
        def average_height(plants: list) -> float:
            """Calculate average plant height.
            
            Args:
                plants: List of plants
                
            Returns:
                Average height or 0 if empty
            """
            if not plants:
                return 0
            total = sum(p.height for p in plants)
            return total / len(plants)

        @staticmethod
        def total_growth(plants: list) -> int:
            """Calculate total height of all plants.
            
            Args:
                plants: List of plants
                
            Returns:
                Sum of all plant heights
            """
            return sum(p.height for p in plants)

        @staticmethod
        def count_by_type(plants: list) -> dict:
            """Count plants by type.
            
            Args:
                plants: List of plants
                
            Returns:
                Dictionary with plant type counts
            """
            regular = flowering = prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return {"Plant": regular, "FloweringPlant": flowering,
                    "PrizeFlower": prize}

        @staticmethod
        def blooming_count(plants: list) -> int:
            """Count blooming plants.
            
            Args:
                plants: List of plants
                
            Returns:
                Number of blooming plants
            """
            count = 0
            for plant in plants:
                if isinstance(plant, (FloweringPlant, PrizeFlower)) and \
                        plant.is_blooming:
                    count += 1
            return count

        @staticmethod
        def total_prize_points(plants: list) -> int:
            """Sum prize points from all plants.
            
            Args:
                plants: List of plants
                
            Returns:
                Total prize points
            """
            return sum(p.prize_points for p in plants
                       if isinstance(p, PrizeFlower))

        @staticmethod
        def tallest_plant(plants: list) -> Plant:
            """Find the tallest plant.
            
            Args:
                plants: List of plants
                
            Returns:
                Tallest plant or None if empty
            """
            if not plants:
                return None
            return max(plants, key=lambda p: p.height)

        @staticmethod
        def validate_heights(plants: list) -> bool:
            """Validate all plant heights are non-negative.
            
            Args:
                plants: List of plants
                
            Returns:
                True if all heights are non-negative
            """
            return all(p.height >= 0 for p in plants)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager("alice")
    plants = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red", True),
        PrizeFlower("Sunflower", 50, "yellow", True, 10)
    ]
    manager.create_garden_network(plants)
    print()
    manager.grow_plants()
    print()
    manager.get_report()
