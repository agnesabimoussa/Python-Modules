import random
from typing import List
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> dict:

        cards_played = []
        mana_used = 0
        damage = 0

        # play cheapest cards first
        hand_sorted = sorted(hand, key=lambda c: c.cost)

        for card in hand_sorted:
            if card.cost <= 3:   # aggressive -> low cost first
                cards_played.append(card.name)
                mana_used += card.cost
                damage += random.randint(2, 5)

        targets = self.prioritize_targets(["Enemy Player", "Enemy Creature"])

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        # aggressive -> attack player first
        if "Enemy Player" in available_targets:
            return ["Enemy Player"]
        return available_targets
