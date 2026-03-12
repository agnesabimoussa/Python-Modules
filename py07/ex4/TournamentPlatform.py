import random

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self._name_counts = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        base = self._normalize_base(card.name)
        count = self._name_counts.get(base, 0) + 1
        self._name_counts[base] = count
        card_id = f"{base}_{count:03d}"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        try:
            card1 = self.cards[card1_id]
            card2 = self.cards[card2_id]
        except KeyError:
            return {"error": "invalid card id"}

        if card1.calculate_rating() > card2.calculate_rating():
            winner_id, loser_id = card1_id, card2_id
        elif card2.calculate_rating() > card1.calculate_rating():
            winner_id, loser_id = card2_id, card1_id
        else:
            winner_id, loser_id = random.choice(
                [(card1_id, card2_id), (card2_id, card1_id)]
            )

        winner = self.cards[winner_id]
        loser = self.cards[loser_id]

        winner.update_wins(1)
        loser.update_losses(1)

        rating_delta = 16
        winner.rating += rating_delta
        loser.rating -= rating_delta

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        ordered = sorted(
            self.cards.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True
        )
        return [
            {
                "id": card_id,
                "name": card.name,
                "rating": card.calculate_rating(),
                "wins": card.wins,
                "losses": card.losses
            }
            for card_id, card in ordered
        ]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        avg_rating = 0
        if total_cards:
            avg_rating = int(
                round(
                    sum(card.calculate_rating()
                        for card in self.cards.values()) / total_cards
                )
            )
        status = "active" if total_cards else "inactive"
        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": status
        }

    def _normalize_base(self, name: str) -> str:
        parts = name.strip().split()
        base = parts[-1] if parts else "card"
        cleaned = "".join(ch for ch in base.lower() if ch.isalnum())
        return cleaned or "card"
