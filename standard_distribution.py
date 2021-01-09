import math

def f(x): return (1/((2*math.pi)**(0.5))) * math.exp(1)**((x**2)/-2)

def calc_standard_normal_probability(start, stop):
    total = 0
    active_x = start
    while active_x < stop:
        total+=(f(active_x)* 0.001)
        active_x += 0.001
    return total



print([calc_standard_normal_probability(-1,1), calc_standard_normal_probability(-2,2), calc_standard_normal_probability(-3,3)])