from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main():

    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")

    # Display the cards currently in hand
    hand_display = []
    for card in engine.hand:
        hand_display.append(f"{card.name} ({card.cost})")

    print("Hand:", "[" + ", ".join(hand_display) + "]")

    # Execute turn
    result = engine.simulate_turn()

    print("\nTurn execution:")
    print("Strategy:", result["strategy"])

    actions = {
        "cards_played": result["cards_played"],
        "mana_used": result["mana_used"],
        "targets_attacked": result["targets_attacked"],
        "damage_dealt": result["damage_dealt"]
    }

    print("Actions:", actions)

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
