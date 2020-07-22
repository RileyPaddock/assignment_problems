from probability import probability
from monte_carlo import monte_carlo

print("Monte Carlo Results:")
for _ in range(3):
    print("\n   "+str(monte_carlo(3,5)))

print("\nProbability:")
print("\n   "+str(probability(3,5)))