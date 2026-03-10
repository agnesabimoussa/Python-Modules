def first_method() -> None:
    import alchemy.elements
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire(): ", end="")
    print(alchemy.elements.create_fire())


def second_method() -> None:
    from alchemy.elements import create_water
    print("\nMethod 2 - Specific function import")
    print("create_water(): ", end="")
    print(create_water())


def third_method() -> None:
    from alchemy.potions import healing_potion as heal
    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")


def forth_method() -> None:
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print("\nMethod 4 - Multiple imports:")
    print("create_earth(): ", end="")
    print(create_earth())
    print("create_fire(): ", end="")
    print(create_fire())
    print("strength_potion() :", end="")
    print(strength_potion())


if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===\n")
    first_method()
    second_method()
    third_method()
    forth_method()
    print("All import transmutation methods mastered!")
