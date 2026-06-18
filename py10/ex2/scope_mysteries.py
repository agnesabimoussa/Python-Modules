from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power: int = initial_power

    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enhancer(enhancement_name: str) -> str:
        return f"{enchantment_type} {enhancement_name}"
    return enhancer


def memory_vault() -> Dict[str, Callable]:
    memories: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        nonlocal memories
        memories[key] = value

    def recall(key: str) -> Any:
        nonlocal memories
        return memories.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("=" * 60)
    print("SCOPE MYSTERIES DEMONSTRATION")
    print("=" * 60)

    print("\n1. MAGE COUNTER (closure counting):")
    counter = mage_counter()
    print(f"   Call 1: {counter()}")
    print(f"   Call 2: {counter()}")
    print(f"   Call 3: {counter()}")

    print("\n2. SPELL ACCUMULATOR (power accumulation):")
    accumulator = spell_accumulator(100)
    print("   Starting power: 100")
    print(f"   Add 25: {accumulator(25)}")
    print(f"   Add 50: {accumulator(50)}")
    print(f"   Add 10: {accumulator(10)}")

    print("\n3. ENCHANTMENT FACTORY (creating enchantments):")
    flaming = enchantment_factory("Flaming")
    icy = enchantment_factory("Icy")
    print(f"   {flaming('Sword')}")
    print(f"   {icy('Arrow')}")
    print(f"   {flaming('Shield')}")

    print("\n4. MEMORY VAULT (private memory storage):")
    vault = memory_vault()
    vault['store']('spell', 'Fireball')
    vault['store']('mage', 'Gandalf')
    vault['store']('level', 99)
    print(f"   Recall 'spell': {vault['recall']('spell')}")
    print(f"   Recall 'mage': {vault['recall']('mage')}")
    print(f"   Recall 'level': {vault['recall']('level')}")
    print(f"   Recall 'unknown': {vault['recall']('unknown')}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
