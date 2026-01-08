def main():
    print("=== Game Analytics Dashboard ===")

    players = [
        {
            "name": "alice",
            "score": 2300,
            "category": "warrior",
            "achievements": ["first_kill", "level_10"]
        },
        {
            "name": "bob",
            "score": 1800,
            "category": "mage",
            "achievements": ["first_kill", "collector"]
        },
        {
            "name": "charlie",
            "score": 2150,
            "category": "warrior",
            "achievements": ["level_10", "speed_demon"]
        },
        {
            "name": "diana",
            "score": 2050,
            "category": "rogue",
            "achievements": ["first_kill", "level_10", "speed_demon"]
        },
        {
            "name": "eve",
            "score": 900,
            "category": "mage",
            "achievements": []
        }
    ]

    print("=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [p["score"] * 2 for p in players]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [
        f"{p['name'].capitalize()} ({p['score']}pts)"
        for p in players if p['score'] > 1000
    ]
    print(f"Active player summary: {active_players}")

    print("=== Dict Comprehension Examples ===")

    score_map = {p["name"]: p["score"] for p in players}
    print(f"Score mapping: {score_map}")

    category_map = {p["name"]: p["category"].upper() for p in players}
    print(f"Category mapping: {category_map}")

    print("=== Set Comprehension Examples ===")

    unique_categories = {p["category"] for p in players}
    print(f"Unique categories: {unique_categories}")

    unique_achievements = {ach for p in players for ach in p["achievements"]}
    print(f"All unique achievements: {sorted(list(unique_achievements))}")


main()
