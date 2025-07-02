# Roulette Strategy Simulator & AI Agent Training

This project explores classic and adaptive betting strategies in **American roulette** using simulation, reinforcement learning, and deep Q-networks (DQN). It answers one of the oldest questions in gambling:

 *Can you beat the house with smart betting or machine learning?*

---

## Project Highlights

- Simulates **100,000+ spins** of roulette
- Trains agents using:
  - Flat & Martingale strategies
  - Q-learning (tabular)
  - Risk-aware agents with drawdown awareness
  - Deep Q-Network (DQN) agent using PyTorch
- Tracks survival, drawdowns, win rate, and bankroll
- Compares all strategies using batch testing and visualizations

---

## Notebooks

| Notebook | Description |
|---------|-------------|
| `01_Simulation_Introduction.ipynb` | Classical strategies: Flat Bet, Martingale, Reverse Martingale |
| `02_Adaptive_Q_Learning.ipynb` | Tabular Q-learning agent that learns from win/loss history |
| `03_Risk_Aware_Q_Learning.ipynb` | Adds drawdown and streak penalties to shape behavior |
| `04_DQN_Roulette_Agent.ipynb` | Deep Q-Network (PyTorch) trained on roulette environment |

Each notebook:
- Defines a custom environment
- Trains or simulates agents
- Evaluates performance over 100+ test runs
- Visualizes outcomes: bankrolls, drawdowns, survival

---
