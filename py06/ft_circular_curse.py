import alchemy.grimoire

if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print("validate_ingredients(\"fire air\"): ", end="")
    print(alchemy.grimoire.validate_ingredients("fire air"))
    print("validate_ingredients(\"dragon scales\"): ", end="")
    print(alchemy.grimoire.validate_ingredients("dragon scales"))

    print("\nTesting spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"): ", end="")
    print(alchemy.grimoire.record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\"): ", end="")
    print(alchemy.grimoire.record_spell("Dark Magic", "shadow"))

    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"): ", end="")
    print(alchemy.grimoire.record_spell("Lightening", "air"))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
