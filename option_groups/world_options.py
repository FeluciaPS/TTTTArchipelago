from Options import Choice, Toggle


#################
# World Options #
#################
class LockDoors(Choice):
    """
    Locks the various doors in the game with keys to create more progression gates

    - off: All doors are unlocked
    - apartment_only: Just like in the base game, entering terry's apartment requires the apartment key
    - on: Locks all doors, requiring "key" items to open them.
    """
    display_name = "Lock Doors"

    option_off = 0
    option_apartment_only = 1
    option_on = 2
    
    default = 1


class ProgressiveKeys(Choice):
    """
    Replaces specific keys with progressive ones, unlocking them in order. 
    Does nothing if Lock Doors isn't set to "on"

    - off: Uses specific keys for all doors
    - apartment: Always unlocks the apartment building first, and the apartment second
    - hat_shop: Always unlocks the Green hat store first, then Red, then Blue
    - all: All of the above
    """
    display_name = "Progressive Keys"

    option_off = 0
    option_apartment = 1
    option_hat_shop = 2
    option_all = 3

    default = 3

class StartWithTurboUpgrade(Toggle):
    """
    Starts off the game with 1 turbo upgrade unlocked.
    Because going fast is fun.
    """
    display_name = "Start With Turbo Upgrade"

class RandomizeMap(Choice):
    """
    Randomizes the map unlock 
    """
    display_name = "Randomize Map"

    option_off = 0
    option_early = 1
    option_on = 2

    default = 1