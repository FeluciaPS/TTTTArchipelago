from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from rule_builder.options import OptionFilter
from rule_builder.rules import Has
from .option_groups import Goal

if TYPE_CHECKING:
    from .world import TTTTWorld


def set_all_rules(world: TTTTWorld) -> None:
    # No entrance rules here, those are handled in regions.py
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: TTTTWorld) -> None:
    pass


def set_completion_condition(world: TTTTWorld) -> None:
    space_rule = Has("Turbo Upgrade", world.options.turbo_requirement.value) & OptionFilter(Goal, Goal.option_space)

    completion_rule = space_rule
    world.set_completion_rule(completion_rule)