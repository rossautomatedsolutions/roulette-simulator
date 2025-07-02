# strategies/reverse_martingale_unlimited.py
from config import BET_LIMITS

class ReverseMartingaleUnlimitedStrategy:
    def __init__(self):
        self.base_bet = BET_LIMITS["outside"]["min"]
        self.current_bet = self.base_bet

    def place_bet(self, bankroll):
        return {
            "type": "red",
            "target": "red",
            "amount": min(self.current_bet, bankroll)
        }

    def update(self, result):
        if result["win"]:
            self.current_bet *= 2
        else:
            self.current_bet = self.base_bet
