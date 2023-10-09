import math

# Define the probability distribution for X
px = { -1: 1/4, 0: 1/2, 1: 1/4 }

# Function to calculate the entropy of a random variable
def entropy(probabilities):
    H = 0
    for p in probabilities:
        if p > 0:
            H -= p * math.log2(p)
    return H

# Calculate the entropy of X
HX = entropy(px.values())

# Calculate the entropies of the other random variables
H2X = entropy([px[x]*px[y] for x in px for y in px])
HX2 = entropy([px[x]**2 for x in px])
H2X_exp = entropy([px[x]*math.log2(2) for x in px])

# Check the statements
A = HX <= math.log2(len(px))  # log2(K) where K is the number of distinct values of X
B = HX <= H2X
C = HX <= HX2
D = HX <= H2X_exp

# Print the results
print("Statement A is :", A)
print("Statement B is :", B)
print("Statement C is :", C)
print("Statement D is :", D)

