#Python 3.10
import random
from collections import Counter

# Function to simulate rolling a six-sided die
def roll_dice():
    return random.randint(1, 6)

# Simulate the experiment of rolling four dice a specified number of times
def simulate_experiment(num_trials):
    outcomes_a = []
    for _ in range(num_trials):
        # Calculate the sum of four random die rolls
        result = sum(roll_dice() for _ in range(4))
        outcomes_a.append(result)
    return outcomes_a

# Compute the Probability Mass Function (PMF) for the outcomes
def compute_pmf(outcomes_a):
    counter = Counter(outcomes_a)
    total_trials = len(outcomes_a)
    # Calculate the probability for each outcome
    pmf = {x: count / total_trials for x, count in counter.items()}
    return pmf

# Run the simulation for Part A and print the PMF
outcomes_a = simulate_experiment(20)
pmf = compute_pmf(outcomes_a)
print("PMF for Part A:")
print(pmf)

# Simulate the experiment of finding the difference between max and min rolls
def simulate_experiment(num_trials):
    outcomes_b = []
    for _ in range(num_trials):
        rolls = [roll_dice() for _ in range(4)]
        max_roll = max(rolls)
        min_roll = min(rolls)
        # Calculate the difference between max and min rolls
        result = max_roll - min_roll
        outcomes_b.append(result)
    return outcomes_b

# Run the simulation for Part B and print the PMF
outcomes_b = simulate_experiment(20)
pmf_b = compute_pmf(outcomes_b)
print("\nPMF for Part B:")
print(pmf_b)
