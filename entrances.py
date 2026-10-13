from __future__ import annotations
from dataclasses import dataclass

from typing import TYPE_CHECKING, Optional

from rule_builder.rules import Has, HasAll, HasAllCounts, Rule
from .data.regions import REGION_DEFS

if TYPE_CHECKING:
    from .world import TTTTWorld

@dataclass
class EntranceData:
    entry: str
    exit: str
    rule: Optional[Rule]

def get_access_rule(world: TTTTWorld, required_items: dict[str, int]) -> Rule:
    requirements = {}
    needs_counts = False
    for item, count in required_items.items():
        if not world.has_item(item):
            continue

        requirements[item] = count
        if count > 1:
            needs_counts = True

    if not requirements:
        return None

    # The performance gain from not using HasAllCounts is practically nonexistent
    # but I'm using it conditionally anyways
    if needs_counts:
        return HasAllCounts(requirements)

    required_items = list(requirements)
    if len(required_items) > 1:
        return HasAll(required_items)

    item = required_items[0]
    return Has(item)

def get_entrance_rules(world: TTTTWorld, name: str):
    data = REGION_DEFS[name]

    parent = data.get("parent", None)
    one_way = data.get("one_way", False)

    if not parent:
        return []

    rule = get_access_rule(world, data.get("required_items", {}))

    entrances = [EntranceData(parent, name, rule)]
    if not one_way:
        entrances.append(EntranceData(name, parent, rule))
    return entrances

def get_all_entrances(world: TTTTWorld):
    entrance_rules: list[EntranceData] = []
    for key in REGION_DEFS:
        entrance_rules += get_entrance_rules(world, key)

    return entrance_rules
