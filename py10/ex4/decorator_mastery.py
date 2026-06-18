from functools import wraps
from typing import Callable, Any
from time import perf_counter


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time: float = perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = perf_counter()
        print(f"Spell completed in {end_time - start_time} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power_value: Any = args[2] if len(args) > 2 else (
                args[0] if args else None)
            if power_value is not None and power_value < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... (attempt {attempt}"
                            f"/{max_attempts})")
                    else:
                        return f"Spell casting failed after {max_attempts}"
                    "attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for c in name:
            if not c.isspace() and not c.isalpha():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("=" * 60)
    print("DECORATOR MASTERY DEMONSTRATION")
    print("=" * 60)

    print("\n1. SPELL TIMER (measures execution time):")

    @spell_timer
    def ancient_spell():
        import time
        time.sleep(0.1)
        return "Spell executed"
    result = ancient_spell()
    print(f"   Result: {result}")

    print("\n2. POWER VALIDATOR (checks power threshold):")

    @power_validator(min_power=50)
    def fireball(power: int):
        return f"Fireball cast with {power} power"
    print(f"   Power 30 (< 50): {fireball(30)}")
    print(f"   Power 75 (>= 50): {fireball(75)}")

    print("\n3. RETRY SPELL (retries on failure):")
    attempt_count = [0]

    @retry_spell(max_attempts=3)
    def unstable_spell():
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise Exception("Spell fizzled!")
        return "Spell finally cast successfully!"
    print(f"   Result: {unstable_spell()}")

    print("\n4. VALIDATE MAGE NAME (static method validation):")
    guild = MageGuild()
    print(f"   'Alice': {guild.validate_mage_name('Alice')}")
    print(f"   'Bob Smith': {guild.validate_mage_name('Bob Smith')}")
    print(f"   'X1': {guild.validate_mage_name('X1')}")
    print(f"   'Jo': {guild.validate_mage_name('Jo')}")

    print("\n5. CAST SPELL (instance method with power validator):")
    print(f"   Power 5 (< 10): {guild.cast_spell('Lightning', 5)}")
    print(f"   Power 25 (>= 10): {guild.cast_spell('Thunder', 25)}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
