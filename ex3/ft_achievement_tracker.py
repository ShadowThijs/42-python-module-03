"""Achievement tracker.

Track and compare player achievements using sets.
"""

import random

ALL_ACHIEVEMENTS: list[str] = [
    "First Steps", "Boss Slayer", "Speed Runner", "Collector Supreme",
    "Master Explorer", "World Savior", "Untouchable", "Unstoppable",
    "Crafting Genius", "Strategist", "Treasure Hunter", "Survivor",
    "Sharp Mind", "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    """Randomly generate a set of achievements for a player."""
    count: int = random.randint(4, 10)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


print("=== Achievement Tracker System ===")
players: dict[str, set[str]] = {
    "Alice": gen_player_achievements(),
    "Bob": gen_player_achievements(),
    "Charlie": gen_player_achievements(),
    "Dylan": gen_player_achievements(),
}

for name, achievements in players.items():
    print(f"Player {name}: {achievements}")

all_achievements: set[str] = set.union(*players.values())
common: set[str] = set.intersection(*players.values())
print(f"All distinct achievements: {all_achievements}")
print(f"Common achievements: {common}")

for name, achievements in players.items():
    others: set[str] = set.union(
        *[a for n, a in players.items() if n != name]
    )
    unique: set[str] = set.difference(achievements, others)
    missing: set[str] = set.difference(all_achievements, achievements)
    print(f"Only {name} has: {unique}")

for name, achievements in players.items():
    missing = set.difference(all_achievements, achievements)
    print(f"{name} is missing: {missing}")
