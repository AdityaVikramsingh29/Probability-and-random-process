from scipy.stats import binom

# Define the parameters
n = 7  # Number of trials (shooting 7 times)
p = 0.25  # Probability of success (hitting the target)

# Calculate the probability of hitting the target at least twice
probability_at_least_twice = 1 - binom.cdf(1, n, p)

print(f"The probability of hitting the target at least twice is approximately {probability_at_least_twice:.4f}")

