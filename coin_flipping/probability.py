def probability(num_heads, num_flips):
    num_possibilities = 2**(num_flips)
    num_heads = factorial(num_flips)/(factorial(num_heads)*factorial(num_flips - num_heads))
    return num_heads/num_possibilities

def factorial(x):
    if x == 0:
        return 1
    else:
        to_be_factorial = x
        for value in range(1,x):
            to_be_factorial*= value
    return to_be_factorial



