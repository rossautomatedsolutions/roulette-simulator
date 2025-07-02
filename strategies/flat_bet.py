# strategies/flat_bet.py
from config import BET_LIMITS

class FlatBetStrategy:
    def __init__(self):
        self.bet_amount = BET_LIMITS["outside"]["min"]

    def place_bet(self, bankroll):
        return {
            "type": "red",
            "target": "red",
            "amount": self.bet_amount
        }

    def update(self, result):
        pass
