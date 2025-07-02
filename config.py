# config.py

# Standard roulette payouts
PAYOUTS = {
    # Inside bets
    "straight": 35,     # single number
    "split": 17,        # two adjacent numbers
    "street": 11,       # three in a row (horizontal)
    "corner": 8,        # four numbers in a square
    "six_line": 5,      # two adjacent streets (6 numbers)

    # Outside bets
    "column1": 2,
    "column2": 2,
    "column3": 2,
    "dozen1": 2,
    "dozen2": 2,
    "dozen3": 2,
    "red": 1,
    "black": 1,
    "odd": 1,
    "even": 1,
    "high": 1,     # 19–36
    "low": 1       # 1–18
}


# Min/max bets
BET_LIMITS = {
    "inside": {"min": 20, "max": 500},
    "outside": {"min": 20, "max": 500}
}

# American roulette wheel numbers (0 and 00 represented separately)
WHEEL_NUMBERS = [0, '00'] + list(range(1, 37))

# Red/black mapping (standard American wheel)
RED_NUMBERS = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
BLACK_NUMBERS = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}
