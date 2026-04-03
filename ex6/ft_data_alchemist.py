"""Data alchemist.

Transform and filter game data using list and dict comprehensions.
"""

import random

players: list[str] = [
    "Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john", "kevin", "Liam"
]

capitalized_all: list[str] = [name.capitalize() for name in players]
capitalized_only: list[str] = [name for name in players if name == name.capitalize()]

scores: dict[str, int] = {name: random.randint(1, 1000) for name in capitalized_all}
avg: float = round(sum(scores.values()) / len(scores), 2)
high_scores: dict[str, int] = {
    name: score for name, score in scores.items() if score > avg
}

print("=== Game Data Alchemist ===")
print(f"Initial list of players: {players}")
print(f"New list with all names capitalized: {capitalized_all}")
print(f"New list of capitalized names only: {capitalized_only}")
print(f"Score dict: {scores}")
print(f"Score average is {avg}")
print(f"High scores: {high_scores}")
