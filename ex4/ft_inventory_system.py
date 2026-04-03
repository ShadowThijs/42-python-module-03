"""Inventory system.

Parse command-line item:quantity pairs into a dictionary and analyze.
"""

import sys

print("=== Inventory System Analysis ===")
inventory: dict[str, int] = {}

for arg in sys.argv[1:]:
    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        continue
    parts: list[str] = arg.split(":", 1)
    item: str = parts[0]
    qty_str: str = parts[1]
    if (item in inventory):
        print(f"Redundant item '{item}' - discarding")
        continue
    try:
        qty: int = int(qty_str)
        inventory[item] = qty
    except ValueError as e:
        print(f"Quantity error for '{item}': {e}")

print(f"Got inventory: {inventory}")
items: list[str] = list(inventory.keys())
print(f"Item list: {items}")
total_qty: int = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total_qty}")

for item, qty in inventory.items():
    pct: float = round(qty / total_qty * 100, 1)
    print(f"Item {item} represents {pct}%")

most: str = items[0]
least: str = items[0]
for item in items:
    if (inventory[item] > inventory[most]):
        most = item
    if (inventory[item] < inventory[least]):
        least = item
print(f"Item most abundant: {most} with quantity {inventory[most]}")
print(f"Item least abundant: {least} with quantity {inventory[least]}")

inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")
