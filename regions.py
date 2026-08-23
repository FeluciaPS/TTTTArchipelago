from __future__ import annotations

from typing import TYPE_CHECKING

from .entrances import get_all_entrances
from .data.regions import REGION_DEFS

from BaseClasses import Entrance, Region


if TYPE_CHECKING:
    from .world import TTTTWorld

#
# Regions should be pretty limited in this game, most of the game is effortlessly 
# accessible from the start I think it'd be valid to use every enterable building 
# as a region, in case we want to add arbitrary locks to the doors eventually
#
def create_and_connect_regions(world: TTTTWorld) -> None:
    create_regions(world)
    connect_regions(world)

def create_regions(world: TTTTWorld):
    for key in REGION_DEFS:
        region = Region(key, world.player, world.multiworld)
        world.multiworld.regions += [region]

def connect_regions(world: TTTTWorld):
    for entrance in get_all_entrances(world):
        entry = world.get_region(entrance.entry)
        exit = world.get_region(entrance.exit)
        entry.connect(exit, f"{entry} to {exit}", entrance.rule)