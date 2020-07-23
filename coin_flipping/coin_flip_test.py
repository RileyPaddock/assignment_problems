from probability import probability
from monte_carlo import monte_carlo

print("Monte Carlo Results:")
for _ in range(3):
    print("\n   "+str(monte_carlo(5,8)))

print("\nProbability:")
print("\n   "+str(probability(5,8)))