# simulator.py
from utils import spin_wheel, is_red, is_black, is_odd, is_even, is_high, is_low
from config import PAYOUTS

class RouletteSimulator:
    def __init__(self):
        self.round = 0

    def spin_and_resolve(self, bet, forced_outcome=None):
        self.round += 1
        outcome = forced_outcome if forced_outcome is not None else spin_wheel()
        win = self.evaluate_bet(bet, outcome)
        payout = self.calculate_payout(bet, win)
        return {
            "round": self.round,
            "outcome": outcome,
            "bet": bet,
            "win": win,
            "payout": payout
        }


    def evaluate_bet(self, bet, outcome):
        bet_type = bet["type"]
        target = bet["target"]
        if bet_type == "straight":
            return outcome == target
        if bet_type == "red":
            return is_red(outcome)
        if bet_type == "black":
            return is_black(outcome)
        if bet_type == "odd":
            return is_odd(outcome)
        if bet_type == "even":
            return is_even(outcome)
        if bet_type == "high":
            return is_high(outcome)
        if bet_type == "low":
            return is_low(outcome)
        return False

    def calculate_payout(self, bet, win):
        if win:
            return bet["amount"] * PAYOUTS[bet["type"]]
        return -bet["amount"]

