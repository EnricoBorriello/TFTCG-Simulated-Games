# TFTCG Simulated Games

This repository contains a simulation framework for analyzing strategies in the **Transformers Trading Card Game (TFTCG)**. The goal is to explore how different deck compositions and team structures affect game outcomes using probabilistic simulations.

---

## Overview

Using simplified combat rules inspired by the TFTCG, this notebook runs thousands of simulated battles between teams of varying size ("1-tall" to "5-wide") and deck archetypes ("mono-blue" to "mono-orange"). Each match-up is repeated multiple times to estimate:

- Win/loss rates
- Average number of turns per game
- Matchups that result in never-ending loops

Results can be visualized via heatmaps to easily compare strategy effectiveness.

---

## Background

The simulation abstracts key elements of the TFTCG:

- **Characters**: Each team is made up of simplified bots with stats `[attack, defense, health, damage_taken, tapped]`.
- **Decks**: Composed of battle cards (orange/blue/white pips), affecting attack and defense through the "bold" and "tough" mechanics.
- **Combat**: Turn-based combat using simplified flipping logic and KO rules.
- **Strategy**: The simulation tests combinations of:
  - Team size (1–5 characters)
  - Deck type (bias toward offense/defense)
  - Bold and tough values (aggressiveness/resilience)

---

## File Structure

- `Simulating Games.ipynb`: Main notebook containing:
  - Simulation logic
  - Game mechanics
  - Strategy testing
  - Heatmap visualization of results
- `old_CL_package.py`: External utility module (required, not included in repo)
  - Functions for deck generation and flipping logic

> If this package is not available locally, you’ll need to implement or mock `generate_deck()` and `generate_flipped_icons()` functions to run the notebook.

---

## Example Visualizations

Two primary heatmaps are generated:

- **Win Rate Heatmap** – how often a strategy wins against others.
- **Average Turns Heatmap** – how long matchups typically last.

The color-coded results make it easy to identify dominant strategies or problematic endless loops (highlighted with visual markers like red or gray circles).

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/EnricoBorriello/TFTCG-Simulated-Games.git
   cd TFTCG-Simulated-Games

2. Open the Jupyter notebook:
   ```bash
    jupyter notebook "Simulating Games.ipynb"
---

## Dependencies
This project uses the following Python libraries:

numpy

pandas

matplotlib

You can install them via pip:
   ```bash
    pip install numpy pandas matplotlib
   ```

---

## Notes
The notebook is designed to simulate simplified TFTCG mechanics and does not model the full official ruleset.

Execution time grows significantly with more simulations (num_games), so keep that in mind when scaling.

Ensure your environment includes the helper module old_CL_package.py or rewrite the logic using included examples.
---
## License
MIT License.
This is an educational project and not affiliated with Hasbro or Wizards of the Coast.
