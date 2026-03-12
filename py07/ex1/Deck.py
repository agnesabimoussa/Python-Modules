from ex0.Card import Card, CardType
from random import shuffle


class Deck:
    """
    This class manages creatures, spells and artifacts polymorphically
    """

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        try:
            self.cards.remove(card_name)
        except ValueError:
            print(f"{card_name} is not in the cards")

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            return None
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        creatures = len([
            card for card in self.cards if card.type == CardType.CREATURE])
        spells = len([
            card for card in self.cards if card.type == CardType.SPELL])
        artifacts = len([
            card for card in self.cards if card.type == CardType.ARTIFACT])
        sum = 0
        for card in self.cards:
            sum += card.cost
        avg_cost = sum / len(self.cards)
        stats = {"total_cards": len(self.cards),
                 "creatures": creatures,
                 "spells": spells,
                 "artifacts": artifacts,
                 "avg_cost": round(avg_cost, 2)}
        return stats
