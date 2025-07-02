# analytics/tracker.py
import csv
from datetime import datetime
import os

class Tracker:
    def __init__(self):
        self.data = []
        dt = datetime.now().strftime("%Y%m%d")
        self.filename = f"logs/game_{dt}.csv"
        os.makedirs("logs", exist_ok=True)
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["round", "outcome", "bet_type", "bet_target", "amount", "win", "payout", "bankroll"])

    def log(self, round_data, bankroll):
        self.data.append(round_data)
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                round_data["round"],
                round_data["outcome"],
                round_data["bet"]["type"],
                round_data["bet"]["target"],
                round_data["bet"]["amount"],
                round_data["win"],
                round_data["payout"],
                bankroll
            ])
