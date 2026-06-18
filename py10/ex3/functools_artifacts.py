from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import List, Dict, Callable, Any


def spell_reducer(spells: List[int], operation: str) -> int:
    match operation:
        case "add":
            return reduce(add, spells)
        case "multiply":
            return reduce(mul, spells)
        case "max":
            return reduce(lambda x, y: x if x > y else y, spells)
        case "min":
            return reduce(lambda x, y: x if x < y else y, spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    fire_enchant = partial(base_enchantment, power=50, element="fire")
    ice_enchant = partial(base_enchantment, power=50, element="ice")
    lightning_enchant = partial(
        base_enchantment, power=50, element="lightning")
    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(spell: Any) -> str:
        return f"{spell}"

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage Spell: {spell} damage dealt!"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment Spell: {spell} applied!"

    @cast_spell.register(list)
    def _(spell: list) -> str:
        results: List[str] = [f"Cast #{i+1}: {s}" for i, s in enumerate(spell)]
        return "Multi-Cast Spell:\n   " + "\n   ".join(results)

    return cast_spell


def main() -> None:
    print("=" * 60)
    print("FUNCTOOLS ARTIFACTS DEMONSTRATION")
    print("=" * 60)

    spells = [10, 20, 15, 5]

    print("\n1. SPELL REDUCER (reduce with different operations):")
    print(f"   Spells: {spells}")
    print(f"   Add: {spell_reducer(spells, 'add')}")
    print(f"   Multiply: {spell_reducer(spells, 'multiply')}")
    print(f"   Max: {spell_reducer(spells, 'max')}")
    print(f"   Min: {spell_reducer(spells, 'min')}")

    print("\n2. PARTIAL ENCHANTER (pre-configured enchantments):")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"Cast {element} spell (power: {power}) on {target}"

    enchantments = partial_enchanter(base_enchantment)
    print(f"   {enchantments['fire_enchant'](target='enemy')}")
    print(f"   {enchantments['ice_enchant'](target='dragon')}")
    print(f"   {enchantments['lightning_enchant'](target='tower')}")

    print("\n3. MEMOIZED FIBONACCI (cached computation):")
    print(f"   fib(10) = {memoized_fibonacci(10)}")
    print(f"   fib(15) = {memoized_fibonacci(15)}")
    print(f"   fib(20) = {memoized_fibonacci(20)}")

    print("\n4. SPELL DISPATCHER (singledispatch by type):")
    dispatcher = spell_dispatcher()
    print(f"   {dispatcher(75)}")
    print(f"   {dispatcher('Fireball')}")
    print(f"   {dispatcher(['Shield', 'Heal', 'Buff'])}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
