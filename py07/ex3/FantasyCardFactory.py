import random
from enum import Enum
from typing import Dict
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class CardType(Enum):
    CREATURE = "creature"
    SPELL = "spell"
    ARTIFACT = "artifact"


class FantasyCardFactory(CardFactory):

    creature_pool = [
        ("Fire Dragon", 5, 7, 5),
        ("Goblin Warrior", 2, 3, 2),
        ("Stone Golem", 4, 4, 6),
    ]

    spell_pool = [
        ("Fireball", 3, "damage"),
        ("Healing Light", 2, "heal"),
        ("Lightning Bolt", 3, "damage"),
    ]

    artifact_pool = [
        ("Mana Ring", 2, 5, "+1 mana per turn"),
        ("Ancient Staff", 3, 4, "spell boost"),
    ]

    def create_creature(self, name_or_power=None):

        name, cost, attack, health = random.choice(self.creature_pool)

        return CreatureCard(
            name=name,
            cost=cost,
            rarity="Common",
            attack=attack,
            health=health
        )

    def create_spell(self, name_or_power=None):

        name, cost, effect = random.choice(self.spell_pool)

        return SpellCard(
            name=name,
            cost=cost,
            rarity="Rare",
            effect_type=effect
        )

    def create_artifact(self, name_or_power=None):

        name, cost, durability, effect = random.choice(self.artifact_pool)

        return ArtifactCard(
            name=name,
            cost=cost,
            rarity="Epic",
            durability=durability,
            effect=effect
        )

    def create_themed_deck(self, size: int) -> Dict:

        deck = []
        created = 0

        while created < size:

            choice = random.choice(list(CardType))

            if choice == CardType.CREATURE:
                deck.append(self.create_creature())

            elif choice == CardType.SPELL:
                deck.append(self.create_spell())

            else:
                deck.append(self.create_artifact())

            created += 1

        return {
            "deck_size": size,
            "cards": deck
        }

    def get_supported_types(self) -> dict:

        return {
            "creatures": ["dragon", "goblin", "golem"],
            "spells": ["fireball", "heal", "lightning"],
            "artifacts": ["mana_ring", "staff"]
        }
