import math
from probability import probability
flips = {
    'George': ['THTH', 'HTHT',  'THTH',  'HHTH',  'THTH',  'TTHT',  'THTH',  'TTTH',  'THTH',  'TTHT',  'THHT',  'HTTH',  'THTH',  'THHT',  'THHT',  'THTH',  'THTH',  'THHT',  'THTH',  'THTH'],
    'David': ['TTHH',  'HHTT',  'HHTT',  'TTHH',  'HTHT',  'THTH',  'THTH',  'THTH',  'HTHT',  'HTHT',  'THTH',  'HTHT',  'THHH',  'THTH',  'HHTT',  'HHTT',  'TTTH',  'HHTH',  'HTHH',  'TTTH'],
    'Elijah': ['THTT',  'HTHT',  'HTHH',  'HHHT',  'TTHH',  'THHH',  'TTTT',  'HHTT',  'TTTH',  'TTHH',  'HTHT',  'HTHT',  'TTTT',  'HTTT',  'TTTH',  'HTTT',  'TTHH',  'THTH',  'THHH',  'HTHH', ''],
    'Colby': ['HTTH',  'HTHH',  'THTT',  'HHTH',  'TTHT',  'HTTT',  'THHH',  'TTHH',  'HHTT',  'THTH',  'HHTT',  'THTH',  'THHH',  'TTHH',  'THTT',  'HHTH',  'HTTH',  'HTHH',  'TTHT',  'HTTT'],
    'Justin': ['THTT',  'HTHT',  'TTTH',  'THHT',  'HTHH',  'TTTH',  'THTH',  'HHTH',  'TTTT',  'HTTH',  'HHTT',  'THHH',  'HHHH',  'THTH',  'HTTH',  'TTHH',  'HTHT',  'HHHT',  'THHT',  'TTTH']
}
probability_results = [probability(x,4) for x in range(5)]
person_results = {}

def analyze_coinset(num_heads,coinset):
    num_succesful_results = 0
    for coindata in coinset:
        heads = 0
        for outcome in coindata:
            if outcome == 'H':
                heads+=1
        if heads == num_heads:
            num_succesful_results+=1
    return num_succesful_results/len(coinset)

def kl_divergence(p,q):
    divergence = 0
    for i in range(len(p)):
        divergence += p[i]*(math.log(p[i]/q[i]))
    return divergence

def fix_zeroes(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 0.0001
    return arr

for person in flips:
    person_results[person] = []
    for i in range(5):
        person_results[person].append(analyze_coinset(i,flips[person]))
for person in person_results:
    print("\nTesting "+ person)
    print(kl_divergence(probability_results,fix_zeroes(person_results[person])))

print("Justin had the best approximation of randomness because his dataset had the least divrgencce from the true data.")