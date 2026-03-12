from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def _format_record(card: TournamentCard) -> str:
    return f"{card.wins}-{card.losses}"


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 1150)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.calculate_rating()}")
    print(f"- Record: {_format_record(dragon)}")

    print(f"{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.calculate_rating()}")
    print(f"- Record: {_format_record(wizard)}")

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for index, entry in enumerate(leaderboard, start=1):
        print(
            f"{index}. {entry['name']} - Rating: {entry['rating']} "
            f"({entry['wins']}-{entry['losses']})"
        )

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print("=== Tournament Platform Successfully Deployed! ===")
