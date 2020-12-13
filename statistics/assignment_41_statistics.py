def f(x):
    return 1/x**4

def p(x):
    return 922741.86667/x**4


output = []
k = 68
while sum(output) < 0.95:
    output.append(p(k))
    k += 1
print(k)
print(round(sum(output),2))