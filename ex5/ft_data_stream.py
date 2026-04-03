"""Data stream.

Generate and consume game event streams using generators.
"""

import random
from typing import Generator

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run", "jump", "eat", "sleep", "move",
    "grab", "climb", "swim", "release", "use",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Endlessly yield random (player, action) tuples."""
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    """Yield random events from the list, removing each one, until empty."""
    while (len(events) > 0):
        idx: int = random.randint(0, len(events) - 1)
        event: tuple[str, str] = events[idx]
        events.pop(idx)
        yield event


print("=== Game Data Stream Processor ===")
stream: Generator[tuple[str, str], None, None] = gen_event()
for i in range(1000):
    name, action = next(stream)
    print(f"Event {i}: Player {name} did action {action}")

stream2: Generator[tuple[str, str], None, None] = gen_event()
event_list: list[tuple[str, str]] = [next(stream2) for _ in range(10)]
print(f"Built list of 10 events: {event_list}")

for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")
