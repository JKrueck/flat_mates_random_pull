import random
from collections import Counter

# Define the population and their respective frequencies
population = [
    "German", "Italian", "French", "Dutch", "Spanish", "Belgian", "American", "Danish",
    "Hong-Kong", "Polish", "Turkish", "Austrian", "Greek", "Albanian", "Japanese",
    "Australian", "Estonian", "Hungarian", "Chilesian", "Finnish", "Canadian",
    "Indian", "Singaporean", "Swedish", "Argentinian", "Protugese"
]
weights = [
    42, 18, 11, 9, 8, 7, 5, 4,
    4, 3, 2, 2, 2, 1, 1,
    1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1
]

# Perform the sampling 10,000 times
num_samples = 16
num_trials = 1
total_counts = Counter()

for _ in range(num_trials):
    selected_samples = random.choices(population, weights=weights, k=num_samples)
    total_counts.update(selected_samples)

# Output the absolute total counts
print("Absolute counts of pulled samples over 10,000 trials:")
for nationality, count in total_counts.items():
    print(f"{nationality}: {count}")
