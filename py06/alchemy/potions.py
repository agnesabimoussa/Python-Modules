import alchemy.elements as utils


def healing_potion() -> str:
    return (
        f"Healing potion brewed with {utils.create_fire()} "
        f"and {utils.create_water()}"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with {utils.create_earth()} "
        f"and {utils.create_fire()}"
    )


def invisibility_potion() -> str:
    return (
        f"Invisibility potion brewed with {utils.create_air()} "
        f"and {utils.create_water()}"
    )


def wisdom_potion() -> str:
    return (
        f"Wisdom potion brewed with all elements: "
        f"{utils.create_fire()}, {utils.create_earth()}, "
        f"{utils.create_air()}, {utils.create_water()}"
    )
