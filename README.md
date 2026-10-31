# Hawk-Dove ESS Simulation

A simple agent-based simulation of the Hawk-Dove game, a classic evolutionary game theory model demonstrating Evolutionarily Stable Strategies (ESS).

## What is this?

In the Hawk-Dove game, individuals compete for limited food resources with two strategies:
- **Hawk**: Aggressive strategy - fights for resources, risking injury
- **Dove**: Peaceful strategy - displays or retreats, avoiding injury

## How it works

The simulation models population dynamics over generations:
1. At each generation, creatures are randomly assigned to food spots (20 food units total)
2. When two creatures compete for the same food spot, they play the Hawk-Dove game
3. Payoffs determine offspring production
4. The population evolves based on strategy success

## Running the simulation

```bash
python main.py
```

This will generate `output.png` showing the population dynamics over time.

## Example Output

![Hawk-Dove Population Dynamics](https://media.licdn.com/dms/image/v2/D4E2DAQEDA83ByewT2g/profile-treasury-image-shrink_8192_8192/B4EaFgH3nGHAAU-/0/1792614038197?e=1794013200&v=beta&t=FDefUEd_bgI-NDuP5gEVujmD_t54dQbQyprQYA7TpRo)
