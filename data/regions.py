from .region_names import HAT_STORES, OVERWORLD_AREA_NAMES, OVERWORLD_NAME

REGION_DEFS = {
    OVERWORLD_NAME: {},
    "The Generator": {
        "parent": OVERWORLD_NAME
    },
    "Binnenrot Apartment Building": {
        "parent": OVERWORLD_NAME,
        "required_items": {
            "Binnenrot Key": 1,
            "Progressive Apartment Key": 1
        }
    },
    "Terry's Apartment": {
        "parent": "Binnenrot Apartment Building",
        "required_items": {
            "Terry Apartment Keys": 1,
            "Progressive Apartment Key": 2
        }
    }
}

REGION_DEFS[OVERWORLD_NAME] = {}

for area in OVERWORLD_AREA_NAMES:
    REGION_DEFS[f"Overworld: {area}"] = {
        "parent": OVERWORLD_NAME
    }

for index, color in enumerate(HAT_STORES):
    store = f"Hat Store ({color})"
    REGION_DEFS[store] = {
        "parent": OVERWORLD_NAME,
        "required_items": {
            f"Hat Store {color} Key": 1,
            "Progressive Hat Store Key": index + 1
        }
    }

INDOOR_KEYS = {
    "Pet Store": "Pet Store Key", 
    "City Hall": "City Hall Key",
    "Beach Club": "Beach Club Key",
    "Junk Store": "Junk Store Key",
    "Laundry House": "Laundry Key",
    "Zmiraphy's Garage": "Garage Key"
}

for name, key in INDOOR_KEYS.items():
    REGION_DEFS[name] = {
        "parent": OVERWORLD_NAME,
        "required_items": {
            key: 1
        }
    }