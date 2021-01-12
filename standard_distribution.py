import math
import matplotlib.pyplot as plt

def f(x): return (1/math.sqrt(2*math.pi))*(math.exp((-x**2)/2))

def num_dec(n):
    if not '.' in str(n):
        return 0
    return len(str(n)) - str(n).index('.')


def calc_standard_normal_probability(a,b,n,rule):
    step = (b-a)/n
    x = a
    scalar = 10**num_dec(step)
    n_range = [elem for elem in [i/scalar for i in range(a*scalar, (b+1)*scalar, int(step*scalar))] if elem <= 1]
    total = 0

    if rule == "left endpoint":
        for i in range(len(n_range) - 1):
            total += f(n_range[i])
    elif rule == "right endpoint":
        for x in n_range[1:]:
            total += f(x)
    elif rule == "midpoint":
        for i in range(len(n_range) - 1):
            total += f((n_range[i] + n_range[i+1])/2)
    elif rule == "trapezoidal":
        for i in range(len(n_range)):
            if i == 0 or i == len(n_range) - 1:
                total += 0.5 * f(n_range[i])
                continue 
            total += f(n_range[i])
    elif rule == "simpson":
        for i in range(len(n_range)):
            if i == 0 or i == len(n_range) - 1:
                total += f(n_range[i])
                continue
            if i % 2 == 1:
                total += 4*f(n_range[i])
                continue
            elif i % 2 == 0:
                total += 2*f(n_range[i])
                continue

    if rule == 'simpson':
        return (step/3) * total
    else:
        return step * total


x_data = [i for i in range(2,100) if i%2 ==0]
for rule in ['left endpoint', 'right endpoint', 'midpoint', 'trapezoidal', 'simpson']:
    y_data = [calc_standard_normal_probability(0,1,i,rule) for i in range(2,100) if i%2 ==0]
    plt.plot(x_data, y_data)
    plt.legend(['left endpoint', 'right endpoint', 'midpoint', 'trapezoidal', 'simpson'])
    plt.savefig('standard_distribution.png')




# x_data = [i for i in range(2,100) if i%2 ==0]
# for rule in ['left endpoint', 'right endpoint', 'midpoint', 'trapezoidal', 'simpson']:
#     y_data = [calc_standard_normal_probability(0,1,i,rule) for i in range(2,100) if i%2 ==0]
#     plt.plot(x_data, y_data)
#     plt.legend(['left endpoint', 'right endpoint', 'midpoint', 'trapezoidal', 'simpson'])
#     plt.savefig('standard_distribution.png')





    



