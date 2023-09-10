from scipy.stats import binom
import random
from scipy.stats import bernoulli
# Define the parameters
n = 7  # Number of trials (shooting 7 times)
p = 0.25  # Probability of success (hitting the target)

# Calculate the probability of hitting the target at least twice
probability_at_least_twice = 1 - binom.cdf(1, n, p)

print(f"The probability of hitting the target at least twice is approximately {probability_at_least_twice:.4f}")

# Number of simulations
num_simulations = 100000

# Initialize a counter to keep track of successful simulations
successful_simulations = 0

# Simulate the scenario num_simulations times
for _ in range(num_simulations):
    hits = sum(random.random() < p for _ in range(n))
    if hits >= 2:
        successful_simulations += 1

# Calculate the simulated probability
simulated_probability = successful_simulations / num_simulations

print(f"Simulated probability of hitting at least twice in {n} shots: {simulated_probability:.4f}")

data_bern = bernoulli.rvs(size=10,p=0.25)
print("Samples generated:",data_bern)

