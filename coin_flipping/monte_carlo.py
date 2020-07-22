import random
from probability import probability

def monte_carlo(num_heads,num_flips):
    with_num_heads = 0
    for _ in range(1000):
        result = []
        for _ in range(num_flips):
            result.append(random.choice(['H','T']))
        head_count = 0
        for elem in result:
            if elem == 'H':
                head_count+=1
        if head_count == num_heads:
            with_num_heads+=1
    return with_num_heads/1000

