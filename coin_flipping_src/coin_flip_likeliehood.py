import matplotlib.pyplot as plt
def find_likeliehood(prob_head, flips):
    heads = len([head for head in flips if head == 'H'])
    tails = len([tail for tail in flips if tail == 'T'])
    if type(prob_head) is float:
        return (prob_head)**heads * (1 - prob_head)**tails
    elif type(prob_head) is str:
        return prob_head+"^"+str(heads)+" * (1 - "+prob_head+")^ "+str(tails)

def range_better(start, end, step = 1):
    result = []
    active = start
    while active < end:
        result.append(round(active,decimal_places(step)))
        active+=step
    return result

def decimal_places(decimal):
    s = str(decimal)
    if '.' not in s:
        return 0
    return len(s) - s.index('.') - 1

print(find_likeliehood(0.5, "HHTTH"))
print(round(find_likeliehood(0.55, "HHTTH"),5))
print(find_likeliehood("p", "HHTTH"))

plt.style.use('bmh')
x_coords = range_better(0,1,0.02)
probablility_results = [find_likeliehood(x,"HHTTH") for x in x_coords]
plt.plot(x_coords,probablility_results,linewidth = 2.5)
plt.legend(['Likeliehood of Flips'])
plt.xlabel('Proability of Heads')
plt.ylabel('Likeliehood of Result')
plt.title("Likeliehood of HHTTH based on different proababilities")
plt.savefig('plot.png')