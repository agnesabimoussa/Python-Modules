from ex2.EliteCard import EliteCard

if __name__ == "__main__":
    elite_card = EliteCard("Arcane Warrior", 65, "Elite")
    target = {"name": "Enemy", "damage": 5, "combat_type": "melee"}
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    print(f"Playing {elite_card.name} (Elite Card):\n")

    print("Combat phase:")
    print(f"Attack result: {elite_card.attack(target)}")
    print(f"Defense result: {elite_card.defend(2)}")

    print("Magic phase:")
    print(
        f"Spell cast:{elite_card.cast_spell("Fireball",
                                            ['Enemy1', 'Enemy2'])}\n")
    
    print("Multiple interface implementation successful!")
