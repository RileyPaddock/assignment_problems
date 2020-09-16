def f(x):
    return 1/x**5

def p(x):
    return 1442309/x**5

output =[]
for x in range(1,26):
    output.append(f(x))
    #print(sum(output))

output = []
k = 25
while sum(output) < 0.95:
    output.append(p(k))
    k += 1
print(k)
print(round(sum(output),2))