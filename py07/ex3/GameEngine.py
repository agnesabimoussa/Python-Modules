from typing import List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):

        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None

        self.hand: List = []
        self.battlefield: List = []

        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:

        self.factory = factory
        self.strategy = strategy

        deck = factory.create_themed_deck(3)

        self.hand = deck["cards"]
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:

        if not self.factory or not self.strategy:
            raise ValueError("Engine not configured")

        result = self.strategy.execute_turn(self.hand, self.battlefield)

        self.turns_simulated += 1
        self.total_damage += result["damage_dealt"]

        return result

    def get_engine_status(self) -> dict:

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
