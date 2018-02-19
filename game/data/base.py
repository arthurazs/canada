
# =========== #
# P L A C E S #
# =========== #

hotel = {
    'name': 'Creepy Hotel',
}
cinema = {
    'name': 'Abandoned Cinema',
}
house = {
    'name': 'Empty House',
}
office = {
    'name': 'Old Office',
}
police = {
    'name': 'Police Station',
}
market = {
    'name': 'Super Market',
}

places = [hotel, cinema, house, office, police, market]

# =============== #
# V E H I C L E S #
# =============== #

car = {
    'usage': {
        'gas': 13,
        'food': 2,
        'energy': 2
    }
}

motorcycle = {
    'usage': {
        'gas': 7,
        'food': 3,
        'energy': 3
    }
}

foot = {
    'usage': {
        'gas': 0,
        'food': 4,
        'energy': 8
    }
}
vehicle = [car, motorcycle]

# ============= #
# W E A P O N S #
# ============= #

a10mm = {
    'availability': 10
}

pistol = {
    'availability': 30,
    'power': 17,
    'ammo': a10mm,
    'sps': 3  # shots per second
}

a556mm = {
    'availability': 3
}

machine_gun = {
    'availability': 9,
    'power': 32,
    'ammo': a556mm,
    'sps': 13  # shots per second
}

hand = 5  # power
weapons = [pistol, machine_gun]
