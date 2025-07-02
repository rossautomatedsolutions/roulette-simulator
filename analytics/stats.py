# analytics/stats.py
import statistics

def summarize(data):
    payouts = [d["payout"] for d in data]
    bankrolls = [d["bankroll"] for d in data]

    total_spins = len(data)
    total_payout = sum(payouts)
    wins = sum([1 for d in data if d["win"]])
    losses = total_spins - wins
    win_rate = (wins / total_spins) * 100 if total_spins else 0
    max_dd = max_drawdown(bankrolls)
    max_win, max_loss = max_streaks(data)
    sharpe = sharpe_ratio(payouts)

    print("===== Simulation Summary =====")
    print(f"Total spins: {total_spins}")
    print(f"Total P&L: {total_payout}")
    print(f"Final bankroll: {bankrolls[-1] if bankrolls else 0}")
    print(f"Win rate: {win_rate:.2f}%")
    print(f"Wins: {wins}, Losses: {losses}")
    print(f"Max Drawdown: {max_dd}")
    print(f"Max Winning Streak: {max_win}")
    print(f"Max Losing Streak: {max_loss}")
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print("================================")


def max_drawdown(bankrolls):
    peak = bankrolls[0] if bankrolls else 0
    max_dd = 0
    for b in bankrolls:
        if b > peak:
            peak = b
        dd = peak - b
        max_dd = max(max_dd, dd)
    return max_dd

def max_streaks(data):
    win_streak = lose_streak = max_win = max_loss = 0
    for d in data:
        if d['win']:
            win_streak += 1
            lose_streak = 0
        else:
            lose_streak += 1
            win_streak = 0
        max_win = max(max_win, win_streak)
        max_loss = max(max_loss, lose_streak)
    return max_win, max_loss

def sharpe_ratio(payouts):
    if len(payouts) < 2:
        return 0
    mean = statistics.mean(payouts)
    stdev = statistics.stdev(payouts)
    return mean / stdev if stdev != 0 else 0

def get_max_losing_streak(data):
    streak = max_streak = 0
    for d in data:
        if not d["win"]:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0
    return max_streak