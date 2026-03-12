from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(ArtifactCard("Ancient Relic", 2, "Epic", 4, "shield"))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", "damage"))
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")

    for i in range(0, 3):
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.type.value})")
        print(f"Play result: {card.play({'mana': 4})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")
