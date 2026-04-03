"""Score analytics.

Process game scores from command-line arguments and display statistics.
"""

import sys

print("=== Player Score Analytics ===")
scores: list[int] = []
for arg in sys.argv[1:]:
    try:
        scores.append(int(arg))
    except ValueError:
        print(f"Invalid parameter: '{arg}'")

if (len(scores) == 0):
    part1: str = "No scores provided. Usage: python3 "
    part2: str = "ft_score_analytics.py <score1> <score2> ..."
    print(part1 + part2)
else:
    total: int = sum(scores)
    average: float = total / len(scores)
    high: int = max(scores)
    low: int = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")
