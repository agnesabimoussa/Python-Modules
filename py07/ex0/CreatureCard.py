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
        if attack <= 0:
            raise ValueError("attack must be a positive integer")
        self.attack = attack
        if health <= 0:
            raise ValueError("health must be a positive integer")
        self.health = health
        self.type = CardType.CREATURE.value

    def play(self, game_state: dict) -> dict:
        try:
            res = {}
            if game_state['mana'] >= self.cost:
                res = {
                    'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': f'{self.type} summoned to battlefield'
                }
            return res
        except KeyError:
            print("KeyError: Make sure game_state dict has mana key")

    def attack_target(self, target: dict) -> dict:
        try:
            res = {
                'attacker': self.name,
                'target': target['name'],
                'damage_dealt': self.attack,
            }
            if target['health'] > self.attack:
                res.update({'combat_resolved': False})
            else:
                res.update({'combat_resolved': True})
            return res
        except KeyError:
            print("KeyError: Make sure target dict has name and health keys")

    def get_card_info(self) -> dict:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": self.type,
                "attack": self.attack,
                "health": self.health}
