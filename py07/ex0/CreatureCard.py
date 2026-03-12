from ex0.Card import Card, CardType


class CreatureCard(Card):
    """
    Concrete class that inherits from Card
    """

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int):
            raise TypeError("attack must be an integer")
        if attack <= 0:
            raise ValueError("attack must be a positive integer")
        self.attack = attack
        if not isinstance(health, int):
            raise TypeError("health must be an integer")
        if health <= 0:
            raise ValueError("health must be a positive integer")
        self.health = health
        self.type = CardType.CREATURE

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: dict) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": self.type.value,
                "attack": self.attack,
                "health": self.health}
