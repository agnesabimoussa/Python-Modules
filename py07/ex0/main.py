from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    creature_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    print(f"{creature_card.get_card_info()}\n")
    print(f"Playing {creature_card.name} with 6 mana available:")
    print(f"Playable: {creature_card.is_playable(6)}")
    print(creature_card.play({"mana": 6}))
    print(f"{creature_card.name} attacks Goblin Warrior:")
    print(creature_card.attack_target("Goblin Warrior"))
    print("Testing insufficient mana (3 available):")
    print(f"Playable: {creature_card.is_playable(3)}\n")
    print("Abstract pattern successfully demonstrated!")
