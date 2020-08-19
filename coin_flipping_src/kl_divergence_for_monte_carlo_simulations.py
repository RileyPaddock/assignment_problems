import math
from monte_carlo import monte_carlo
from probability import probability

def kl_divergence(p,q):
    divergence = 0
    for i in range(len(p)):
        divergence += p[i]*(math.log(p[i]/q[i]))
    return divergence

def fix_zeroes(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 0.0001
    return arr

probability_results = [probability(x,10) for x in range(10)]
monte_carlo_100 = fix_zeroes([monte_carlo(x,10,100) for x in range(10)])
monte_carlo_1000 = fix_zeroes([monte_carlo(x,10,1000) for x in range(10)])
monte_carlo_10000 = [monte_carlo(x,10,10000) for x in range(10)]
print("\nDivergence with 100 trials: ")
print("\n   "+str(kl_divergence(probability_results,monte_carlo_100)))
print("\nDivergence with 1000 trials: ")
print("\n   "+str(kl_divergence(probability_results,monte_carlo_1000)))
print("\nDivergence with 1000 trials: ")
print("\n   "+str(kl_divergence(probability_results,monte_carlo_10000)))

# As the number of samples increases, the KL divergence gets closer to 0 because as the number of trials increases the monte_carlo estimation gets closer and closer the the actual probability.