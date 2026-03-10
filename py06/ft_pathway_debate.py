import alchemy.transmutation.basic as basic
import alchemy.transmutation.advanced as advanced
import alchemy.transmutation


if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold(): ", end="")
    print(basic.lead_to_gold())
    print("stone_to_gem(): ", end="")
    print(basic.stone_to_gem())

    print("\nTesting Relative Imports (from advanced.py):")
    print("philosophers_stone(): ", end="")
    print(advanced.philosophers_stone())
    print("elixir_of_life(): ", end="")
    print(advanced.elixir_of_life())

    print("\nTesting Package Access")
    print("alchemy.transmutation.lead_to_gold(): ", end="")
    print(alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone(): ", end="")
    print(alchemy.transmutation.philosophers_stone())

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
