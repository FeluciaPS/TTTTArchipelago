from __future__ import annotations

from Options import Choice, Range


################
# Goal Options #
################
class Goal(Choice):
    """
    The goal required to beat the game
    
    - space: Vanilla goal, collect enough Turbo Upgrades and go to space!
    """
    display_name = "Goal"

    option_space = 0
    default = 0

class TurboRequirement(Range):
    """
    Amount of Turbo Upgrades required to go to space.

    IF YOU'RE READING THIS PLEASE SET IT TO 8 NOTHING ELSE WORKS YOU 
    HAVE BEEN WARNED
    """
    display_name = "Required Turbo Upgrades"

    range_start = 1
    range_end = 16

    default = 8

