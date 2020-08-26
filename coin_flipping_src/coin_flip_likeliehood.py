import matplotlib.pyplot as plt
def compute_likeliehood(prob_head, flips):
    heads = len([head for head in flips if head == 'H'])
    #find the number of heads in the set of flips
    tails = len([tail for tail in flips if tail == 'T'])
    # find the number of tails in the flip
    if type(prob_head) is float:
        return (prob_head)**heads * (1 - prob_head)**tails
        #evalute the likeliehood of the flip
    elif type(prob_head) is str:
        return prob_head+"^"+str(heads)+" * (1 - "+prob_head+")^ "+str(tails)
        #show an equation for the likeliehood of the flip

def range_better(start, end, step = 1):
    result = []
    active = start
    s = str(step)
    while active < end:
        if '.' not in s:
            result.append(active)
            #if theres no decimal place in the step size just append normally
        else:
            num_decimal_places = len(s) - (s.index('.') + 1)
            result.append(round(active, num_decimal_places))
            #if there is a decimal place in the step size then find the number of decimal places and make sure to only have that many decimal places on the number.
        active+=step
    return result

print(compute_likeliehood(0.5, "HHTTH"))
print(round(compute_likeliehood(0.55, "HHTTH"),5))
print(compute_likeliehood("p", "HHTTH"))

plt.style.use('bmh')
x_coords = range_better(0,1,0.02)
probablility_results = [compute_likeliehood(x,"HHTTH") for x in x_coords]
plt.plot(x_coords,probablility_results,linewidth = 2.5)
plt.legend(['Likeliehood of Flips'])
plt.xlabel('Proability of Heads')
plt.ylabel('Likeliehood of Result')
plt.title("Likeliehood of HHTTH based on different proababilities")
plt.savefig('coin_flip_likeliehood.png')