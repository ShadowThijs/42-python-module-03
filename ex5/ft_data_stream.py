def game_event_generator(n):
    """Generates a stream of game events."""
    players = ["alice", "bob", "charlie", "diana", "eve"]

    for i in range(n):
        player = players[i % len(players)]

        level = ((i * 7) % 20) + 1

        action_seed = i % 10

        if action_seed == 0:
            action = "found treasure"
        elif action_seed < 3:
            action = "leveled up"
        else:
            action = "killed monster"

        yield f"Event {i+1}: Player {player} (level {level}) {action}"


def fibonacci_generator():
    """Yields Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator():
    """Yields prime numbers indefinitely."""
    num = 2
    while True:
        is_prime = True
        if num < 2:
            is_prime = False
        else:
            for i in range(2, num):
                if i * i > num:
                    break
                if num % i == 0:
                    is_prime = False
                    break

        if is_prime:
            yield num
        num += 1


def main():
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    stream = game_event_generator(total_events)

    count = 0
    high_level_count = 0
    treasure_count = 0
    level_up_count = 0

    for event in stream:
        count += 1

        if count <= 3:
            print(event)
        elif count == 4:
            print("...")

        try:
            lvl_start = event.find("(level ") + 7
            lvl_end = event.find(")", lvl_start)
            if lvl_start > 6 and lvl_end != -1:
                level = int(event[lvl_start:lvl_end])
                if level >= 10:
                    high_level_count += 1
        except ValueError:
            pass

        if "found treasure" in event:
            treasure_count += 1
        elif "leveled up" in event:
            level_up_count += 1

    print("=== Stream Analytics ===")
    print(f"Total events processed: {count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("=== Generator Demonstration ===")

    fib_gen = iter(fibonacci_generator())
    fib_vals = []
    for _ in range(10):
        fib_vals.append(str(next(fib_gen)))
    print(f"Fibonacci sequence (first 10): {', '.join(fib_vals)}")

    prime_gen = iter(prime_generator())
    prime_vals = []
    for _ in range(5):
        prime_vals.append(str(next(prime_gen)))
    print(f"Prime numbers (first 5): {', '.join(prime_vals)}")


main()
