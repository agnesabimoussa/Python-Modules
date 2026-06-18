from typing import List, Tuple, Any, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined() -> Tuple[Any, Any]:
        t = (spell1(), spell2())
        return tuple(t)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier() -> int:
        res: int = base_spell() * multiplier
        return res
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: List[Callable]) -> Callable:
    def cast_all(*args, **kwargs) -> List[Any]:
        results = [spell(*args, **kwargs) for spell in spells]
        return results
    return cast_all


def main() -> None:
    print("=" * 60)
    print("HIGHER MAGIC DEMONSTRATION")
    print("=" * 60)

    def base_power() -> int: return 10
    def double_power() -> int: return 5
    def fireball(target: str) -> str: return f"Fireball cast on {target}!"
    def strong_condition(val: int) -> bool: return val > 10

    print("\n1. SPELL COMBINER (combining two spells):")
    combined = spell_combiner(base_power, double_power)
    result = combined()
    print(f"   Combined output: {result}")

    print("\n2. POWER AMPLIFIER (amplifying base power by 3x):")
    amplified = power_amplifier(base_power, 3)
    result = amplified()
    print(f"   Amplified power: {result}")

    print("\n3. CONDITIONAL CASTER (spell casts if value > 10):")
    strong_caster = conditional_caster(strong_condition, fireball)
    print(f"   Value 18 (>10): {strong_caster(18)}")
    print(f"   Value 7 (>10): {strong_caster(7)}")

    print("\n4. SPELL SEQUENCE (casting multiple spells):")
    sequence = spell_sequence([base_power, double_power, lambda: 15])
    results = sequence()
    print(f"   Sequence results: {results}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
