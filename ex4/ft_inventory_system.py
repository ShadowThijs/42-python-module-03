def print_inventory(inventory):
    """Calculates and prints inventory details."""
    total_value = 0
    total_items = 0
    categories = {}

    for name, details in inventory.items():
        price = details.get("price", 0)
        amount = details.get("amount", 0)
        type_ = details.get("type", "unknown")
        rarity = details.get("rarity", "common")

        item_total = price * amount
        total_value += item_total
        total_items += amount

        print(f"{name} ({type_}, {rarity}): "
              f"{amount}x @ {price} gold each = {item_total} gold")

        current_cat_count = categories.get(type_, 0)
        categories[type_] = current_cat_count + amount

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    cat_parts = []
    for cat, count in categories.items():
        cat_parts.append(f"{cat}({count})")

    print(f"Categories: {', '.join(cat_parts)}")


def transfer_item(source, target, item_name, amount):
    """Transfers items from source inventory to target inventory."""
    if item_name in source:
        source_item = source[item_name]
        if source_item["amount"] >= amount:
            source_item["amount"] -= amount

            if item_name not in target:
                target[item_name] = {
                    "price": source_item["price"],
                    "type": source_item["type"],
                    "rarity": source_item["rarity"],
                    "amount": 0
                }

            target[item_name]["amount"] += amount
            print("Transaction successful!")
            return

    print("Transaction failed: Not enough items or item not found.")


def main():
    print("=== Player Inventory System ===")

    alice_inventory = {
        "sword": {"price": 500, "amount": 1,
                  "type": "weapon", "rarity": "rare"},
        "potion": {"price": 50, "amount": 5,
                   "type": "consumable", "rarity": "common"},
        "shield": {"price": 200, "amount": 1,
                   "type": "armor", "rarity": "uncommon"}
    }

    bob_inventory = {
        "magic_ring": {"price": 100, "amount": 1,
                       "type": "accessory", "rarity": "rare"}
    }

    print("=== Alice's Inventory ===")
    print_inventory(alice_inventory)

    print("=== Transaction: Alice gives Bob 2 potions ===")
    transfer_item(alice_inventory, bob_inventory, "potion", 2)

    print("=== Updated Inventories ===")
    alice_potions = alice_inventory.get("potion", {}).get("amount", 0)
    bob_potions = bob_inventory.get("potion", {}).get("amount", 0)
    print(f"Alice potions: {alice_potions}")
    print(f"Bob potions: {bob_potions}")

    print("=== Inventory Analytics ===")

    players = {"Alice": alice_inventory, "Bob": bob_inventory}

    max_value = -1
    max_value_player = ""

    max_items = -1
    max_items_player = ""

    rarest_items = []

    for player_name, inv in players.items():
        p_val = 0
        p_items = 0

        for name, details in inv.items():
            amt = details["amount"]
            p_val += details["price"] * amt
            p_items += amt

            if details["rarity"] == "rare":
                rarest_items.append(name)

        if p_val > max_value:
            max_value = p_val
            max_value_player = player_name

        if p_items > max_items:
            max_items = p_items
            max_items_player = player_name

    rarest_items_unique = []
    for item in rarest_items:
        if item not in rarest_items_unique:
            rarest_items_unique.append(item)

    print(f"Most valuable player: {max_value_player} ({max_value} gold)")
    print(f"Most items: {max_items_player} ({max_items} items)")
    print(f"Rarest items: {', '.join(rarest_items_unique)}")


main()
