from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    creature_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("\n=== DataDeck Card Foundation ===\n")
    print("\nTesting Abstract Base Class Design:\n")
    print(f"CreatureCard Info:\n{creature_card.get_card_info()}\n")
    print(f"Playing {creature_card.name} with 6 mana available:")
    print(f"Playable: {creature_card.is_playable(6)}")
    print(f"Play result: {creature_card.play({'available_mana': 6})}")
    print(f"{creature_card.name} attacks Goblin Warrior:")
    print(f"Attack result: {creature_card.attack_target('Goblin Warrior')}")
    print("Testing insufficient mana (3 available):")
    print(f"Playable: {creature_card.is_playable(3)}")
    print("Abstract pattern successfully demonstrated!")
