from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 rating: int,
                 wins: int = 0,
                 losses: int = 0):
        Card.__init__(self, name, cost, rarity)
        Rankable.__init__(self, wins, losses)
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters battlefield"
        }

    def attack(self, target: dict) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.cost
        }

    def defend(self, incoming_damage: int) -> dict:

        blocked = 1
        damage_taken = max(0, incoming_damage - blocked)

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked
        }

    # def get_combat_stats(self) -> dict:
    #     pass

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating()
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating()
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.cost,
            "defense": 1
        }
