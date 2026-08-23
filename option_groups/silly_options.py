from Options import Toggle, Visibility

#################
# Silly Options #
#################


class DutchItemNames(Toggle):
    """
    In the spirit of TTTT, replaces archipelago item names with Dutch ones.
    """
    display_name = "Dutch Item Names"

    # Maybe: visibility = Visibility.template | Visibility.complex_ui | Visibility.spoiler
    # Probably shouldn't be visible by default on an options page, but for now
    # I'm only putting it in spoiler logs.
    visibility = Visibility.spoiler