from ex0.Card import Card, CardType


class ArtifactCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = CardType.ARTIFACT

    def play(self, game_state: dict) -> dict:
        res = {}
        type = ""
        if self.effect == 'buff':
            type = f'Deal {self.cost} damage to target'
        if game_state['mana'] >= self.cost:
            res = {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': type
            }
        return res

    def activate_ability(self) -> dict:
        ...
