def main():
    print("=== Achievement Tracker System ===")

    alice_achievements = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
    }
    bob_achievements = {
        'first_kill', 'level_10', 'boss_slayer', 'collector'
    }
    charlie_achievements = {
        'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
        'perfectionist'
    }

    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")

    print("=== Achievement Analytics ===")

    all_achievements = alice_achievements.union(
        bob_achievements, charlie_achievements
    )
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all = alice_achievements.intersection(
        bob_achievements, charlie_achievements
    )
    print(f"Common to all players: {common_all}")

    alice_only = alice_achievements.difference(
        bob_achievements, charlie_achievements
    )
    bob_only = bob_achievements.difference(
        alice_achievements, charlie_achievements
    )
    charlie_only = charlie_achievements.difference(
        alice_achievements, bob_achievements
    )

    rare_achievements = alice_only.union(bob_only, charlie_only)
    print(f"Rare achievements (1 player): {rare_achievements}")

    alice_bob_common = alice_achievements.intersection(bob_achievements)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_vs_bob_unique = alice_achievements.difference(bob_achievements)
    print(f"Alice unique: {alice_vs_bob_unique}")

    bob_vs_alice_unique = bob_achievements.difference(alice_achievements)
    print(f"Bob unique: {bob_vs_alice_unique}")


main()
