import random

def monte_carlo(num_heads,num_flips,num_trials):
    with_num_heads = 0
    for _ in range(num_trials):
        result = [random.choice(['H','T']) for _ in range(num_flips)]
        if result.count('H') == num_heads:
            with_num_heads+=1
    return with_num_heads/num_trials

