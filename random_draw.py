import random
def random_draw(distribution):
    cum_dist = [sum([distribution[j] for j in range(len(distribution)) if j<=i]) for i in range(len(distribution))]

    randint = random.randint(0,10000)/10000

    i = 0
    while randint > cum_dist[i]:
        i+=1
    
    return i
for test_dist in [[0.5, 0.5],[0.25, 0.25, 0.5],[0.05, 0.2, 0.15, 0.3, 0.1, 0.2]]:
    test = []
    for i in range(1000):
        test.append(random_draw(test_dist))
    print("Distribution: "+str(test_dist))
    print(" (expected,average)")
    for j in range(len(test_dist)):
        print(" "+str((test_dist[j],(test.count(j)/len(test)))))



