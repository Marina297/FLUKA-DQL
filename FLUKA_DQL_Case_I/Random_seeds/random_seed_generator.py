"""
random_seed_generator.py

"""

import random
import numpy as np
from datetime import datetime

NUM_SEEDS   = 20          # number of independent runs
SEED_MIN    = 1
SEED_MAX    = 10**10
OUTPUT_FILE = "seed_log.txt"


def generate_seeds(num_seeds: int, seed_min: int, seed_max: int) -> list[int]:
    """Generate a list of unique random integer seeds."""
    seeds = random.sample(range(seed_min, seed_max), num_seeds)
    return seeds


def print_seeds(seeds: list[int]) -> None:
    """Print seeds in a clean formatted table."""
    print("=" * 30)
    print(f"{'Run':<6} {'Seed':>15}")
    print("=" * 30)
    for i, s in enumerate(seeds, 1):
        print(f"{i:<6} {s:>15}")
    print("=" * 30)


def save_seeds(seeds: list[int], filepath: str) -> None:
    """Save seeds to a log file with timestamp for reproducibility."""
    with open(filepath, "w") as f:
        f.write(f"# Random Seed Log\n")
        f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"# Total runs: {len(seeds)}\n")
        f.write(f"# {'Run':<6}\t{'Seed'}\n")
        f.write("-" * 30 + "\n")
        for i, s in enumerate(seeds, 1):
            f.write(f"{i:<6}\t{s}\n")
    print(f"\nSeeds saved to: {filepath}")


def main():
    seeds = generate_seeds(NUM_SEEDS, SEED_MIN, SEED_MAX)
    print_seeds(seeds)
    save_seeds(seeds, OUTPUT_FILE)

    # Optional: set numpy seed with first seed for downstream reproducibility
    np.random.seed(seeds[0])
    print(f"\nNumPy seeded with first seed: {seeds[0]}")


if __name__ == "__main__":
    main()
