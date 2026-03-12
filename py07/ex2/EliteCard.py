from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Magical, Combatable):
    """
    Multiple inheritance class
    """

    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.damage = 0

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target: dict) -> dict:
        try:
            res = {"attacker": self.name,
                   "target": target["name"],
                   "damage": target["damage"],
                   "combat_type": target["combat_type"]}
            self.damage = target["damage"]
            return res
        except KeyError:
            return None

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        res = {"cater": self.name,
               "spell": spell_name,
               "targets": targets,
               "mana_used": self.cost}
        return res

    def defend(self, incoming_damage: int) -> dict:
        self.damage = self.damage - incoming_damage
        res = {"defender": self.name,
               "damage taken": incoming_damage,
               "damage_blocked": self.damage,
               "still_alive": True if self.damage >= 0 else False
               }
        return res
