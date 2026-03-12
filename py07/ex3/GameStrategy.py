from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """
    Abstract strategy interface
    """

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a full turn using the given hand and battlefield state.

        Should decide which cards to play, which targets to attack, and return
        a structured dict describing actions taken (cards played, damage, etc.).
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return a human-readable name for this strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Order or filter targets based on the strategy's priorities."""
        pass
