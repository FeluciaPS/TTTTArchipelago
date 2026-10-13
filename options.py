from __future__ import annotations

from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions
from .option_groups import *

@dataclass
class TTTTOptions(PerGameCommonOptions):
    # Goal Options
    goal: Goal
    turbo_requirement: TurboRequirement

    # Shop Options
    randomize_shop_items: RandomizeShopItems
    randomize_shop_prices: RandomizeShopPrices
    shop_price_multiplier: ShopPriceMultiplier
    shop_item_count: ShopItemCount

    # World Options
    randomize_map: RandomizeMap
    lock_doors: LockDoors

option_groups = [
    OptionGroup(
        "Goal Options",
        [Goal, TurboRequirement]
    ),
    OptionGroup(
        "Shop Options",
        [RandomizeShopItems, RandomizeShopPrices, ShopPriceMultiplier, ShopItemCount],
    ),
    OptionGroup(
        "Silly Options",
        [DutchItemNames],
    ),
    OptionGroup(
        "World Options",
        [RandomizeMap, LockDoors]
    )
]

option_presets = {}
