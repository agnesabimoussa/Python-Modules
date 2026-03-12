from ex0.Card import Card, CardType


class SpellCard(Card):
    def __init__(self, name, cost, rarity, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = CardType.SPELL

    def play(self, game_state: dict) -> dict:
        res = {}
        type = self.effect_type
        if self.effect_type == 'damage':
            type = f'Deal {self.cost} damage to target'
        if game_state['mana'] >= self.cost:
            res = {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': type
            }
        return res

    def resolve_effect(self, targets: list) -> dict:
        ...
