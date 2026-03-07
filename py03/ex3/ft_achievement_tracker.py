# sets: unordered, no duplicates, mutable
# union: a or b
# intersection: a and b
# difference: elements in a but not in b
if __name__ == "__main__":
    # sample sets data
    alice = {"first_kill", "level_10",
             "treasure_hunter", "speed_demon"}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter',
               'boss_slayer', 'speed_demon', 'perfectionist'}

    only_alice = alice.difference(bob).difference(charlie)
    only_bob = bob.difference(alice).difference(charlie)
    only_charlie = charlie.difference(alice).difference(bob)
    # all unique achievements
    unique_achievements = alice.union(
        bob).union(charlie)
    # common achivements
    common_achievements = alice.intersection(
        bob).intersection(charlie)
    # achievemnets made by only one player
    rare_achievements = only_alice.union(only_bob).union(only_charlie)
    # common achievements betwen alice and bob
    common = alice.intersection(bob)
    alice_bob = alice.difference(bob)
    bob_alice = bob.difference(alice)

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    print(f"\nCommon to all players: {common_achievements}")
    print(f"Rare achievements (1 player): {rare_achievements}")

    print(f"\nAlice vs Bob common: {common}")
    print(f"Alice unique: {alice_bob}")
    print(f"Bob unique: {bob_alice}")
