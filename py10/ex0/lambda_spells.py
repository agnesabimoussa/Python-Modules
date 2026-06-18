from typing import Dict, List


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    try:
        sorted_list = sorted(
            artifacts, key=lambda artifact: artifact['power'], reverse=True)
        return sorted_list
    except KeyError:
        print("KeyError: the key 'power' does not exist!")


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    try:
        filtered_list = list(filter(lambda m: m["power"] >= min_power, mages))
        return filtered_list
    except KeyError:
        print("KeyError: the key 'power' does not exist!")


def spell_transformer(spells: List[str]) -> List[str]:
    transformed_list = list(map(lambda s: '*' + s + '*', spells))
    return transformed_list


def mage_stats(mages: List[Dict]) -> Dict:
    try:
        max_power = max(mages, key=lambda m: m["power"])["power"]
        min_power = min(mages, key=lambda m: m["power"])["power"]
        avg_power = round(sum(m["power"] for m in mages) / len(mages), 2)
        return {
            "max_power": max_power,
            "min_power": min_power,
            "avg_power": avg_power
        }
    except KeyError:
        print("KeyError: the key 'power' does not exist!")


def main() -> None:
    artifacts = [{'name': 'Shadow Blade', 'power': 69, 'type': 'focus'},
                 {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'}, {
        'name': 'Crystal Orb', 'power': 106, 'type': 'relic'},
        {'name': 'Crystal Orb', 'power': 118, 'type': 'relic'}]
    mages = [{'name': 'Rowan', 'power': 93, 'element': 'shadow'},
             {'name': 'Casey', 'power': 94, 'element': 'earth'},
             {'name': 'Alex', 'power': 60, 'element': 'earth'},
             {'name': 'Morgan', 'power': 93, 'element': 'ice'},
             {'name': 'Storm', 'power': 72, 'element': 'shadow'}]
    spells = ['shield', 'lightning', 'meteor', 'fireball']

    print("=" * 60)
    print("LAMBDA SPELLS DEMONSTRATION")
    print("=" * 60)
    print("\n1. ARTIFACT SORTER (sorted by power descending):")
    sorted_artifacts = artifact_sorter(artifacts)
    if (sorted_artifacts is not None):
        for artifact in sorted_artifacts:
            print(
                f"   {artifact['name']}: {artifact['power']} power"
                f"({artifact['type']})")
    print("\n2. POWER FILTER (mages with power >= 90):")
    strong_mages = power_filter(mages, 90)
    for mage in strong_mages:
        print(f"   {mage['name']}: {mage['power']} power ({mage['element']})")
    print("\n3. SPELL TRANSFORMER (wrapping with asterisks):")
    transformed_spells = spell_transformer(spells)
    print(f"   Original: {spells}")
    print(f"   Transformed: {transformed_spells}")
    print("\n4. MAGE STATS (power analysis):")
    stats = mage_stats(mages)
    print(f"   Max Power: {stats['max_power']}")
    print(f"   Min Power: {stats['min_power']}")
    print(f"   Avg Power: {stats['avg_power']}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
