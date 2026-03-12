from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    Abstract interface
    """

    @abstractmethod
    def attack(self, target: dict) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass
