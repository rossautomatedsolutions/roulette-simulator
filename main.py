# main.py
from simulator import RouletteSimulator
from strategies.flat_bet import FlatBetStrategy
from strategies.martingale import MartingaleStrategy
from strategies.reverse_martingale import ReverseMartingaleStrategy
from analytics.stats import summarize
from config import BET_LIMITS
from utils import spin_wheel
import copy

def run_strategy(name, strategy, spins):
    sim = RouletteSimulator()
    bankroll = 1000
    data = []
    for i, outcome in enumerate(spins):
        if bankroll < BET_LIMITS["outside"]["min"]:
            break

        bet = strategy.place_bet()
        round_data = sim.spin_and_resolve(bet, forced_outcome=outcome)
        bankroll += round_data["payout"]
        round_data["bankroll"] = bankroll
        data.append(round_data)

        if hasattr(strategy, 'update'):
            strategy.update(round_data)

    print(f"\n{name} Strategy:")
    summarize(data)
    return {
        "name": name,
        "spins": len(data),
        "pnl": sum([d["payout"] for d in data]),
        "final_bankroll": data[-1]["bankroll"] if data else 0,
        "win_rate": sum(d["win"] for d in data) / len(data) * 100 if data else 0
    }

def main():
    # Generate a shared spin sequence for fairness
    spins = [spin_wheel() for _ in range(1000)]

    # Instantiate strategies
    strategies = [
        ("Flat Bet", FlatBetStrategy()),
        ("Martingale", MartingaleStrategy()),
        ("Reverse Martingale", ReverseMartingaleStrategy())
    ]

    results = []
    for name, strat in strategies:
        # Deepcopy ensures isolated state
        strat_copy = copy.deepcopy(strat)
        results.append(run_strategy(name, strat_copy, spins))

    # Summary Table
    print("\n=== Comparison Table ===")
    print(f"{'Strategy':20} {'Spins':>6} {'P&L':>8} {'Bankroll':>10} {'Win Rate':>10}")
    for r in results:
        print(f"{r['name']:20} {r['spins']:>6} {r['pnl']:>8.0f} {r['final_bankroll']:>10.0f} {r['win_rate']:>9.2f}%")
    print("=========================\n")

if __name__ == "__main__":
    main()
